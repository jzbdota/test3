#!/usr/bin/env python

# test3.py

from math import sqrt

for i in range(10000,0,-1):
	x = sqrt(i+100)
	y = sqrt(i+268)
	if x == int(x) and y == int(y):
		print i