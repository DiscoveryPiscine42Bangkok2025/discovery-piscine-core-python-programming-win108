#!/usr/bin/env python3

import sys
import re

if len(sys.argv)!= 3:
    print("none")
else:
    scan = sys.argv[1]
    word = sys.argv[2]

    res = re.findall(scan, word)

    if scan != "" and len(res) > 0:
        print(len(res))
    else:
        print("none")