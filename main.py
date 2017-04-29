import csv
import os
import sys
import time
from platform import system, python_version, platform


def check_python_version():
    x = python_version()
    if not x.__contains__('2.'):
        sys.stderr.write('Please consider using a python version 2 for this project')

    else:
        sys.stdout.write("Pass, The system is using python 2")
        time.sleep(2)
        check_system()


def check_system():
    x = system()
    if x is not 'Windows':
        sys.stderr.write('Please use a Windows based machine')
        sys.exit(0)
    else:
        sys.stderr.write('Pass, system is running on Windows')
        time.sleep(2)
        get_details()


def get_details():
    import subprocess as sp
    os.system('echo list volume > command.txt')
    path = os.path.join(os.getcwd(),"command.txt")
    command = ("diskpart" + path) 
    with open('output.txt', 'a') as outfile:
        sp.call(command, stdout=outfile)
   


def main():
    return check_python_version()


if __name__ == '__main__':
    main()
