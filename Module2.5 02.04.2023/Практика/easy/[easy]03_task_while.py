""""Четные из диапазона"
Задание
Даны два целые числа a и b.

Выведите на экран все целые четные числа от a до b включительно.

Формат входных данных
Даны два целые числа. Гарантируется, что a < b.

Формат выходных данных
Выведите все числа, требуемые по условию задачи."""

a = int(input("a: "))
b = int(input("b: "))

while a <= b:
    if a % 2 == 0:
        print(a)
    
    a += 1
