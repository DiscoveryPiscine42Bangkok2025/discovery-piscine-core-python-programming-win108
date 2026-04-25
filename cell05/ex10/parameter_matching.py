#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv)<1:
        print("none")
        exit()

    x = input("What was the parameter? ")
    if sys.argv[1]==x:
        print("Good job!")
    else:
        print("Nope, sorry...")

main()