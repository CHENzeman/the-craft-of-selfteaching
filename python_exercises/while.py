#!/bin/usr/env python3

#1.
clist = ['Canada', 'USA', 'Mexico']
size = len(clist)
i = 0

while i < size:
	print(clist[i])
	i = i + 1

#3.sums for numbers from 100-200:
n = 101
while n < 201:
	s = 100*(n-99) + 0.5*(n-99)*(n-100)
	print(f'The sum for numbers from 100 to {n} is: {s}')
	n = n + 1
