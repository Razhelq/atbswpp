# filling_in_the_gaps.py - fins all files with a given prefix and locates any gaps in the numbering.
# Insert gaps into numbered files so that the new file can be added.


import os, shutil, re

def filling_in_the_gaps(folder):

    for folder_name, subfolders, filenames in os.walk(folder):
        numbero = 1
        for filename in filenames:
            if filename.startswith('spam'):
                number = re.search(r'\d{3}', filename).group(0)
                if int(number) == numbero:
                    numbero += 1
                    continue
                else:
                    num = '0' * (3-len(str(int(number)))) + str(numbero)
                    numbero += 1

                    f = open('spam{}.txt'.format(num), 'w')
                    f.close()

filling_in_the_gaps('.')


# Script used to create example files for tests.
# for i in range(1, 50):
#     if i in (3, 6, 15, 27, 32, 41):
#         continue
#     elif i < 10:
#         f = open('spam00{}.txt'.format(i), 'w')
#     else:
#         f = open('spam0{}.txt'.format(i), 'w+')
#     f.close()