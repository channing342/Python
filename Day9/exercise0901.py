#-*- coding: UTF-8 -*- 
#File Name	: exercise0901.py
#Edit		: Channing Liu
#Time Date	: 20160721


class IntegerDemo:

	def set_value(self,value):
		self.value = value
	def add(self,p):
		self.value += p

		
b = IntegerDemo ()

b.set_value(25)
b.add(24)
print(b.value)
