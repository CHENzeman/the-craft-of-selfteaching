#!/bin/usr/env python3

class Friend:
	def __init__(self):
		self.job = 'None'
		self.age = 'None'

	def get_job(self):
		return self.job

	def set_job(self,job):
		self.job = job

	def set_age(self,age):
		self.age = age

	def get_age(self):
		return self.age

Alice = Friend()
Alice.set_job('software designer')
print(Alice.get_job())
print(Alice.job)
Alice.set_age(23)
print(Alice.age)