def swap_list(myList):
	if len(myList) <= 1:
		return myList

	else:
		#for lists with even number of elements
		if len(myList) % 2 == 0:     
			myList[-1], myList[(len(myList) // 2) - 1] = myList[(len(myList) // 2) - 1], myList[-1]
			return myList
                        
		else:  
			# for lists with odd number of elements
			myList[-1], myList[(len(myList) // 2)] = myList[(len(myList) // 2)], myList[-1]
			return myList
					
