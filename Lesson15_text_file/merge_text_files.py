import glob
import os
import sys

# This script merges all .txt files from the 'text_files' directory into a single file named 'merged_file.txt'.
#started out with the coding from the lesson but made some changes to improve cross-platform compatibility and error handling using Copilot when it didn't work as expected

# Build a platform-independent pattern for text files inside the 'text_files' directory
base_dir = os.path.dirname(os.path.abspath(__file__))
pattern = os.path.join(base_dir, 'text_files', '*.txt')

# Use glob to find all files matching the pattern, and sort them alphabetically
filepaths = sorted(glob.glob(pattern))

if not filepaths:
    print("No .txt files found in 'text_files' directory.")
    sys.exit(0)

# Write merged output next to this script
merged_path = os.path.join(base_dir, 'merged_file.txt')

try:
    # Open the new file in write mode with explicit encoding
    with open(merged_path, 'w', encoding='utf-8', newline='\n') as merged_file:
        for idx, file_path in enumerate(filepaths):
            # Open and read the file's content with a fallback for encoding errors
            with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                merged_file.write(f.read())
            # Add a single newline between files (but not after the last file)
            if idx != len(filepaths) - 1:
                merged_file.write("\n")
except OSError as e:
    print(f"Error writing merged file: {e}")
    sys.exit(1)