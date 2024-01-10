import os
from os import listdir
from os.path import isfile, join
import sys
import json

def read_file(file_path, charset="utf-8"):
    """ read a file and return liens """
    
    with open(file_path, encoding=charset) as fin:
        lines = []
        for line in fin.readlines():
            lines.append(line.replace("\r\n", "\n"))
        return lines

def read_json(json_path_arg):
    if json_path_arg == "":
        print("The json path is empty.")
        return
    with open(json_path_arg, 'r',encoding="utf-8") as f:
        config = json.load(f)
        return config

def get_filenames(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    for filename in onlyfiles:
        print(filename)

def get_filenames_recursively(dir_path):
    file_list = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def get_dirpath_containing_file_being_interpreted():
    path = os.path.dirname(os.path.realpath(__file__))
    return path

def path_join(directory, *items):
    joinned_path = directory
    for item in items: joinned_path = os.path.join(joinned_path, item)
    return joinned_path

def append_path_to_current_dir(*items):
    return path_join(get_current_dir(), *items)

def get_current_dir():
    return sys.path[0]