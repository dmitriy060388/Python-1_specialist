""""Кратные пяти из диапазона"
Задание
Даны два целые числа a и b.

Выведите на экран все целые кратные 5 от a до b включительно.

Формат входных данных
Даны два целые числа. Не гарантируется, что a < b.
Если a > b, то выводим все числа из диапазона [b, a].

Формат выходных данных
Выведите все числа, требуемые по условию задачи."""

a = int(input("a: "))
b = int(input("b: "))

for i in range(a, b+1):
    if i % 5 == 0:
        print(i)
if a > b:
    for i in range(b, a+1):
        if i % 5 == 0:
            print(i)
