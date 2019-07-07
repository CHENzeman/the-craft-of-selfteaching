#!/bin/usr/env python3

x = [(3,6), (4,7), (5,9), (8,4), (3,1)]
x.sort(key=lambda pair:pair[0])
print(x)

x.sort(key=lambda pair:pair[1])
print(x)