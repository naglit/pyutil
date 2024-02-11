import sys, os
from os import listdir
from os.path import isfile, join
import pyutil.util.log_util as log

def write_file(file_name: str, lines: list[str], charset="utf-8"):
    """ write lines into a file """
    file_path = file_name
    data = "".join(lines)
    if "-d" in sys.argv:
        log.write_log("\nDEBUG MODE:")
        log.write_log(data)
        return

    with open(file_path, "w", encoding=charset) as fout:
        fout.write(data)

def make_dir(dir_path):
    if "-d" not in sys.argv:
        if not os.path.isdir(dir_path): os.makedirs(dir_path)
    else:
        log.write_log("\nDEBUG MODE:")
        log.write_log(dir_path)