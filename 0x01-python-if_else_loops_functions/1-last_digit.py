#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l = abs(number) % 10
if (number < 0):
    l *= -1
print("Last digit of", end=" ")
if (l > 5):
    print("{:d} is {:d} and is greater than 5".format(number, l))
elif (l == 0):
    print("{:d} is {:d} and is 0".format(number, l))
else:
    print("{:d} is {:d} and is less than 6 and not 0".format(number, l))
