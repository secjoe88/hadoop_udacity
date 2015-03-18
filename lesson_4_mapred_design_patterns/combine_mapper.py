#!/usr/bin/python2
import csv
import sys


forum_node=open('c:\\users\\jojo\desktop\\nodes_short.tsv', 'r')
forum_users=open('c:\\users\\jojo\\desktop\\forum_users.tsv','r')

node_reader=csv.reader(forum_node, delimiter='\t')
users_reader=csv.reader(forum_users, delimiter='\t')
node_reader.next();users_reader.next()

writer=csv.writer(sys.stdout, delimiter='\t', quoting=csv.QUOTE_ALL)

for line in node_reader:
    #store desired data from forum post 
    #with format key=[author_id], value=[id, title, tagnames, node_type, parentid, abs_parent_id, added_at, score]
    key,value=[line[3]],[line[i] for i in [0,1,2,5,6,7,8,9]]
    #print out user id of poster, node keyword identifier (b), and forum post info as value
    #final format: 
    #   [author_id, b, id, title, tagnames, node_type, parentid, abs_parent_id, added_at, score]
    writer.writerow(key+['b']+value)

forum_node.close()


for line in users_reader:
    #store user information
    #with formatting key=[usr_ptr_id], value=[reputation, gold, silver, bronze]
    key,value=[line[0]],line[1:]
    #print user id, user keywork identifier (a), and remaining user information
    writer.writerow(key+['a']+value)
    
forum_users.close()