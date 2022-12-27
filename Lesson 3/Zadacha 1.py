# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4

# out
# [4, 2, 4, 9]
# 8

import random
n = int(input("Введите количество чисел N: "))
perem=0
sum=0
spisok=[]
for i in range(1,n+1):
      spisok.append(random.randint(1,10))
      if i % 2 !=0: 
          sum = sum + spisok[i-1]
print(spisok)
print(sum)