#!/usr/bin/python2

import csv
import sys


prevkey=None;totalsales=0.;count=0
weekdays={
    '0':'Monday',
    '1':'Tuesday',
    '2':'Wednesday',
    '3':'Thursday',
    '4':'Friday',
    '5':'Saturday',
    '6':'Sunday'
    }
    
reader=csv.reader(sys.stdin, delimiter='\t')
for line in reader:
    #read in key value pair from stdin
    curkey, cursale=line;
    cursale=float(cursale);
    prevkey=curkey if prevkey==None else prevkey
    if curkey==prevkey:
        #if key on current line is same as key on previous line (they are same day of the week)
        #add cursale to the total for the current day of the week and increment the number of sales
        #for that day of the week
        totalsales+=cursale
        count+=1
    else:
        #otherwise print mean sale for that weekday and reset totalsales and counter
        
        print '%s\t%.3f'%(weekdays[prevkey],totalsales/count)
        totalsales=cursale;
        count=1;
        
    
    prevkey=curkey
        
#print final solution
print '%s\t%.3f'%(weekdays[prevkey],totalsales/count)