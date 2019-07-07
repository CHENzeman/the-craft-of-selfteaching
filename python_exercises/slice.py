#!/bin/usr/env python3

text = 'Hello, world'
slice = text[7:12]
print(slice)
s = text[1:3]
print(s)  #不包括3，只有1-2

#可以用到split()
s = text.split(" ")
print(s[1])
x = text.split()
print(x[1])
