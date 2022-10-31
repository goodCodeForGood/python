def reverse_list(myList):
	newList = []
	if len(myList) <= 1:
		return myList
	
	else:
		counter = len(myList) - 1
		while counter >= 0:
			newList.append(myList[counter])
			counter -= 1


	return newList
			
			
		
	
