#-*- coding: UTF-8 -*-
#File Name	: exercise0705.py
#Edit		: Channing Liu
#Time Date	: 20160731

i = int(raw_input("Range is : "))

for a in range (i,0,-1):
	print (a*'*')

s = 0
while i>=s:
	print(i*'*')
	i -= 1