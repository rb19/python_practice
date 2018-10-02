import random

def passGen():
	#print random.randint(1,4)
	myList = []
	x = input("Enter number of characters you want for your generated password: ")

	for i in range (10):
		myList.append(str(random.randint(0,x)))
	joinList = ''.join(myList)
	print "Your new generated password: " + joinList

passGen()
