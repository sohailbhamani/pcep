#!/usr/bin/env python3.7

myString = input("Enter a message: ")
print("First Character: ", myString[0])
print("Last Character: ", myString[-1])
print("Middle Character: ", myString[int((len(myString)) / 2)])
print("Even Index Characters: ", myString[::2])
print("Odd Index Characters: ", myString[1::2])
print("Reversed Message: ", myString[::-1])
