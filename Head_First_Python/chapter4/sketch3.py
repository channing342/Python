#!/usr/bin/python
# coding: UTF-8
import sys
import os 
os.chdir('/home/tomcat/Python/Head_First_Python/chapter4')

man=[]
other=[]
try:
        data = open('sketch.txt')
        try: 
                for each_line in data:
                        (role , line_spoken) = each_line.split(":",1)
                        line_spoken = line_spoken.strip()
                        if role == 'Man':
                                man.append(line_spoken)
                        elif role == 'Other Man':
                                other.append(line_spoken)
        except ValueError:
                pass
        data.close()
except IOError:
        print('File is missing')

try:
        with open("man.txt","w") as out,open("other_man.txt","w") as out1:
                print(man,file=out)
                print(other,file=out1)
except IOError:
        print('File error.')

def print_lol(the_list,indent=False,level=0,fh=sys.stdout):
        for each_item in the_list:
                if isinstance(each_item,list):
                        print_lol(each_item,indent,level+1,fh)
                else:
                        if indent:
                                for tab_stop in range(level):
                                        print("\t",end="",file=fh)
                        print(each_item,file=fh)

print_lol(man)
print ()
print_lol(other)
