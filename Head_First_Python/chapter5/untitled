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

james = sorted([sanitize(each_t) for each_t in james])
julie = sorted([sanitize(each_t) for each_t in julie])
mikey = sorted([sanitize(each_t) for each_t in mikey])
sarah = sorted([sanitize(each_t) for each_t in sarah])

unique_james = []
unique_julie = []
unique_mikey = []
unique_sarah = []

for each_t in james:
	if each_t not in unique_james:
		unique_james.append(each_t)
for each_t in julie:
	if each_t not in unique_julie:
		unique_julie.append(each_t)
for each_t in mikey:
	if each_t not in unique_mikey:
		unique_mikey.append(each_t)
for each_t in sarah:
	if each_t not in unique_sarah:
		unique_sarah.append(each_t)

print(unique_james[0:3])
print(unique_julie[0:3])
print(unique_mikey[0:3])
print(unique_sarah[0:3])
