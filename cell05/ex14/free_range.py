#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv)!=3:
        print("none")
    else:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        
        result = list(range(x, y + 1))
        print(result)
            

main()