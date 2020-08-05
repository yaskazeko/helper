#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys

if __name__ == "__main__":
   dir = sys.argv[1] 
print (dir)

listFiles = os.listdir(dir)

for f in listFiles:
    print(f, os.stat(f).st_mtime)
    
