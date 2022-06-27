import sys, os
from os import listdir
from os.path import isfile, join

def read_file(file_name, charset="utf-8"):
    """ read a file and return liens """
    
    with open(file_name, encoding=charset) as fin:
        lines = []
        for line in fin.readlines():
            lines.append(line.replace("\r\n", "\n"))
        return lines

def write_file(file_name, lines, charset="utf-8"):
    """ write lines into a file """

    file_path = file_name
    data = "".join(lines)
    if "-d" in sys.argv:
        print("\nDEBUG MODE:")
        print(data)
        return

    with open(file_path, "w", encoding=charset) as fout:
        print(f"Create {file_path}")        
        fout.write(data)

def make_dir(dir_path):
    if "-d" not in sys.argv:
        if not os.path.isdir(dir_path): os.makedirs(dir_path)
    else:
        print("\nDEBUG MODE:")
        print(dir_path)

def get_filenames(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    for filename in onlyfiles:
        print(filename)

def get_dirpath_containing_file_being_interpreted():
    path = os.path.dirname(os.path.realpath(__file__))
    return path