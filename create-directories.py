import os
import shutil
import string
import sys
import os.path
from pathlib import Path

#when inputting make sure file path destination is 100% correct

current_path = os.path.dirname(os.path.abspath(__file__))
path_destination = current_path + '/output/'
path_metadata_file = current_path + '/list-of-directories.csv'

#for creating folders
with open(path_metadata_file) as x:
    for line in x.readlines()[1:]: #ignores the first line:
        line = line.split(',')
        main_folder = line[0]
        sub_folder = line[1].replace("\n", "")
        os.chdir('' + path_destination + '')
        path = Path(path_destination + main_folder + '/')
        if path.is_dir():
            pass
        else:
            os.mkdir('' + main_folder + '/')

#for creating subfolders
with open(path_metadata_file) as x:
    for line in x.readlines()[1:]: #ignores the first line:
        line = line.split(',')
        main_folder = line[0]
        sub_folder = line[1].replace("\n", "")
        os.chdir('' + path_destination + '' + main_folder + '/')
        os.mkdir('' + sub_folder + '')
        os.chdir('' + path_destination + '' + main_folder + '/' + sub_folder + '/')
        os.mkdir('subfolder_3_a/')
        os.mkdir('subfolder_3_b/')
        os.mkdir('subfolder_3_c/')
        os.mkdir('subfolder_3_d/')
        os.mkdir('subfolder_3_e/')
        os.mkdir('subfolder_3_f/')

