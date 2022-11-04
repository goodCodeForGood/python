import time

def timeme(func):
	def wrapper(inputVal):
		print("Total time", time.time())
		func(inputVal)
	return wrapper
	
