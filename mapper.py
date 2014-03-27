        #!/usr/bin/python2

## Mapper for mapreduce jobs on countrywide purchase data
import sys
import argparse

parser=argparse.ArgumentParser(usage='%(prog)s [option1] [option2]')
parser.add_argument("-d", "--date", help="Return the date as part of the Key/Value pair")
parser.add_argument("-t", "--time", help="Return the time as part of the Key/Value pair")
parser.add_argument("-c", "--city", help="Return the city as part of the Key/Value pair")
parser.add_argument("-p", "--product", help="Return the product_category as part of the Key/Value pair")
parser.add_argument("-s", "--cost", help="Return the cost as part of the Key/Value pair")
parser.add_argument("-m", "--method", help="Return the payment method as part of the Key/Value pair")
args=parser.parse_args()
if len(args)!=2:
        parser.print_help()
        exit

returnValues=['', '']
for line in sys.stdin:

        ## Read line from stdin and parse 
        data = line.strip().split('\t')
        [date, time, city, product_category, cost, payment_method] = data

        ##Discern desired Key for Key/Value pair
        if args[0]=="-d" or args[0]=="--date":
                returnValues[0]=date
        elif args[0]=="-t" or args[0]=="--time":
                returnValues[0]=time
        elif args[0]=="-c" or args[0]=="--city":
                returnValues[0]=city
        elif args[0]=="-p" or args[0]=="--product":
                returnValues[0]=product_category
        elif args[0]=="-s" or args[0]=="--cost":
                returnValues[0]=cost
        elif args[0]=="-m" or args[0]=="--method":
                returnValues[0]=payment_method
        ## Discern value for Key/Value pair
        if args[0]=="-d" or args[0]=="--date":
                returnValues[1]=date
        elif args[0]=="-t" or args[0]=="--time":
                returnValues[1]=time
        elif args[0]=="-c" or args[0]=="--city":
                returnValues[1]=city
        elif args[0]=="-p" or args[0]=="--product":
                returnValues[1]=product_category
        elif args[0]=="-s" or args[0]=="--cost":
                returnValues[1]=cost
        elif args[0]=="-m" or args[0]=="--method":
                returnValues[1]=payment_method

        
        print("{0}\t{1}".format(returnValues))
