import random
import time

start = input("Roll die? ")

if start == "Yes" or start == "yes" or start == "y":
	print("Rolling die!")
	time.sleep(1)
	roll = random.randint(1,6)
	print("You rolled a " + str(roll))

	i=0
	while (i < 2) :
		try_again = input("Roll again? ")
		if try_again == "Yes" or try_again == "yes" or try_again == "y":
			print("Rolling again! ")
			time.sleep(1)
			roll2 = random.randint(1,6)
			print("You rolled a " + str(roll2))
			i += 1
		else:
			print("No? Are you sure? ")
			i -= 1
	print("That's all for now! Thanks for trying! ")
	
else:
	print ("Boo! You're missing out on an awesome die rolling simulator! ")
	time.sleep(1)
	print ("Bye!")