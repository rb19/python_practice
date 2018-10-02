import random

def passGen():
	#print random.randint(1,4)
	myList = []
	passLength = input("Enter number of characters you want for your generated password: ")
	# TODO: Add checks for each category.
	# num_check = input("Enable numbers? (Y/N): ")
	# upper_check = input("Enable uppercase letters? (Y/N): ")
	# lower_check = input("Enable lowercase letters? (Y/N): ")
	# special_check = input("Enable special characters (ie !@#$%^&*)? (Y/N): ")

	for i in range (passLength):
		myList.append(str(random.randint(0,9)))
	joinList = ''.join(myList)
	print "Your new generated password: " + joinList

passGen()
