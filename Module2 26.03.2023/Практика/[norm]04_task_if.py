# Название задачи - "FooBar"

"""Задание
Дано целое число.
Если оно делится на 3 без остатка - вывести "Foo",
если делится на 5 - вывести "Bar",
а если делится на 3 и на 5 - вывести "Foobar".
Для всех остальных случаев не выводить ничего.

Формат входных данных
Дано целое число.

Формат выходных данных
Вывести "Foo", "Bar" или "Foobar"""

x = int(input())
if x % 3 == 0:
    if x % 3 == 0 and x % 5 == 0:
        print("Foobar")
    else:
        print('Foo')
elif x % 5 == 0:
    print('Bar')
