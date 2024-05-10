#!/bin/bash

# Define the output file
output_file="combined_output.txt"

# Iterate through each subdirectory
for dir in */; do
    # Extract the directory name
    dir_name=$(basename "$dir")

    # Print the directory name to the output file
    echo "====================$dir_name====================" >> "$output_file"
    echo "" >> "$output_file"

    # Cat the content of txt file to the output file
    cat "${dir}cms.json" >> "$output_file"

    # Add a newline for separation
    echo "" >> "$output_file"
    echo "" >> "$output_file"

done

echo "Combined output saved to $output_file"
