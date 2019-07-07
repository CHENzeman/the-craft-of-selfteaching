#!/bin/usr/env python3

#1.
def a_func(a,b):
	sum = a+b
	return a,b,sum

def b_func():
	name = 'lea'
	weight = '45KG'
	height = '154cm'
	job = 'student'
	goal = 'programmer'
	return name, weight, height, job, goal

print(a_func(2,4))
name, weight, height, job, goal = b_func()
print(name)
print(height)
print(weight)
print(job)
print(goal)
#不用每个都写，用一个variable就可以
data = b_func()
print(data)
