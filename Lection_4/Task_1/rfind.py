# Program for finding files
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--folder', required=True)
parser.add_argument('--file', required=True)

args = parser.parse_args()


def FindFiles(path, name):
    try:
        global_path = os.listdir(path)
    except FileNotFoundError:
        return 'Error: name file not found!'
    for files in global_path:  # Recursive method
        if files.find(f'{name}') != -1:
            full_path = os.path.abspath(f'{path}')
            print(f'File: {files}', f'Path: {full_path}', sep='\n')
            print()
        if os.path.isdir(f'{path}\\{files}'):
            FindFiles(f'{path}\\{files}', name)
    return ''


print(FindFiles(args.folder, args.file))
