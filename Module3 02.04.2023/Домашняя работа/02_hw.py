# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
numbers = []
# (random.randint(-100, 100))  # раскомментируйте, чтобы посмотреть работу функции randint
for i in range(20):
    numbers.append(random.randint(-100, 100))
print(numbers)
