#!/bin/bash

TARGET=$1

if [ "$#" -eq 0 ]
then 
	echo "Provide the direcotry path"
	echo "Usage: "
	echo "./script.sh OutputFolder/google.com"
	exit 1
fi

cd "$1/fuzzing/"

for file in *; do
	if [ -f "$file" ]; then
	cat $file | grep -P '^2\d{2}' >> 200
	cat $file | grep -P '^3\d{2}' >> 302
	cat $file | grep -P '^4\d{2}' >> 403
	cat $file | grep -P '^5\d{2}' >> 500
	fi
done
mkdir all
mv *.txt all/

