# x = [123, 2, 1, '1512', None] # список

# x = '123'
# x = list(x)
# print(x)

# fruits = ['banana', 'orange']
# print(fruits[0][2])

# x = [1, 2, 3]
# x.append(4)
# print(x)

# x = [1, 2, 3]
# y = [4, 5, 6]
# x += y сложение двух списков
# print(x)

# x = ['a', 'b', 'c']
# for char in x:
#     print(char)

# x = [1, 3, 5, 8, '1dqwdq']
# for el in x:
#     print(el)

# x = [[1, 2, 3], ['a', 'b', 'c']]
# for el in x:
#     for elel in el:
#         print(el)

# x = [1, 2, 3]
# 
# for el in x:
#     el += 5 # для каждого элемента прибавить 5
#     print(el)

# x = [1, 2, 3]
# n = 5
# for i in range(len(x)): # перебираем в диапазоне длину списка
#     print(x[i]) # если обращаемся к индексу - то обращаемся напрямую к значению
# 
# for el in x: # в el записывается копия значения
#     print(el)
# # когда известно количество операций используем с функцией range


# for i in range(2, 10, 2):
#     print(i)

# x = [1, 2, 3, 4, 5]
# print(x[2:5:2])

# x = [1, 2, 3, 4, 5]
# print(x[4:1:-1])

# x = [1, 2, 3, 4, 5] # - перечисление элементов в обратном порядке
# print(x[::-1])

x = [1, 2, 3]
y = x
x[0] = 5
print(y)