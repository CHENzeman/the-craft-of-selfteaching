#!/bin/usr/env python3

a_list = list(range(1000))
n = max(a_list)
m = min(a_list)
print(f'the maximum number of a_list: {n}')
print(f'the minimum number of a_list: {m}')

even_number = [x for x in a_list if not x % 2]
odd_number = [x for x in a_list if x % 2]
print(f'A list of even numbers: {even_number}')
print()
print(f'A list of odd numbers: {odd_number}')
