# Исследуйте функцию f = 2 * x ** 3 + 2 * x ** 2 - 18 * x - 18

# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0

from sympy import *
import matplotlib.pyplot as plt

print("1. Определить корни")
x = Symbol('x')
func = 2 * x ** 3 + 2 * x ** 2 - 18 * x - 18
y = solve(func, x)
print(f'найденные корни: X1 = {round(y[0],2)}; X2 = {round(y[1],2)}')


print("2. Найти интервалы, на которых функция возрастает")
dif = diff(func)
print(solve(0 < dif))


print("3. Найти интервалы, на которых функция убывает")
print(solve(0 > dif))


print("4. Построить график")
list_y = []
for i in range(-5, 6):
    x = i
    y = 2 * x ** 3 + 2 * x ** 2 - 18 * x - 18
    list_y.append(y)
print(list_y)
plt.plot(range(-5, 6), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
plt.plot(range(-5, 6), list_y)
plt.show()


print("5. Вычислить вершину")
roots = solve(dif)
top = roots[0]
x = top
y = 2 * x ** 3 + 2 * x ** 2 - 18 * x - 18
print(f'x = {round(float(top), 2)}, y = {round(float(y), 2)}')


print("6. Определить промежутки, на котором f > 0")
print(solve(0 < func))


print("7. Определить промежутки, на котором f < 0")
print(solve(func < 0))