x = 0
y = 0
while x == 0:
    x = int(input('Введите координату Х не равную нулю: '))
while y == 0:
    y = int(input('Введите координату Y не равную нулю: '))
if x > 0 and y > 0:
    print('1 четверть')
if x < 0 and y > 0:
    print('2 четверть')
if x < 0 and y < 0:
    print('3 четверть')
if x > 0 and y < 0:
    print('4 четверть')
