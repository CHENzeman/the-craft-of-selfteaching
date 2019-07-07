#!/bin/usr/env python3

for i in range(1,4):
	for n in range(1,4):
		print(f'({i},{n})')

persons = [ 'John', 'Marissa', 'Pete', 'Dayton' ]
people = persons
places = ['Mcdonald']
for i in persons:
	for n in people:
		for p in places:
			if i != n:
				print(f'{i} met {n} in {p}.')