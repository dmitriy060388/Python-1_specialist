# people['address']['city']

#  создаём словарь
# phonebook = {}
# phonebook["Boris"] = 89152995195
# phonebook["Alex"] = 89152995197
#  phonebook.pop('Boris')
#  print(phonebook.keys()) # вывести только ключи
# 
# for key, value in phonebook.items(): # конструкция цикла for для работы со словарями, 
#     должна быть только такая конструкция
#     print(key, value)

x = {'kek': 'bug'}
y = x.copy()
x['kek'] = 'kek2'
print(y)