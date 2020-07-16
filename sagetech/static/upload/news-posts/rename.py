#!/usr/bin/python

import os

files = os.listdir()


for file in files:
    file_split = file.split('.')
    if file.split('.')[1] == 'jpg':
        file_split[1] =  'png'
        file_renamed = '.'.join(file_split)
        print(file_renamed)
        os.rename(file, file_renamed)
        
        
