"""Задача 10: На столе лежат n монеток. 
Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть"""

from random import randint
n = int(input("Введите количество монеток: "))
i = 0
countHeads = 0
countTails = 0
minCount = 0

while i <= n - 1:
    coins = randint(0, 1)
    print(coins, end = " ")
    i+=1
    if coins > 0:
        countHeads+=1
    else:
        countTails+=1
print()
print(f"количество монеток с гербом вверх = {countHeads}, с решкой = {countTails}")  
if countHeads < countTails:
    minCount = countHeads
    print(f"необходимо перевернуть {countHeads} монеток")
else:
    print(f"необходимо перевернуть {countTails} монеток")
    
          
    
