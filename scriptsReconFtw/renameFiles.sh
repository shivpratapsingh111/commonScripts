#!/bin/bash
directory=$1

if [ "$#" -eq 0 ]; then
    echo 'Usage:'
    echo $0' /home/users/chad/OuputFolder/screenshots/'
else
    for file in "$directory"/*; do
        name=$(basename "$file")
        name="${name//_//}"
        echo $name
    done
fi
