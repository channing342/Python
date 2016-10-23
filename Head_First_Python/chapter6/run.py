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
                return(data.strip().split(','))
        except IOError as ioerror:
                print('File error : ' +str(ioerror))
                return(None)


sarah = get_file('sarah2.txt')

(sarah_name,sarah_dob) = sarah.pop(0) , sarah.pop(0)
print(sarah_name + "'s fastest times are : " + str(sorted(set([sanitize(t) for t in sarah]))[0:3]))