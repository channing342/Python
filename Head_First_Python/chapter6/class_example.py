#!/usr/bin/python
# coding: UTF-8

class Demo:
    __x = 0
 
    def __init__(self, i):
        self.__i = i
        Demo.__x += 1
     
    def __str__(self):
        return str(self.__i)
          
    def hello(self):
        print("hello", self.__i)
     
    @classmethod
    def getX(cls):
        return cls.__x
 
class SubDemo(Demo):
    pass
 
 
a = SubDemo(1234)
a.hello()
print(a.getX())
b = SubDemo(5678)
b.hello()
print(b.getX())
c = SubDemo(9012)
c.hello()
print(c.getX())
d = SubDemo(3456)
d.hello()
print(b.getX())
e = SubDemo(7890)
e.hello()
print(c.getX())
