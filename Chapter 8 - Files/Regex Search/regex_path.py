import os, re

files = os.listdir('./to_search')

for file in files:
    print(file)
    file_to_check = open('./to_search/{}'.format(file))
    file_splited = file_to_check.readlines()
    for line in file_splited:
        if re.search(r'\W*(for)\W*', line) != None:
            print(line)
    file_to_check.close()