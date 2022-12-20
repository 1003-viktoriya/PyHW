# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

full_str = "aabbbccccccccccc"
short_str = ""
simvol_list = []
count_simvol_list = []
simvol_list.append(full_str[0])
count_simvol_list.append(1)
i = 0
for s in full_str[1:]:
    if s == simvol_list[-1]:
        count_simvol_list[i] += 1
    else:
        simvol_list.append(s)
        count_simvol_list.append(1)
        i += 1

for i in range(len(simvol_list)):
    short_str = short_str + str(count_simvol_list[i])
    short_str = short_str + simvol_list[i]
print(short_str)

for i in range(len(short_str)):
    if short_str[i].isdigit() and short_str[i + 1].isdigit():
        k = k + short_str[i]
    elif short_str[i].isdigit():
        k = k + short_str[i]
        full_str_again = full_str_again + (int(k) * short_str[i + 1])
        k = ""

print(full_str_again)
print(full_str == full_str_again)