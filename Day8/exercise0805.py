#-*- coding: UTF-8 -*- 
#File Name	: exercise0805.py
#Edit		: Channing Liu
#Time Date	: 20160721

def factorial(p):
  i = 1
  s = 1
  while i <=p:
    s *= i
    i += 1
  return s

p = int(input("Number p : "))
print (factorial(p))
