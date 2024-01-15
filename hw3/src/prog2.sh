#!/bin/bash

# Check for correct number of command line arguments
if [ $# -ne 2 ]; then
    echo "data file or output file not found"
    exit 1
fi

input_file="$1"
output_file="$2"

# Check if input file exists
if [ ! -f "$input_file" ]; then
    echo "<$input_file> not found"
    exit 1
fi

# Initialize an array to store column sums
declare -a col_sums

# Clear the contents of the output file
> "$output_file"

# Read the file line by line
while IFS= read -r line; do
    # Replace delimiters with a common delimiter (comma) for consistency
    line=$(echo "$line" | tr ';:' ',')

    # Split the line into fields based on the delimiter
    IFS=',' read -ra fields <<< "$line"

    # Iterate through each field and add to the corresponding column sum
    for i in "${!fields[@]}"; do
        col_sums[$i]=$((${col_sums[$i]} + ${fields[$i]}))
    done
done < "$input_file"

# Write the column sums to the output file
for i in "${!col_sums[@]}"; do
    echo "Col $((i + 1)) : ${col_sums[$i]}" >> "$output_file"
done
