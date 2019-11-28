#!/usr/bin/env bash
set -e

newOldVersion=$1
if [[ -z "$newOldVersion" ]] ; then
  newOldVersion="old-$(date +%Y%V)"
  echo new ${newOldVersion}
fi

echo "changing latest to $newOldVersion"
echo creating new latest from master
read -p "Press enter to continue"

# Create new old-xxx
git checkout latest
git branch -m "$newOldVersion"
git push origin :latest
git push --set-upstream origin "$newOldVersion"
mvn versions:set -DgenerateBackupPoms=false -DnewVersion=${newOldVersion}
git commit -a -m "Auto update version to $newOldVersion"
git push
# create new latest
git checkout master
git checkout -b latest
mvn versions:set -DgenerateBackupPoms=false -DnewVersion=latest-SNAPSHOT
git commit -a -m "Auto update pom version to latest-SNAPSHOT"
git checkout master
git push --all origin
