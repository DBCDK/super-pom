#!/usr/bin/env bash
set -e

function die() {
  echo "Error : $*"
  echo "use $0 old-20yyww"
  exit 1
}

oldVersion=$1

if [ -z "$oldVersion" ] ; then
  oldVersion="old-$(date +%Y%V)"
fi

[[ ! $oldVersion =~ ^old-20[0-9]{4}$ ]] && die "argument must match old-20yyww"

echo "creating new releases from master"
echo "setting old version to $oldVersion"
read -p "Press enter to continue"

git checkout master
git pull

for JDK in java25 java21 java17
do
  # create -old- branch
  git checkout $JDK
  git checkout -b "$JDK-$oldVersion"
  mvn versions:set -DgenerateBackupPoms=false -DnewVersion="$JDK-$oldVersion"
  mvn install
  git commit -a -m "Autoupdate version to $JDK-$oldVersion"
  git push --set-upstream origin "$JDK-$oldVersion"

  # update $JDK branch
  git checkout $JDK
  git merge master
done

git checkout master
git push --all origin
