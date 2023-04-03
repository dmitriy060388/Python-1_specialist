# число Фибоначчи начинается с 0 1 1 2 3 5 8 13 21 34 55
#                              1 2 3 4 5 6 7 8 9 10 11

""""Число Фибоначчи"
Задание
По данному числу n определите n-е число Фибоначчи.

Формат входных данных
Дано целое положительное число n, номер числа Фибоначчи в последовательности.

Формат выходных данных
Вывести число Фибоначчи с номером n."""

n = int(input())
result = None
x = 0
f1 = 0 # первое число Фибоначчи
f2 = 1 # второе число Фибоначчи


if n == 1:
    result = 0
    print(result)
if n == 2:
    result = 1
    print(result)
else:
    while x < n - 2:
        x += 1
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        result = f3

print(result)