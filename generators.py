#! /usr/bin/env python3.7

def genRange(stop, start=1, step=1):
    num = start
    while num <= stop:
        yield num
        num += step

def genFib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a