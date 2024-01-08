import sys, os
from os import listdir
from os.path import isfile, join

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