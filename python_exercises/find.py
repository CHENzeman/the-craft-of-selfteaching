#!/bin/usr/env python3

s = 'The lantern is really awful. Damn damn it! I will never use it after expiry.'
index = s.find('damn')
print(index)

x = s.find('it')
print(x)

age = int(input('Please tell me your age:'))
if age < 18:
	question = input('Do you wanna drink an ice beer?')
	if question == 'yes':
		print('No way. Get out of here.')
	if question == 'Yes':
		print('No way. Get out of here.')
	else:
		print('Good kid! Byebye.')
else:
	print('Help yourself please.')

