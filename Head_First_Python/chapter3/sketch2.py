import os 
os.chdir('/Users/channingliu/Python/Head_First_Python/chapter3')

try:
	data = open('sketch.txt')
	try: 
		for each_line in data:
			(role , the_spoken) = each_line.split(":",1)
			print(role,end='')
			print(' say : ',end='')
			print(the_spoken,end='')
	except ValueError:
		pass
except IOError:
	print('File is missing')