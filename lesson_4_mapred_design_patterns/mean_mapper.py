#!/usr/bin/python2

import sys
import csv
from datetime import datetime

reader=csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    #discern weekday and sale price of current line
    weekday=datetime.strptime(line[0], '%Y-%m-%d').weekday(); sale=line[4];
    #print to stdout as tab separated key   value pair
    print '%s\t%s'%(weekday,sale)