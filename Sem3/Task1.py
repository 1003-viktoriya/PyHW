# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
nums = [3, 55, 34, 15, 4, 105, 206]
print(nums)
summa = 0
for i in range(len(nums)):
    if i%2==1:
        summa += int(nums[i])
print(f'Сумма элементов на нечетных позициях: {(summa)}')