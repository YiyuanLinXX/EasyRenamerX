import os
import re
import shutil
import argparse

def title_except_prepositions(name, prepositions):
    # Split the name into words, using underscore as delimiter while keeping it
    words = re.split('(_)', name)
    new_words = []
    for word in words:
        # Keep prepositions as is, capitalize other words
        if word.lower() in prepositions:
            new_words.append(word)
        else:
            new_words.append(word.capitalize())
    return ''.join(new_words)

def rename_files_and_folders(root_dir):
    # Define a set of common prepositions
    prepositions = {'in', 'on', 'at', 'since', 'for', 'ago', 'before', 'to', 'past', 'till', 'until', 'by', 'under', 'below', 'over', 'above', 'across', 'through', 'into', 'towards', 'onto', 'from', 'of', 'off', 'about'}
    
    # Lists to store paths for renaming later
    files_to_rename = []
    dirs_to_rename = []

    # First, collect all file and directory paths
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        # Collect files for renaming
        for filename in filenames:
            original_file_path = os.path.join(dirpath, filename)
            new_name = filename.replace(' ', '_')
            new_name = title_except_prepositions(new_name, prepositions)
            new_file_path = os.path.join(dirpath, new_name)
            files_to_rename.append((original_file_path, new_file_path))
        
        # Collect directories for renaming
        if dirpath != root_dir:  # Skip the root directory itself
            new_dirname = os.path.basename(dirpath).replace(' ', '_')
            new_dirname = title_except_prepositions(new_dirname, prepositions)
            new_dirpath = os.path.join(os.path.dirname(dirpath), new_dirname)
            dirs_to_rename.append((dirpath, new_dirpath))

    # Rename files
    for original_path, new_path in files_to_rename:
        shutil.move(original_path, new_path)
        print(f"Renamed file: {original_path} -> {new_path}")

    # Rename directories from bottom to top
    for original_path, new_path in reversed(dirs_to_rename):
        shutil.move(original_path, new_path)
        print(f"Renamed folder: {original_path} -> {new_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename files and folders: replace spaces with underscores and capitalize titles except for prepositions.")
    parser.add_argument('--root_dir', type=str, default=os.path.dirname(os.path.abspath(__file__)), help="The root directory to process. Defaults to the script's directory if not specified.")

    args = parser.parse_args()

    print(f"Starting to rename files and folders in: {args.root_dir}")
    rename_files_and_folders(args.root_dir)
    print("Finished renaming.")
