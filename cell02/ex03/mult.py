#!/usr/bin/env python3

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
num = x*y
print(x,"x",y,"=",num)
if num>0:
    print( "The result is positive.")
elif num<0 :
    print("The result is negative.")
else:
    print("The result is positive and negative.")