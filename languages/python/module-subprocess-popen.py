#!/usr/bin/python3

# subprocess example with output and return code

import subprocess
import sys

try:
    p = subprocess.Popen(['/bin/ls', '-l', '-h'], stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    print(out.decode('UTF-8'))
    if p.returncode != 0:
        print(err)
        sys.exit(1)
except subprocess.SubprocessError as e:
    print(e)
    sys.exit(1)
