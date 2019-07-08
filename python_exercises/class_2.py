#!/bin/usr/env python3

class Plane:
	def __init__(self):
		self.wings = 2
		self.drive()
		self.flaps()
		self.wheels()
		self.bugs = 0


	def drive(self):
		print('Accelerating')

	def flaps(self):
		print('Changing flaps')

	def wheels(self):
		print('Closing wheels')

g = Plane()  #g就是self，作为位置参数传递给methods
print(f'wings: {g.wings}')
print(f'bugs: {g.bugs}')
