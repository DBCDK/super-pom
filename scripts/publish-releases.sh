#!/usr/bin/env bash
set -e

# Payara 6 -> 7 migration roadmap. Update the two lists as each step happens.
# A frozen branch must never receive master, it would change payara line
# under an unchanged SNAPSHOT version.
#
#   step                                          MERGE_MASTER_BRANCHES    FROZEN_BRANCHES
#   now                                           java21-payara7           java25 java21 java21-payara6 java17
#   cutoff (merge master into java21 by hand)     java21 java21-payara7    java25 java21-payara6 java17
#   java21-payara7 no longer used as parent       java21                   java25 java21-payara6 java17
#   no projects left on payara6                   java21                   java25 java17
#   java25 approved (merge master by hand once)   java21 java25            java17
#   java17 retired                                java21 java25            (empty)

# Branches that receive master on bump day.
MERGE_MASTER_BRANCHES="java21-payara7"
# Branches that only get a frozen -old- copy. They stay on their own payara line
# and receive changes by cherry-pick, never by merging master.
FROZEN_BRANCHES="java25 java21 java21-payara6 java17"

function die() {
  echo "Error : $*"
  echo "use $0 old-20yyww"
  exit 1
}

function create_old_branch() {
  local branch=$1
  git checkout "$branch"
  git checkout -b "$branch-$oldVersion"
  mvn versions:set -DgenerateBackupPoms=false -DnewVersion="$branch-$oldVersion"
  mvn install
  git commit -a -m "Autoupdate version to $branch-$oldVersion"
  git push --set-upstream origin "$branch-$oldVersion"
}

# Wrapped in main so bash parses the whole script before git checkout
# replaces this file with another branch's version.
function main() {
  oldVersion=$1

  if [ -z "$oldVersion" ] ; then
    oldVersion="old-$(date +%Y%V)"
  fi

  [[ ! $oldVersion =~ ^old-20[0-9]{4}$ ]] && die "argument must match old-20yyww"

  echo "creating new releases from master"
  echo "setting old version to $oldVersion"
  echo "merging master into: $MERGE_MASTER_BRANCHES"
  echo "frozen copy only:    $FROZEN_BRANCHES"
  read -p "Press enter to continue"

  git checkout master
  git pull

  for branch in $MERGE_MASTER_BRANCHES $FROZEN_BRANCHES
  do
    create_old_branch "$branch"
  done

  for branch in $MERGE_MASTER_BRANCHES
  do
    git checkout "$branch"
    git merge master
  done

  git checkout master
  git push --all origin
}

main "$@"
exit
