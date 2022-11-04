import time

def timeme(func):
	def wrapper(inputVal):
		timeOne = time.time()
		func(inputVal)
		timeTwo = time.time()
		print("Total time", timeTwo - timeOne)
	return wrapper
	
# time.sleep = timeme(time.sleep)

# time.sleep(2)
# time.sleep(4)
# time.sleep(0)
# time.sleep(100)