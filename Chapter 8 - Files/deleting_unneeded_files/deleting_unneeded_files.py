# deleting_unneeded_files.py Searches for any file bigger than 100MB and displays the location in the console.

import os

def deleting_unneeded_files(folder):
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if (os.path.getsize('{}\\{}'.format(foldername, filename)) * 0.000001) > 100:
                print(os.path.join(foldername, filename))

deleting_unneeded_files('.')