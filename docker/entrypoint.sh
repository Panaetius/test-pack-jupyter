#!/bin/bash

if [[ -v GIT_AUTHOR_NAME && -v EMAIL && -v CI_PROJECT ]];
then
    # Setup git user
    if [ -z "$(git config --global --get user.name)" ]; then
        git config --global user.name "$GIT_AUTHOR_NAME"
    fi
    if [ -z "$(git config --global --get user.email)" ]; then
        git config --global user.email "$EMAIL"
    fi

fi





# run the command
$@

