#! /usr/bin/env python3.7
y = 5

def setX(z):
    x = z
    global a
    x = y
    print("X is: ", x)
    a = 7

print("y before setX ", y)
setX(10)
print("y after setX ", y)
print("a after setX ", a)


