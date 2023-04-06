#!/usr/bin/python3
import random
number = random.randint(-10, 10)
number = int(number)
if (number > 0):
    print ("{} is positive\n".format(number))
elif (number == 0):
    print ("{} is zero\n".format(number))
else:
    print ("{} is negative\n".format(number))
