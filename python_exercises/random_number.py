# !/bin/usr/env python3

import random
x = random.random()
print(x)

a_list = [random.randrange(1,100) for i in range(3)]
print(f'a_list comprehends {len(a_list)} random numbers: {a_list}')

b_list = [random.randrange(1,150) for i in range(100)]
print(f'b_list comprehends {len(b_list)} random numbers: {b_list}')
