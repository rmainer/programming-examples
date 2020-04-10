#!/usr/bin/python3

# getopt example
# NOTE: after a non-option argument, all further arguments are considered also non-options!

import getopt
import sys

# args: -a -b -c 123
# opts: --clong=very --long arg
test = '-a -b -c 123 --clong=123 --long1 arg --long2'.split(' ')

try:
    opts, args = getopt.getopt(sys.argv[1:], 'abc:', ['clong=', 'long1=', 'long2'])
except getopt.GetoptError as e:
    print(e)
    sys.exit(1)

for o, a in opts:
    if o == '-a':
        print('a')
    elif o == '-b':
        print('b')
    elif o in ('-c', '--clong'):
        print(o, a)
    elif o == '--long1':
        print(o, a)
    elif o == '--long2':
        print('long2')
    else:
        assert False, "unhandled option"
