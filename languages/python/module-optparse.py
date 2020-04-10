#!/usr/bin/python3

# optparse example, a replacement for getopt
# try: module-optparse -h

import optparse
import sys

p = optparse.OptionParser()
p.add_option('-f', '--file', dest='fn', help='destination filename', metavar='FILE')
p.add_option('-q', '--quite', action='store_false', dest='verbose', help='be quiet', default=True)
p.add_option('-s', '--show', action='store_true', dest='show', help='show something')

if len(sys.argv) < 2:
    p.print_help()
    sys.exit(0)

(options, args) = p.parse_args()
opts = vars(options)

print(opts['verbose'])
print(opts['fn'])