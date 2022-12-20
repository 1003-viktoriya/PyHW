# Игра с конфетами
import random
def player_move(name_player):
    candy_taken = int(input(name_player + ", сколько возьмёте конфет от 1 до 28: "))
    while candy_taken < 1 or candy_taken > 28:
        candy_taken = int(input(name_player + ", столько взять нельзя. Введите корректное количество конфет: "))
    return candy_taken

player1 = input("Кто будет играть, имя: ")
player2 = "PC"
all_candy_on_table = 150

move = random.randint(0, 2)
if move:
    print("Первый ходит,", player1)
else:
    print("Первый ходит,", player2)

candy_first_player = 0
candy_second_player = 0

while all_candy_on_table > 28:
    if move:
        taken = player_move(player1)
        candy_first_player += taken
        all_candy_on_table -= taken
        move = False
        print(player1, "совершил ход и взял", taken, ", его текущие количество конфет:", candy_first_player,
              ". На столе осталось конфет:", all_candy_on_table)
    else:
        taken = random.randint(1, 28)
        candy_second_player += taken
        all_candy_on_table -= taken
        move = True
        print(player2, "совершил ход и взял", taken, "его текущще количество конфет", candy_second_player,
              ". На столе осталось конфет:", all_candy_on_table)
    print("*********")
if move:
    print("Победу одержал:", player1)
else:
    print("Победу одержал:", player2)
    
# total = 150
# while total>0:
#  print('Сколько кофет берете?')
#  player = int(input())
#  total -= player
#  print(f'{player} Конфет осталось:{total}')
#  bot = random.randint(1, 28)
#  total -=bot
#  print('Ход Бота')
#  print(f'{bot} Конфет осталось:{total}')