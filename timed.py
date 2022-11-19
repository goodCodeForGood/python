import time

def timeme(func):
    def wrapper():
        timeOne = time.time()
        func()
        timeTwo = time.time()
        print("Total time" , timeTwo - timeOne)
    return wrapper