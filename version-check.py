#!/usr/bin/python3


#
# mvn -Doutput=effective-pom.xml help:effective-pom
#

from xml.etree import ElementTree as ET
import argparse
import csv
import logging
import sys
import requests

logger = logging.getLogger()


class VersionChecker(object):
    '''
    Class for checking the versions within an effective pom against a list of known repos
    '''

    NS = '{http://maven.apache.org/POM/4.0.0}'

    def __init__(self, pom, ignore, repos=None):
        self._ok = True
        self._root = ET.parse(pom).getroot()
        self._repos = []
        for repo in self._root.findall(VersionChecker.NS + 'distributionManagement/' +
                                       VersionChecker.NS + 'snapshotRepository/' +
                                       VersionChecker.NS + 'url'):
            self._repos.append(repo.text)
        for repo in self._root.findall(VersionChecker.NS + 'distributionManagement/' +
                                       VersionChecker.NS + 'repository/' +
                                       VersionChecker.NS + 'url'):
            self._repos.append(repo.text)
        if repos is not None:
            for repo in repos:
                self._repos.append(repo)
        self._ignore = {}
        if ignore is not None:
            with open(ignore) as csvfile:
                for row in csv.reader(csvfile):
                    row = [r.strip() for r in row]
                    if len(row) < 3:
                        raise Exception("ignore file is csv with group,artifact,version[,version...]")
                    if row[0] not in self._ignore:
                        self._ignore[row[0]] = {}
                    if row[1] not in self._ignore[row[0]]:
                        self._ignore[row[0]][row[1]] = set()
                    for version in row[2:]:
                        self._ignore[row[0]][row[1]].add(version)
        self._cache = {}
        self._requests = requests.session()

    def _find_ignore_list(self, group_id, artifact_id):
        if group_id in self._ignore:
            ign = self._ignore[group_id]
            if artifact_id in ign:
                return ign[artifact_id]
            if '*' in ign:
                return ign['*']
        while '.' in group_id:
            group_id = group_id[0:group_id.rindex('.')]
            if group_id + '.*' in self._ignore:
                ign = self._ignore[group_id + '.*']
                if artifact_id in ign:
                    return ign[artifact_id]
                if '*' in ign:
                    return ign['*']
        return set()
    
    def _fetch_versions(self, group_id, artifact_id, require_snapshot=False):
        ignore = self._find_ignore_list(group_id, artifact_id)
        if ignore == set(['*']):
            return False

        if group_id in self._cache and artifact_id in self._cache[group_id]:
            release, snapshot, row = self._cache[group_id][artifact_id]
            if not require_snapshot or snapshot is not None:
                return True
        
        path = group_id.replace('.', '/') + '/' + artifact_id + '/maven-metadata.xml'
        for repo in self._repos:
            url = repo + '/' + path
            resp = self._requests.get(url, headers = {'Accept': 'text/xml, application/xml'})
            if resp.status_code == 404:
                continue
            if resp.status_code != 200:
                logger.warning("Got status code: %(status)d for %(url)s", dict(status=resp.status_code, url=url))
                continue
            else:
                release = None
                snapshot = None
                versions = []
                for v in ET.fromstring(resp.content).findall('versioning/versions/version'):
                    version = v.text
                    if version in ignore:
                        continue
                    versions.append(version)
                    if version.endswith('-SNAPSHOT'):
                        snapshot = version
                    else:
                        release = version
                if require_snapshot and snapshot is None:
                    continue
                if group_id not in self._cache:
                    self._cache[group_id] = {}
                versions.reverse()
                row = [group_id, artifact_id] + versions
                self._cache[group_id][artifact_id] = (release, snapshot, row)
                logger.debug("Got versions from %(url)s", dict(url=url))
                return True
        logger.error("Didn't find %(group)s:%(artifact)s in ay repo",
                     dict(group=group_id, aritfact=artifact_id))
        return False


    def _check_version(self, group_id, artifact_id, version):
        is_snapshot = version.endswith('-SNAPSHOT')
        if self._fetch_versions(group_id, artifact_id, require_snapshot=is_snapshot):
            release, snapshot, row = self._cache[group_id][artifact_id]
            if version not in set([release, snapshot]):
                self._ok = False
                logger.warning("Newer version found for: %(group)s:%(artifact)s version: %(version)s <> %(expected)s",
                            dict(group=group_id, artifact=artifact_id, version=version,
                                 expected=snapshot if is_snapshot else release))
                logger.info("Known versions: %(row)s", dict(row=", ". join(row)))

    def _check_plugins(self):
        for plugin in self._root.findall('.//' + VersionChecker.NS + 'plugin'):
            group_id = plugin.find(VersionChecker.NS + 'groupId')
            artifact_id = plugin.find(VersionChecker.NS + 'artifactId')
            version = plugin.find(VersionChecker.NS + 'version')
            if artifact_id is None:
                continue
            if group_id is None:
                group_id = 'org.apache.maven.plugins'
            else:
                group_id = group_id.text
            artifact_id = artifact_id.text
            if version is not None:
                version = version.text
            self._check_version(group_id, artifact_id, version)

    def _check_dependencies(self):
        for dependency in self._root.findall('.//' + VersionChecker.NS + 'dependency'):
            group_id = dependency.find(VersionChecker.NS + 'groupId')
            artifact_id = dependency.find(VersionChecker.NS + 'artifactId')
            version = dependency.find(VersionChecker.NS + 'version')
            if group_id is None or artifact_id is None:
                continue
            group_id = group_id.text
            artifact_id = artifact_id.text
            if version is not None:
                version = version.text
            self._check_version(group_id, artifact_id, version)
        
    def check(self):
        self._check_plugins()
        self._check_dependencies()
        return self._ok


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check dependency and plugin versions.')
    parser.add_argument('--pom', metavar='POM', dest='pom',
                        default="effective-pom.xml",
                        help='Processed pom to check versions in')
    parser.add_argument('--ignore-file', metavar='CSVFILE', dest='ignore',
                        help='Repository versions to ignore')
    parser.add_argument('--log-level', metavar='LEVEL', dest='level',
                        default="INFO",
                        help='Logger is limited to this level')
    parser.add_argument('--repositories', metavar='URL', nargs='*', dest='repos',
                        default=['https://repo1.maven.org/maven2'],
                        help='Extra repositories to use')

    args = parser.parse_args()

    logging.basicConfig(level=args.level.upper(), force=True)

    vc = VersionChecker(args.pom, args.ignore, args.repos)
    if not vc.check():
        sys.exit(1)
