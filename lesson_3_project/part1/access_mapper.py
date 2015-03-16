#!/usr/bin/python2

##Mapper for MapReduce jobs on webserver access log data

import sys
import argparse
import re

parser=argparse.ArgumentParser(usage='%(prog)s [option1] [option2]', description='Returns the Key/Value pairs specified by [option1] [option2]')
parser.add_argument("-ip", help="Return the  client's ip address as part of the Key/Value pair", action="store_true")
parser.add_argument("-id", help="Return the client's identity as part of the Key/Value pair", action="store_true")
parser.add_argument("-u", help="Return the client's username as part of the Key/Value pair", action="store_true")
parser.add_argument("-t", help="Return the request's finish date/time as part of the Key/Value pair", action="store_true")
parser.add_argument("-q", help="Return the request's query string as part of the Key/Value pair", action="store_true")
parser.add_argument("-c", help="Return the status code of the request as part of the Key/Value pair", action="store_true")
parser.add_argument("-s", help="Return the requested object's size as part of the Key/Value pair", action="store_true")
parser.add_argument("-1", help="Return the integer 1 as part of the Key/Value pair (must be second option)", action="store_true")
##mapper accepts exactly two parameters
if len(sys.argv)!=3:
        parser.print_help()
        sys.exit()
returnValues=['', '']

pattern=re.compile("( |\[.+\]|\".+\")")

for line in sys.stdin:
        data=[]

        ## Read line from stdin and parse
        
        tmp=re.split(pattern, line.strip())
        for l in tmp:
                if l !="" and l!=" ":
                        data.append(l)

        if len(data)==7:
                [ip, identity, username, time, query, status, size] = data
        else:
                print "error\t1"
        
        ##Discern desired Key for Key/Value pair
        if sys.argv[1]=="-ip":
                returnValues[0]=ip
        elif sys.argv[1]=="-id":
                returnValues[0]=identity
        elif sys.argv[1]=="-u":
                returnValues[0]=username
        elif sys.argv[1]=="-t":
                returnValues[0]=time
        elif sys.argv[1]=="-q":
                returnValues[0]=query
        elif sys.argv[1]=="-c":
                returnValues[0]=status
        elif sys.argv[1]=="-s":
                returnValues[0]=size
        else:
            parser.print_help()
            sys.exit()
                

        ## Discern desired Value for Key/Value pair
        if sys.argv[2]=="-ip":
                returnValues[1]=ip
        elif sys.argv[2]=="-id":
                returnValues[1]=identity
        elif sys.argv[2]=="-u":
                returnValues[1]=username
        elif sys.argv[2]=="-t":
                returnValues[1]=time
        elif sys.argv[2]=="-q":
                returnValues[1]=query
        elif sys.argv[2]=="-c":
                returnValues[1]=status
        elif sys.argv[2]=="-s":
                returnValues[1]=size
        elif sys.argv[2]=="-1":
                returnValues[1]="1"

        ##Print Key/Vlue
        print("{0}\t{1}".format(returnValues[0], returnValues[1]))

