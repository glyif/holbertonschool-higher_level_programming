#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def last_number(number):
    if number < 0:
        return (number * -1) % 10
    else:
        return number % 10

last = last_number(number)

if last == 0:
    print("Last digit of {:d} is {:d}".format(number, last),
          "and is 0")
elif last < 0:
    print("Last digit of {:d} is {:d}".format(number, last),
          "and is less than 6 and not 0")
elif last < 6:
    print("Last digit of {:d} is {:d}".format(number, last),
          "and is less than 6 and not 0")
elif last > 5:
    print("Last digit of {:d} is {:d}".format(number, last),
          "and is greater than 5")
