# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0.67 -> 13
# 198.45 -> 27

list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
s = 0
a = 0
print ("Введите через Enter по цифрам Ваше число (если оно дробное,  то символ дроби вводить не нужно), если цифр больше нет введите '888': ")
for i in list:
    while a != 888:
        a = int(input())
        list[i] = a
        s = s + list[i]

print("Сумма цифр =", s-888)


# x = (input("Введите число:"))
# def  Sumnumber (num):
#     tot = 0
#     while(num >  0):
#         dig = num % 10
#         tot = tot + dig
#         num = num//10
#     return  tot
# print(Sumnumber(x))