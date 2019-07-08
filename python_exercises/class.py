#!/bin/usr/env python3

class Website():
	def __init__(self, title):
		self.title = title
		self.show_title()

	def show_title(self):
		print(self.title)

	def location(self):
		print('location: archive.com')

obj = Website('keto-diet.com')
obj.show_title()
obj.location()