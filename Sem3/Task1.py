# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# from random import randint
nums = int(input('Введите количество чисел в списке: '))
my_list =[]
from random import randint
for i in range(nums):
    my_list.append(randint(1, 20))
print(my_list)
summa = 0
for i in range(len(my_list)):
    if i%2==1:
        summa += int(my_list[i])
print(f'Сумма элементов на нечетных позициях: {(summa)}')