#!/bin/usr/env python3

introduction = 'Chris Lee is an awesome musician. She is absolutely one of the self-teaching learners.'
print(introduction)

s = 'lucky guy'
print(s[:4])

date = 'Today is 2/2/2016'
print(date[9:])
#还有另一种方法
t = 'Today is %d/%d/%d' % (7, 7, 2016)
print(t)

s = 'Hello, world, world, universe'
s = s.replace('Hello', 'Hi')
print(s)
s_2 = s.replace('world', 'universe', 1)
print(s_2)