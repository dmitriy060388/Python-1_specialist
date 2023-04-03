# Название задачи - "Точка в круге"

"""Задание
Даны координаты точки, координаты центра круга и его радиус.
Определить принадлежит ли данная точка кругу.

Будем считать, что точка принадлежит кругу, 
если находится внутри его или на его окружности

Формат входных данных
Даны координаты точки (x, y) - два целых числа.
Координаты центра круга (xr, yr) - два целых числа.
Радиус круга - целое положительное число.

Формат выходных данных
Вывести "Да", если точка принадлежит кругу, и "Нет" в противоположном случае."""

x, y = int(input()), int(input())
xr, yr = int(input()), int(input())
r_circle = int(input())

c = (x - xr) ** 2 + (y - yr) ** 2 / 0.5

if c <= r_circle:
    print('Да')
else:
    print('Нет')
    