#-*- coding: UTF-8 -*-
#File Name	: exercise0709.py
#Edit		: Channing Liu
#Time Date	: 20160731

range = int(raw_input("Range is : "))
i = 1
a = 1
while i <= range:
	a *= i
	i += 1
print (a)