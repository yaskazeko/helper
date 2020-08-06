#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
from pathlib import Path

if __name__ == "__main__":
    dir_in = sys.argv[1]
print("Search and delete unnecessary files in a directory " + dir_in)

listFiles = os.walk(dir_in)
# list files in dir with full path
path_ = []
# list files for find last ver
path_py = []
# list file for del
path_other = []
for top, dirs, files in listFiles:
    for i in files:
        path_.append(os.path.join(top, i))
for f in path_:
    if Path(f).suffix == '.py':
        path_py.append(f)
    else:
        path_other.append(f)
# create list of suffix for .gitignore
list_of_suffix = [".txt"]
for f in path_other:
    find_suf = 0
    for suf in list_of_suffix:
        if Path(f).suffix == suf:
            find_suf = 1
    if find_suf == 0:
        list_of_suffix.append(Path(f).suffix)
# create .gitignore
gitignore_file = open(dir_in + "/.gitignore", "w")
for f in list_of_suffix:
    gitignore_file.write("*" + f + '\n')
gitignore_file.close()

print(".gitignore created." + "\n")

max_write_time = 0
last_write = ""
for f in path_py:
    if os.path.getmtime(f) > max_write_time:
        max_write_time = os.path.getmtime(f)
        last_write = f

print("Last modified file:" + "\n" + last_write + "\n" + "********************")
# remove old ver files
for f in path_py:
    if f != last_write:
        os.remove(f)
        print("file: " + f + " was removed")

# remove other files
for f in path_other:
    os.remove(f)
    print("file: " + f + " was removed")
'''
for f in path_:
    print(f)

print("**************")
for f in path_py:
    print(f)
print("**************")
for f in path_other:
    print(f)

print("**************")
for f in list_of_suffix:
    print(f)
'''
