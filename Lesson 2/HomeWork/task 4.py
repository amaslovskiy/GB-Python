# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

user_str = input("введите строку ")
str_word = []
num = 1
for word in range(user_str.count(' ') + 1):
    str_word = user_str.split()
    if len(str(str_word)) <= 10:
        print(f" {num} {str_word[word]}")
        num += 1
    else:
        print(f" {num} {str_word[word][0:10]}")
        num += 1
