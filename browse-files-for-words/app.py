import os
import re

def is_git_directory(path):
    return '.git' in path.split(os.path.sep)

def search_files(directory, search_word, output_file):
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for root, dirs, files in os.walk(directory):
            # Remove .git directories from the dirs list to prevent descending into them
            dirs[:] = [d for d in dirs if d != '.git']
            
            for file in files:
                file_path = os.path.join(root, file)
                # Skip files in .git directories
                if is_git_directory(file_path):
                    continue
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        matches = len(re.findall(r'\b' + re.escape(search_word) + r'\b', content, re.IGNORECASE))
                        if matches > 0:
                            out_file.write(f"{file_path}-{matches}\n")
                except Exception as e:
                    print(f"Error reading file {file_path}: {str(e)}")

# Get user input
directory = input("Enter the directory path to search: ")
search_word = input("Enter the word to search for: ")
output_file = input("Enter the name of the output file: ")

# Run the search
search_files(directory, search_word, output_file)

print(f"Search complete. Results written to {output_file}")
