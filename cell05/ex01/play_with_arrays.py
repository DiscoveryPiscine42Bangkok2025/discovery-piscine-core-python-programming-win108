#!/usr/bin/env python3

num =  "2 8 9 48 8 22 -12 2"
array = list(map(int, num.split()))
print("Original array:",array)
for i in range(len(array)):
    array[i] += 2
print("New array:",array)