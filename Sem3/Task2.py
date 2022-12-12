# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]
nums = int(input('Введите количество чисел в списке: '))
my_list =[]
from random import randint
for i in range(nums):
    my_list.append(randint(1, 10))
print(my_list)
# nums = [3, 55, 34, 15, 4, 105, 206]
# print(nums)
result = []
for i in range(int(len(my_list)/2)):
    result.append(my_list[i]*my_list[-i-1])
for i in range(len(result)):
    print(f'Произведение {i+1} пары: {result[i]}')
