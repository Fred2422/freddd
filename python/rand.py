#!/usr/bin/python3

import random

print ("введите числа а и б")
a = float(input("a = "))
b = float(input("b = "))
if ( a > b ):
    result = random.randint (b,a)
else:
    result = random.randint (a,b)

print (result)
