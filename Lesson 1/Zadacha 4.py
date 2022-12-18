a = int(input('Введите номер четверти: '))
if a != 1 and a != 2 and a != 3 and a != 4: print('Нет такой четверти')
if a == 1:
    print('x > 0, y > 0')
if a == 2:
    print('x < 0, y > 0')
if a == 3:
    print('x < 0, y < 0')
if a == 4:
    print('x > 0, y < 0')
