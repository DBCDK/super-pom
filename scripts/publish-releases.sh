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

for JDK in java11 java8
do
  # create -old- branch
  echo git checkout $JDK
  echo git checkout -b "$JDK-$oldVersion"
  echo mvn versions:set -DgenerateBackupPoms=false -DnewVersion="$JDK-$oldVersion"
  echo git commit -a -m "Autoupdate version to $JDK-$oldVersion"
  echo git push --set-upstream origin "$JDK-$oldVersion"

  # update $JDK branch
  echo git checkout $JDK
  echo git merge master
done

echo git checkout master
echo git push --all origin
