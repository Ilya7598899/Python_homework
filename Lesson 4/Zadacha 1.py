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