# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

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