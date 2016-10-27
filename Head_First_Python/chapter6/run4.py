#!/usr/bin/python
# coding: UTF-8


def sanitize(time_string):
        if '-' in time_string:
                splitter = '-'
        elif ':' in time_string:
                splitter = ':'
        else:
                return(time_string)
        (mins,secs) = time_string.split(splitter)
        return(mins + '.' + secs)

def get_file(the_file):
        try:
                with open(the_file) as file:
                        data = file.readline()
                temp1=(data.strip().split(','))
                return{'Name':temp1.pop(0),'Birthday':temp1.pop(0),'Time':sorted(set([sanitize(t) for t in temp1]))[0:3]}
        except IOError as ioerror:
                print('File error : ' +str(ioerror))
                return(None)

sarah = get_file('sarah2.txt')
print(sarah['Time'])