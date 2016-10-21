#!/usr/bin/python
# coding: UTF-8

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

clean_james = sorted([sanitize(each_t) for each_t in james])
clean_julie = sorted([sanitize(each_t) for each_t in julie])
clean_mikey = sorted([sanitize(each_t) for each_t in mikey])
clean_sarah = sorted([sanitize(each_t) for each_t in sarah])

print(clean_james[0:3])
print(clean_julie)
print(clean_mikey)
print(clean_sarah)
