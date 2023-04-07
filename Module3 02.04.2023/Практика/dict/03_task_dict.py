# Данные о сотрудниках в программе хранятся в словаре
staff = [
    {
        'name': 'Алексей',
        'surname': 'Петров',
        'salary': 124300
    },
    {
        'name': 'Николай',
        'surname': 'Петров',
        'salary': 120000
    },
    {
        'name': 'Иван',
        'surname': 'Павлов',
        'salary': 34500
    },
    {
        'name': 'Василий',
        'surname': 'Кукушкин',
        'salary': 162500
    },
    {
        'name': 'Василий',
        'surname': 'Павлов',
        'salary': 47800
    },
]
# Вычислите:
print("Имя и Фамилию сотрудника с самой высокой зарплатой:")
max = staff[0]['salary']
for el in staff:
    if el['salary'] > max:
        max = el['salary']
print(max)

print("Имя и Фамилию сотрудника с самой низкой зарплатой:")
min = staff[0]['salary']
for el in staff:
    if el['salary'] < min:
        min = el['salary']
print(min)


print("Среднеарифметическую зарплату всех сотрудников")
x = 0
for el in staff:
    x += el['salary']
print(x/len(staff))

print("Количество однофамильцев в организации")
x = {}
for el in staff:
    x[el['surname']] = 0
for el in staff:
    x[el['surname']] += 1
print(*x.items())


print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")
