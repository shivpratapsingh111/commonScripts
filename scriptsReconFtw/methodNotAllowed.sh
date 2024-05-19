#!/bin/bash

directory=$1
rm allResponses.txt 
if [ "$#" -eq 0 ]; then
    echo "Usage: "
    echo $1" /home/chad/OutputFolder/screenshots/organised/methodNotAllowed"
else
    for file in "$directory"/*; do
        name=$(basename "$file")
        name="${name//_//}"
        name="${name%.png}"


        req=$(curl -X POST -k "$name")
        echo "==============================================================" >> allResponses.txt
        echo "$name" >> allResponses.txt
        echo "Method: POST" >> allResponses.txt
        echo "-----" >> allResponses.txt
        echo "$req" >> allResponses.txt


        #OPTIONS req
        req=$(curl -X OPTIONS -i -k "$name")
        echo "-----" >> allResponses.txt
        echo "Method: OPTIONS" >> allResponses.txt
        echo "-----" >> allResponses.txt
        echo "$req" >> allResponses.txt

    done
fi
