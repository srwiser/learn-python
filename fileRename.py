import sys
import os
import argparse

def renameFile(path, find_string, replace_string):
    counter_names = 0
    if not os.path.exists(path):
        print('Path does not exist')
        return False
    for dirpath, dirs, files in os.walk(path):
        for filename in files:
            if find_string in filename:
                os.rename(
                    os.path.join(dirpath, filename),
                    os.path.join(dirpath, filename.replace(find_string, replace_string))
                )
                counter_names += 1
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", help="path")
    parser.add_argument("-f", help="find_string")
    parser.add_argument("-r", help="replace_string")
    args = parser.parse_args()
    if len(sys.argv) != 7:
        print("\nUsage: python fileRename.py -p <path> -f <find_string> -r <replace_string>\n")
    else:
        # Reading arguments
        directory = sys.argv[2]
        find_string = sys.argv[4]
        replace_string = sys.argv[6]
        try:
            renameFile(directory,find_string,replace_string)
        except Exception as e: print(e)