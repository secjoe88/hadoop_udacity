#!/usr/bin/python2

import sys
import csv
import re

reader=csv.reader(sys.stdin, delimiter='\t', )
writer=csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
pattern=re.compile('\W+')
#skip first row, since it only defines column fields
reader.next()

for line in reader:
    #store row id
    current_id=line[0]
    #split the body column into individual words
    split_line=pattern.split(re.sub('<.+?>', ' ', line[4].replace('\n', ' ').strip()))
    split_line=[word.lower() for word in split_line if word !='']
    #print to stdout
    for word in split_line: print "{0}\t{1}".format(word,current_id)
