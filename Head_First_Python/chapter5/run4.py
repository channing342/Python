#!/usr/bin/python
# coding: UTF-8


def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return(time_string)
	(mins,secs) = time_string.split(splitter)
	return(mins + '.' + secs)	


with open('james.txt') as james:
	data = james.readline()
	james = data.strip().split(',')

with open('julie.txt') as julie:
	data = julie.readline()
	julie = data.strip().split(',')

with open('mikey.txt') as mikey:
	data = mikey.readline()
	mikey = data.strip().split(',')

with open('sarah.txt') as sarah:
	data = sarah.readline()
	sarah = data.strip().split(',')

try:

james = sorted(set([sanitize(each_t) for each_t in james]))
julie = sorted(set([sanitize(each_t) for each_t in julie]))
mikey = sorted(set([sanitize(each_t) for each_t in mikey]))
sarah = sorted(set([sanitize(each_t) for each_t in sarah]))

print(james[0:3])
print(julie[0:3])
print(mikey[0:3])
print(sarah[0:3])
