#-*- coding: UTF-8 -*- 
#File Name	: exercise0904.py
#Edit		: Channing Liu
#Time Date	: 20160721

class IntegerDemo:

	def set_value(self,value):
		self.value = value
	def add(self,p):
		self.value += p
	def subtract(self,q):
		self.value -= q
	def multiplication(self,s):
		self.value *= s
	def division(self,n):
		self.value /= n
		
b = IntegerDemo ()

b.set_value(int(input("Value : ")))
b.add(int(input("add : ")))
print(b.value)
b.subtract(int(input(" - : ")))
print(b.value)
b.multiplication(int(input(" * : ")))
print(b.value)
b.division(int(input(" / : ")))
print(b.value)