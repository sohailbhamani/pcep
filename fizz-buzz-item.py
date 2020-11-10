#!/usr/bin/env python3.7

userInt = int(input("Enter an integer value: "))
if (userInt % 3 == 0) and (userInt % 5 == 0):
    print("FizzBuzz")
elif userInt % 3 == 0:
    print("Fizz")
elif userInt % 5 == 0:
    print("Buzz")
else:
    print(userInt)
