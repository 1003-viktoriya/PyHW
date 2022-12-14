# 1) Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from functools import reduce

str_nums = input("Введите список чисел через пробел: ")
nums = list(map(int, str_nums.split()))
summa = sum([nums[i] for i in range(len(nums)) if nums[i] % 2 == 1])

print(summa)


# 2) Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

# nums = [9, 5, 6, 2, 6, 9]
# res = [i * j for i, j in zip(nums[:len(nums) // 2], nums[::-1][:len(nums) // 2])]
# for i in range(len(res)):
#     print("Произведение", i + 1, "пары:", res[i])