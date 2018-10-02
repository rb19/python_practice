import random

def passGen():
	#print random.randint(1,4)
	myList = []
	for i in range (10):
		myList.append(str(random.randint(0,9)))
	joinList = ''.join(myList)
	print "Your new generated password: " + joinList

passGen()
