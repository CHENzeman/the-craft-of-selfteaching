#!/usr/bin/env python

filename = "file.py"

infile = open(filename, 'r')
data = infile.read()
infile.close()

print(data)

#用with语句块更elegant
with open('file.py','r') as f:
	print(f.read())