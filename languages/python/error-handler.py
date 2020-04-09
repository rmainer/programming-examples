#!/usr/bin/python3

# an error handler which prints the file and line where the error occurred

import os.path
import sys

def error_handler(e):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    if exc_tb is not None:
        fn = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("{}: {} ({}:{})".format(exc_type.__name__, e, fn, exc_tb.tb_lineno))
    else:
        print(e)


error_handler('custom error message')

try:
    a = [1, 2]
    print(a[3])
except IndexError as e:
    error_handler(e)
    sys.exit(1)
