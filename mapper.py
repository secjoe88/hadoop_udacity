#/usr/bin/python2
def mapper():
    for line in sys.stdin:
        data=line.strip().split("\t")
        date, time, city, product_category, cost, payment_method =data
        print "{0}\t{1}".format(product_category, cost)
