import os
import sys
import shutil
import ast

def generate_text_files(basedir):
    files = os.listdir(basedir)
    f = open('distribution.txt', 'a+')
    for fl in sorted(files):
        f.write('/home/jax/final_data/datas/' + fl + '\n')

    f.close()

if __name__ == '__main__':
    arguments = sys.argv[1:]

    if(len(arguments) > 1):
        raise IOError("Arguments must not be greater than %d" % 1)
    generate_text_files(arguments[0])
