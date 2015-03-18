#!/usr/bin/python2
import csv
import sys


reader=csv.reader(sys.stdin, delimiter='\t')


writer=csv.writer(sys.stdout, delimiter='\t', quoting=csv.QUOTE_ALL)

for line in reader:
    if len(line)==5: #user information line
        #store user information
        #with formatting key=[usr_ptr_id], value=[reputation, gold, silver, bronze]
        key,value=[line[0]],line[1:]
        #print user id, user keywork identifier (a), and remaining user information
        writer.writerow(key+['a']+value)
    else: #forum post information line
        #store desired data from forum post 
        #with format key=[author_id], value=[id, title, tagnames, node_type, parentid, abs_parent_id, added_at, score]
        key,value=[line[3]],[line[i] for i in [0,1,2,5,6,7,8,9]]
        #print out user id of poster, node keyword identifier (b), and forum post info as value
        #final format: 
        #   [author_id, b, id, title, tagnames, node_type, parentid, abs_parent_id, added_at, score]
        writer.writerow(key+['b']+value)

