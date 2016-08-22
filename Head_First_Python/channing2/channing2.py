def lol(the_list,level=0):
	for each_item in the_list:
		if isinstance (each_item,list):
			lol (each_item,level+1)
		else:
			for tab_stop in range(level):
				print("\t",end="")
			print (each_item)

noc = [ "Channing","Luke","Bii" , [ 27, 29 , 25 , [ "Supervised"  , "Senior" , "Junior" ] ] ]

lol(noc)