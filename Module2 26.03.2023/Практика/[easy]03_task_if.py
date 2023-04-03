# Название задачи - "Существует ли треугольник"

"""Задание
По длинам трех отрезков, определить возможность существования треугольника, 
составленного из этих отрезков.

Формат входных данных
Даны три целые положительные числа, длины сторон треугольника.

Формат выходных данных
Вывести "Существует", если можно построить треугольник с заданными длинами сторон, 
и "Не существует", если невозможно."""

a = int(input())
b = int(input())
c = int(input())

if a + b > c:
    print('Существует')
else:
    print('Не Существует')
    