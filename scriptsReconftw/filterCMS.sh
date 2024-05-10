#!/bin/bash

shopt -s extglob

TARGET=$1
output_file="combined_output.txt"

cd "$1/cms/"
mkdir all

for dir in */; do
	dir_name=$(basename "$dir")
	if [ -d "$dir" ]; then
		if [ "$dir_name" != "all" ]; then

    		echo "====================$dir_name====================" >> "$output_file"
    		echo "" >> "$output_file"

    		cat "${dir}cms.json" >> "$output_file"

    		echo "" >> "$output_file"
    		echo "" >> "$output_file"
			
			mv "$dir_name" all

		fi
	fi

done

echo "Combined output saved to $output_file"
