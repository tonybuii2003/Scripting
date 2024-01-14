#!/bin/bash

copy_c_files() {
    local src="$1"
    local dest="$2"

    find "$src" -type f -name '*.c' -print0 | while IFS= read -r -d '' file; do
        # Construct the destination path
        local dest_path="$dest/${file#$src/}"
        local dest_dir=$(dirname "$dest_path")
        
        mkdir -p "$dest_dir"
        
        cp "$file" "$dest_path"
    done
}

interactive_copy() {
    local src="$1"
    local dest="$2"
    local c_file_count
    
    c_file_count=$(find "$src" -maxdepth 1 -type f -name '*.c' | wc -l)
    
    if [ "$c_file_count" -gt 3 ]; then
        echo "The directory '$src' contains more than 3 C files."
        read -p "Do you want to move these files? (y/n): " -n 1 -r
        echo    # Move to a new line
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            copy_c_files "$src" "$dest"
        fi
    else
        copy_c_files "$src" "$dest"
    fi
}

# Main
if [ $# -ne 2 ]; then
    echo "src and dest dirs missing"
    exit 1
fi

src_dir=$1
dest_dir=$2

if [ ! -d "$src_dir" ]; then
    echo "<src-dir> not found"
    exit 0
fi

if [[ $src_dir == $dest_dir* ]]; then
    echo "Destination directory cannot be a subdirectory of the source directory."
    exit 1
fi

if [ ! -d "$dest_dir" ]; then
    mkdir -p "$dest_dir"
fi
export -f copy_c_files
export -f interactive_copy
find "$src_dir" -type d -exec bash -c 'interactive_copy "$0" "$1"' {} "$dest_dir" \;
