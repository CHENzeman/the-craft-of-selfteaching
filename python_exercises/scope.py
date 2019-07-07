#!/bin/usr/env python3

balance = 0
def reduce_amount(x):
	global balance  #要写global balance
	balance -= x
	return balance

def multiple_func(n):
	x = n * n
	return x

print(reduce_amount(12))
print(multiple_func(4))