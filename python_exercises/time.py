#!/bin/usr/env python3

import time
time_now = time.localtime(time.time())
year, month, day, hour, minute = time_now[0:5]

print(f'DATE: {year}-{month}-{day}')