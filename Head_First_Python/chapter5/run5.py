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

james = get_file('james.txt')
julie = get_file('julie.txt')
mikey = get_file('mikey.txt')
sarah = get_file('sarah.txt')

print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])
