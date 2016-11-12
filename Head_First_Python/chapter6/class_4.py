#!/usr/bin/python
# coding: UTF-8

class AtheletList(list):
        def __init__(self, a_name,a_Birthday=None,a_Time=[]):
                self.name=a_name
                self.birthday=a_Birthday
                list.__init__([])
                self.extend(a_Time)
        def top3(self):
            return (sorted([sanitize(t) for t in self])[0:3])

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
                return AtheletList(temp1.pop(0),temp1.pop(0),temp1)

        except IOError as ioerror:
                print('File error : ' +str(ioerror))
                return(None)

sarah = get_file('sarah2.txt')
james = get_file('james2.txt')
julie = get_file('julie2.txt')
mikey = get_file('mikey2.txt')

print(sarah.name + "'s fastest times are : " + str(sarah.top3()))
print(james.name + "'s fastest times are : " + str(james.top3()))
print(julie.name + "'s fastest times are : " + str(julie.top3()))
print(mikey.name + "'s fastest times are : " + str(mikey.top3()))


channing=AtheletList('Channing Liu')
channing.extend(['0.01','2-38','1.69'])

print (channing)


#     def __init__(self,a_name):
#             list.__init__([])
#             self.name=a_name

#johnny = NamedList("John Paul Jones")
#johnny.append("Bass Player")
#johnny.extend(['Composer','Piano','Musician'])


