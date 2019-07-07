#!/bin/usr/python3

with open('test-file.txt', 'w') as f:
    f.write('first line\nsecond line\nthrid line\n')

with open('test-file.txt','r') as f:
	lines = f.readlines()
	i = 1
	for line in lines:
			print(f'line {i}: {line}')
			i += 1
#涉及到递进的编号，就要想到i = i + 1, 且是放在最后的部分执行的。
#否则就会重复执行。

	