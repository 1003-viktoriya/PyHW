# Напишите программу, которая будет преобразовывать десятичное число в двоичное. 
# Без применения встроеных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
n = int(input('Введите число: '))
remains= ' '
while n>0:
    remains +=str(n%2)
    n //=2
print(remains)