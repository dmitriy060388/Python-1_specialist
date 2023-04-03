x = int(input())

result = False

if x >= 8:
    result = True

if x % 3 == 0 or x % 5 == 0:
    result = True

if result:
    print('Да')
else:
    print('Нет')
    