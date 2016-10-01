noc = [ "Channing","Luke","Bii" , [ 27, 29 , 25 , [ "Supervised"  , "Senior" , "Junior" ] ] ]

for name in noc:
 	if isinstance(name,list):
 		for e_name in name: 		
 			if isinstance(e_name,list):
 				for d_name in e_name:
 					print (d_name)
 			else:
 				print(e_name)
 				#print()	
 	else:
 			print (name)
 			#print ()


