#!/usr/bin/python
# coding: UTF-8
import sys
import os
import pickle

with open('james.txt') as james:
	data = james.readline()
	james = data.strip().split(',')

with open('julie.txt') as julie:
	data = julie.readline()
	julie = data.strip().split(',')

with open('mikey.txt') as mikey:
	data = mikey.readline()
	mikey = data.strip().split(',')
	#mikey.sort()

with open('sarah.txt') as sarah:
	data = sarah.readline()
	sarah = data.strip().split(',')

def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return(time_string)
	(mins,secs) = time_string.split(splitter)
	return(mins + '.' + secs)	

clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []

for each_t in james:
	clean_james.append(sanitize(each_t))
for each_t in julie:
	clean_julie.append(sanitize(each_t))
for each_t in mikey:
	clean_mikey.append(sanitize(each_t))
for each_t in sarah:
	clean_sarah.append(sanitize(each_t))

print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))
