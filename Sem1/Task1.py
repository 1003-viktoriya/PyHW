#Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

a = int(input('Введите номер дня недели: '))
if 1<=a<=5:
  print('нет')
elif 6<=a<=7:
   print('да')
else:
  print('нет такого номера дня недели')