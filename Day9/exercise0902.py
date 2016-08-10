#-*- coding: UTF-8 -*- 
#File Name	: exercise0902.py
#Edit		: Channing Liu
#Time Date	: 20160721

class IntegerDemo:

	def set_value(self,value):
		self.value = value
	def add(self,p):
		self.value += p

		
b = IntegerDemo ()

b.set_value(int(input("Value : ")))
b.add(int(input("add : ")))
print(b.value)