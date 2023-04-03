""""Подсчет длинных слов"
Задание
Определить в предоставленном сообщении количество слов длиной больше, чем 5.

Формат входных данных
Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.

Формат выходных данных
Вывести количество найденных слов."""

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
text += " "
current_length = 0
count_of_words5 = 0
i = 0
while i < len(text):
    if text[i] != ' ':
        current_length += 1
    else:
        if current_length > 5:
            count_of_words5 += 1
        current_length = 0
    i += 1
print(count_of_words5)



