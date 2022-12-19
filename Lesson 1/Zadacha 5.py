"""
5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве. 
https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
in
- 3
- 6
- 2
- 1

out
5.099
"""

ax = 3
ay = 6
bx = 2
by = 1
ab = round (((bx-ax)**2 + (by-ay)**2)**0.5,3)
print (ab)