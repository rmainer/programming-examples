#!/usr/bin/python3

# example how to use configparser

import configparser
import sys

cfg = configparser.ConfigParser()
try:
    cfg.read('module-configparser.conf')
except configparser.Error as e:
    print(e)
    sys.exit(1)

if cfg.has_section('section1'):
    print('has section1 :)')

if not cfg.has_option('section1', 'option3'):
    print('no option3 in section 1 :(')

print(cfg['section2']['option3'])
