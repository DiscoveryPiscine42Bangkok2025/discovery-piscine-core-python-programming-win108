#!/usr/bin/env python3

import sys

def downcase_it(a):
    return a.lower()



def main():
    if len(sys.argv) < 2:
        print("none")
        sys.exit()
    
    for i in range(len(sys.argv -1)):
        x = sys.argv[i+1]
        print(downcase_it(x))

main()