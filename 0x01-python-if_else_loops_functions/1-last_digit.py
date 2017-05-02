#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def last_number(number):
    if number < 0:
        return (number * -1) % 10
    else:
        return number % 10

last = last_number(number)

if last_number == 0:
    print("Last digit of {} is 0 and is 0".format(number))
elif number < 0:
    print("Last digit of {} is {}".format(number, last_number),
          "and is less than 6 and not 0")
elif last_number < 6:
    print("Last digit of {} is {}".format(number, last_number),
          "and is less than 6 and not 0")
else:
    print("Last digit of {} is {}".format(number, last_number),
          "and is greater than 5")
