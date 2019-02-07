# Use this script to generate a password of any length.
# TODO: Add checks for each category. Write these as separate methods

import random
import string

def passGen():
    myList = []
    # num_check(num_enable)
    # print num_enable
    passLength = input("Enter number of characters you want for your generated password: ")

    # Call each check function here.
    # upper_check()
    # lower_check()
    # special_check()

    special_case = '!@#$%^&*()[]}{+=-_?/<>'
    for i in range (passLength):
        # 0 = number; 1 = uppercase ; 2 = lowercase; 3 = special chars
        char_type = random.randint(0,3)
        if char_type == 0:
            myList.append(str(random.randint(0,9)))
        elif char_type == 1:
            myList.append(str(random.choice(string.ascii_uppercase)))
        elif char_type == 2:
            myList.append(str(random.choice(string.ascii_lowercase)))
        else:
            myList.append(str(random.choice(special_case)))
    joinList = ''.join(myList)
    print "Your new generated password: " + joinList

passGen()
