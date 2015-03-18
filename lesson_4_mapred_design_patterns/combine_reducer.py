#!/usr/bin/python2
import csv
import sys

reader=csv.reader(sys.stdin, delimiter='\t')
writer=csv.writer(sys.stdout, delimiter='\t', quoting=csv.QUOTE_ALL)
additional_info=''
for line in reader:
    
    if line[1]=='a': #if line is a user identifier
        #store pertinent fields for current user [reputation, gold, silver, bronze]
        additional_info=line[2:]
    else: #presumably, line is a post attributed to the currently stored user info
        #fist we extract the pertinent post info in the correct order
        post_info=[line[i] for i in [2,3,4,0,5,6,7,8,9]]
        writer.writerow(post_info+additional_info)