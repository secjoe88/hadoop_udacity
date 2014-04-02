#!/usr/bin/python2

##Mapper that returns a key for each file that is accessed in a webserver log in the form of
## <path_to_file, 1>

import sys
import re

pattern=re.compile("(/(.+))*/(.+)\.(.+) ")

##Parse inputed lines using regex
for line in sys.stdin:
    query=re.search("\".+\"", line)
    ##check if line matches regex
    match=pattern.search(query.string[query.start():query.end()])
    ##If so print the portion of the line that matches the regex
    if match:
        print "{0}\t1".format(match.string[match.start():match.end()])
