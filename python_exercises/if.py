#!/bin/usr/env python3

ask = int(input('What is you number?'))
if ask < 1 or ask > 10:
	print('invalid number')

password = input('What is your password?')
if '\n' in password or '\t' in password or ' ' in password:
	print('Please input your password correctly.')