#!/bin/bash

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

