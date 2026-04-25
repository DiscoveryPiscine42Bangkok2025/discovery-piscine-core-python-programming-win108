#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv)!=2:
        print("none")
    else:
        word = sys.argv[1]
        if 'z' not in word:
            print("none")
        else:
            for i in word:
                if i == 'z':
                    print("z", end="")
        
            print()

main()