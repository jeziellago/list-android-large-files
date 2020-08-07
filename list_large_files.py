#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author Jeziel Lago (https://github/com/jeziellago)

How it works:

$ python list_largest_files.py --help

'''

import os
import sys
from argparse import ArgumentParser

files_count={}

def walk(ROOT):
    if os.path.isfile(ROOT):
        if "build" not in ROOT and (ROOT.endswith(".java") or ROOT.endswith(".kt")):
            count = 1
            for _ in open(ROOT, "r"): 
                count += 1
            files_count[ROOT.split("/")[-1]] = count
    else:
        dirs = os.listdir(ROOT)
        for d in dirs:
            path = os.path.join(ROOT, d)
            walk(path)

def print_results(limit, output_file, include_test):
    sorted_files = sorted(files_count.items(), key=lambda x: x[1], reverse=True)

    check_test_file = lambda filename: not "Test" in filename  if not include_test else True

    def print_line(position, count, filename, output_file=None):
        if output_file: output_file.write("{},{},{}\n".format(position,count,filename))
        else: print("[{}º]> {} lines - {}".format(position,count,filename))

    csv_file = None
    if output_file:
        csv_file = open(output_file + ".csv", "w")
        csv_file.write("Position,Lines,File\n")

    index = 1
    for fl in sorted_files:
        if fl[1] >= limit and check_test_file(fl[0]):
            print_line(index, fl[1],fl[0], csv_file)
            index += 1

def main(args):
    project = args.project
    limit = args.limit
    include_test = args.include_test
    output_file = args.output

    walk(project)
    print_results(limit, output_file, include_test)

if __name__ == '__main__':
    parser = ArgumentParser(description="Show the largest files in Android project")

    parser.add_argument('--project', help='Project dir')
    parser.add_argument('--limit', help='Lines count limit', default=300)
    parser.add_argument('--include_test', help='Include test files')
    parser.add_argument('--output', help='File to save the results')
    
    args = parser.parse_args()
    main(args)
