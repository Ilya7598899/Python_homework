"""
2. Напишите программу для проверки ложности утверждения
(W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат.

"""
for x in range (2):
        for y in range (2):
            for z in range (2):
                print(not (x or y or z) == (not x and not y and not z))
                print (x, y, z)