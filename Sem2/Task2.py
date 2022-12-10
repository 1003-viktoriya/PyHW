#Задайте список из n чисел последовательности (1 + 1/n)^n. 
# Вывестив консоль сам список и сумму его элементов.
num = int(input("Введите число: "))
list = []
for i in range (1, num+1):
    list.append(f'{(1+1*i)**i}')
print(list)
# list_length=len(list)
# sum=0
# list[i] = [list[i].astype (int)
# for i in range(list_length):
#     sum += list[i]
# print(sum)
def sum_elements(num):
    sum=0
    for i in num:
        sum += num
    retern (sum)
sum_elements()
