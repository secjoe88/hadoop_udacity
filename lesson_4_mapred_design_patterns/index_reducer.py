#!/usr/bin/python2

import sys


prevkey='';curkey='';instances=0;posts=[]
for line in sys.stdin:
    curkey,id=line.split('\t');id=int(id);
    if not instances: prevkey=curkey
    
    if curkey==prevkey: #if key on current line is the same as key on previous line
        #increment instance counter
        instances+=1;
        #and track current post id if it isn't already in the list for this key
        if id not in posts: posts.append(id)
        
    else: #if key on current line is different from previous line
        #print index entry for key on previous line
        print "%(key)s(%(instances)d)  %(posts)s"%{
        'key':prevkey,
        'instances':instances,
        'posts':str(sorted(posts))[1:-1]
        }
        #reset instance counter to 1
        instances=1
        #reset post id list to only include current id
        posts=[id]
    #set previous key to current key
    prevkey=curkey
    