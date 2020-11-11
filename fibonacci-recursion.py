#! /usr/bin/env python3.7

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fib(n - 2) + fib(n - 1)

itemToCalc = int(input("What Fibonacci item would you like to calculate? "))
print(fib(itemToCalc))
