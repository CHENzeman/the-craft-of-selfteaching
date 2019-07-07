#!/usr/bin/env python

filename = "file.py"

with open(filename) as f:
    content = f.readlines()

print(content)
print(type(content))