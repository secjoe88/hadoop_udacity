#!/usr/bin/python2

##Mapper that searches for a string amongst data

import sys
import argparse
import re

parser=argparse.ArgumentParser(usage='%(prog)s string', description='Prints Key/Value pair <string, 1>')
parser.add_argument("string", help="String to match")

if len(sys.argv)!=2:
    parser.print_help()
    sys.exit()
else:
    argString=sys.argv[1]


for line in sys.stdin:
    if re.search(argString, line):
        print "{0}\t1".format(argString)
