import os 
os.chdir('/Users/channingliu/Python/Head_First_Python/chapter3')
data = open('sketch.txt')
for each_line in data:
	if  each_line.find(':') != -1 :
		(role , the_spoken) = each_line.split(":",1)
		print(role,end='')
		print(' say : ',end='')
		print(the_spoken,end='')