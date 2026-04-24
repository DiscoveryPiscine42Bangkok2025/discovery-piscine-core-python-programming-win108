#!/usr/bin/env python3

num = float(input("Give me a number: "))
if num%1 != 0:
    num = (num//1)+1
    print(int(num))
else:
    print(int(num))