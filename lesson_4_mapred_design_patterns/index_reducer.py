#!/usr/bin/python2

import sys

index={}
for line in sys.stdin:
    key,id=line.split('\t');id=int(id);
    
    if key not in index:
        #if the current word isn't in the index yet, add it to the index, note that there is now 1 instance of it
        #and note the post id that this instance takes place in
        index[key]={}; index[key]['instances']=1; index[key]['posts']=[id]
    else:
        #if current word already exist in the index, increment the number of instances of the word
        index[key]['instances']+=1
        if id not in index[key]['posts']:
            #and if the post id of this instance of word isn't in the post id list of this word in the index, add the 
            #current post id to this word's index entry
            index[key]['posts'].append(id)
            
for key in index:
    #print index entries
    print "%(key)s(%(instances)d)  %(posts)s"%{
        'key':key,
        'instances':index[key]['instances'],
        'posts':str(sorted(index[key]['posts']))[1:-1]
        }
    
    