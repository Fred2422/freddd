
print ("введите общую сумму чека") 
a = float(input("a = ")) #сумма чека 
if a<0:
    print ("чек-a должен быть больше 0!")
    quit()
print ("введите процент чаевых от общей суммы")
b = float(input("b = ")) #процент чаевых 
if b<0:
    print ("чаевые-b должны быть больше 0!")
    quit()
print ("сколько человек оплачивают счет?")
c = int(input("c = ")) #сколько человек оплачивает счет
d = (a+b)/c
print ("сколько должен оплатить один человек из всех")
print (d)
 
