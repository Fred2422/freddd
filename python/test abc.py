#!/usr/bin/python3
#a=int (input())
#b=int (input(random.randint (-110,100))) 
print ("введите числа")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
min=a
if min>b:
    min=b
if min>c:
    min=c
print ("ответ")
print (min)