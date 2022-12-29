# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001

# out
# 8.988

n = float(input("Введите число: "))
toch = float(input("Введите точность:"))
i = 0
temp=0,00
while toch != 1:
    toch = toch*10
    i = i+1
print("Ваше число с заданной точностью равно: ", round(n, i))
