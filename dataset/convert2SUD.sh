#!/bin/bash

# Create output directory if it doesn't exist
mkdir -p tagged-stanza/SUD/

# Process all .conllu files
for file in tagged-stanza/UD/*.conllu; do
    # Extract just the filename without path
    filename=$(basename "$file")
    
    # Create output filename with SUD_ prefix
    output_file="tagged-stanza/SUD/SUD_${filename}"
    
    # Run the grew transform command
    grew transform -grs ../tools/converter/grs/UD_to_SUD.grs -config sud -i "$file" -o "$output_file"
    
    echo "Processed: $file → $output_file"
done
