#!/bin/bash

# get the latest commit message
commit_msg=$(git log -1 --pretty=%B)

# check if the commit was made to the main branch
if [ "$GITHUB_REF" = "refs/heads/main" ]; then
  # extract the version number from the commit message
  version_number=$(echo $commit_msg | grep -o -E 'v[0-9]+\.[0-9]+\.[0-9]+' | head -1)

  # create a new release with the version number and tag it as "latest"
  git tag -a $version_number -m "Release $version_number"
  git tag -fa latest -m "Latest release"
  git push --tags --force
fi
