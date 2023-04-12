#!/usr/bin/python3
import random
number = random.randit(-10000, 100000)
number = int(number)
if number < 0:
    last_digit = ((number * -1) % 10) * -1
elif number == 0:
    last_digit = 0
else:
    last_digit = number % 10
if last_digit > 5:
    print("last digit of {} is {} and\ is greater than 5".format(number, last_digit))
elif last_digit == 0:
    print("last digit 0f {} is {} and is 0".format(number, last_digit))
elif last_digit < 6 and last_digit != 0:
    print("last digit of {} is {} and is less than\ 6 and not 0".format(number, last_digit))
