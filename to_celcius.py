#!/usr/bin/env python3.7

farTemp = float(input("What temperature (in F) would you like converted to C? "))
celTemp = round((farTemp - 32) * 5 / 9, 2)
print(farTemp, "F is", celTemp, "C")
