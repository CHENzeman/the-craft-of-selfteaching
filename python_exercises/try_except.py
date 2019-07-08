#!/bin/usr/env python3

try:
	x = int(input('Enter number: '))
	x = x + 1
	print(x)
except:
	print('Invalid input')
finally:
	print('Valid input.')
