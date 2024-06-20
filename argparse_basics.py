import argparse
import sys

parser = argparse.ArgumentParser(description='process some integers.')

import argparse
import sys
import sort
import remove_duplicate
...
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-f', '--file', help="csv file to read from", dest="input_filename")
parser.add_argument('-o', '--output', help="csv file to write to", dest="output_filename")
parser.add_argument('-c', '--columns', help="columns to do action on", dest="column")
parser.add_argument('-a', '--action', help="action to run", dest="action")
args = parser.parse_args()
# Basic error handling of the options provided
if args.input_filename is None:
    sys.exit('Error! No file name provided.')
if args.action is None:
    sys.exit('Error! No action provided.')
if args.action == "sort":
    sort.sort_file(args.input_filename, args.output_filename, args.column)
if args.action == "remove_duplicate":
    remove_duplicate.remove_duplicate(args.input_filename, args.output_filename, args.column)

sorted()