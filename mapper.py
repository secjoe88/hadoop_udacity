#!/usr/bin/python2

## Mapper for mapreduce jobs on countrywide purchase data
import sys
import argparse

parser=argparse.ArgumentParser(usage='%(prog)s [option1] [option2]', description='Returns the Key/Value pairs specified by [option1] [option2]')
parser.add_argument("-d", "--date", help="Return the date as part of the Key/Value pair", action="store_true")
parser.add_argument("-t", "--time", help="Return the time as part of the Key/Value pair", action="store_true")
parser.add_argument("-c", "--city", help="Return the city as part of the Key/Value pair", action="store_true")
parser.add_argument("-p", "--product", help="Return the product_category as part of the Key/Value pair", action="store_true")
parser.add_argument("-s", "--cost", help="Return the cost as part of the Key/Value pair", action="store_true")
parser.add_argument("-m", "--method", help="Return the payment method as part of the Key/Value pair", action="store_true")
##mapper accepts exactly two parameters
if len(sys.argv)!=3:
        parser.print_help()
        sys.exit()
returnValues=['', '']
for line in sys.stdin:

        ## Read line from stdin and parse 
        data = line.strip().split('\t')
        [date, time, city, product_category, cost, payment_method] = data
        
        ##Discern desired Key for Key/Value pair
        if sys.argv[1]=="-d" or sys.argv[1]=="--date":
                returnValues[0]=date
        elif sys.argv[1]=="-t" or sys.argv[1]=="--time":
                returnValues[0]=time
        elif sys.argv[1]=="-c" or sys.argv[1]=="--city":
                returnValues[0]=city
        elif sys.argv[1]=="-p" or sys.argv[1]=="--product":
                returnValues[0]=product_category
        elif sys.argv[1]=="-s" or sys.argv[1]=="--cost":
                returnValues[0]=cost
        elif sys.argv[1]=="-m" or sys.argv[1]=="--method":
                returnValues[0]=payment_method

        ## Discern desired Value for Key/Value pair
        if sys.argv[2]=="-d" or sys.argv[2]=="--date":
                returnValues[1]=date
        elif sys.argv[2]=="-t" or sys.argv[2]=="--time":
                returnValues[1]=time
        elif sys.argv[2]=="-c" or sys.argv[2]=="--city":
                returnValues[1]=city
        elif sys.argv[2]=="-p" or sys.argv[2]=="--product":
                returnValues[1]=product_category
        elif sys.argv[2]=="-s" or sys.argv[2]=="--cost":
                returnValues[1]=cost
        elif sys.argv[2]=="-m" or sys.argv[2]=="--method":
                returnValues[1]=payment_method

        ##Print Key/Vlue
        print("{0}\t{1}".format(returnValues[0], returnValues[1]))
