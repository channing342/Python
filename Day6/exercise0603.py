#-*- coding: UTF-8 -*-
#File Name	: exercise0603.py
#Edit		: Channing Liu
#Time Date	: 20160631

score = int(raw_input("What is your score : "))

if score < 60:
	print("Bad")
elif 60<= score < 70:
	print("Not Bad!")
elif 70<= score < 80:
	print("Good!")
elif 80<= score < 90:
	print("Great!")
elif 90<= score < 100:
	print("Excellent")
elif score == 100:
	print("Perfect")
else:
	print("Your integer out of range")

