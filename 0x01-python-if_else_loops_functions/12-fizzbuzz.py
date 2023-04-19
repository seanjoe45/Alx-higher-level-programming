#!/usr/bin/python3
def fizzbuzz():
    numbers = range(1, 101)
    if numbers % 3 == 0 and numbers % 5 != 0:
        print("fizz", end=" ")
    elif numbers % 5 == 0 and numbers % 3 != 0:
        print("buzz", end=" ")
    elif numbers % 5 == 0 and numbers % 3 == 0:
        print("fizzbuzz", end=" ")
    else:
        print("{:d}".format(numbers), end=" ")
