# selective_copy.py Searches for any pdf and jpg files inside given directory and copy them into the output_files folder.

import os, shutil

def selective_copy(folder):
    for folder_name, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith('.pdf') or filename.endswith('.jpg'):
                print(os.path.join(folder_name, filename))
                print(os.path.abspath('.\output_files'))
                shutil.copy(os.path.join(folder_name, filename), os.path.abspath('.\output_files'))

folder = os.path.abspath('.')
selective_copy(folder)
