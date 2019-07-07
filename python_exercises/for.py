#!/bin/usr/env python3

#1.
clist = ['Canada','USA','Mexico','Australia']
print('The list of foreign cities:')
for c in clist:
	print('city:' + c)
	print('\n')

#3.
for n in range(1,10):
    for i in range(1,10):
        if n <= i:
            multiplication = n * i
            s = f"{n} * {i} = {multiplication}"
            print(s)

#4.
for i in range(1,12):
	if i > 1:
		i -= 1
		print(i)

#5.		
print('All even numbers within 0~10:')
for i in range(0,11):
	if not i % 2:
		print(i)

#6.
#总和：
a_list = list(range(100,201))
sum_of_a_list = sum(a_list)
print(sum_of_a_list)

#loop for sums:
for n in range(101,201):
	s = 100 *(n-99) + 0.5*(n-99)*(n-100)
	print(f'The sum of numbers from 100 to {n} is: {s}')
	
	
