# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]


import random
n = int(input("Введите количество чисел N: "))
pr=[]
spisok=[]
for i in range(1,n+1):
      spisok.append(random.randint(1,10))
for i in range(1,len(spisok)-1):
      pr.append(spisok[i-1] * spisok[-i])
if n%2 !=0:
    pr[int(n/2)]=spisok[int(n/2)]
print(spisok)
print(pr)