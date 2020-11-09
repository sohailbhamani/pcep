#!/usr/bin/env python3.7

name = input("What is your name? ")
color = input("What is your favorite color? ")
age = int(input("How old are you today? "))
# print(name, end= " ")
# print("is " + str(age) + " years old", end= " ")
# print("likes the color " + color + ".", end= " ")

print(name, 'is', age, 'years old and loves the color', color + ".", sep=" ")


