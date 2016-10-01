import os 
os.chdir('/Users/channingliu/Python/Head_First_Python/chapter4')

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
print(man)
print(other)