#!/usr/bin/python
# coding: UTF-8

class NamedList(list):
     def __init__(self,a_name):
             list.__init__([])
#             self.name=a_name

johnny = NamedList("John Paul Jones")
johnny.append("Bass Player")
johnny.extend(['Composer','Piano','Musician'])

#print(johnny.name)

for t in johnny:
        print(t)
