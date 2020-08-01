# Get latest log file
import glob
import pathlib
from os import environ
from os.path import join, getmtime

default_path = join(environ['USERPROFILE'], "Saved Games\Frontier Developments\Elite Dangerous")


def get_latest_journal_path(path_to_search=default_path):
    """Returns the full path of the latest elite journal log file from specified path"""
    path_to_search = pathlib.Path(path_to_search)
    list_of_files = glob.glob(str(path_to_search) + '\Journal.*.log')
    latest_file = max(list_of_files, key=getmtime)
    return latest_file


if __name__ == '__main__':
    print(get_latest_journal_path())
