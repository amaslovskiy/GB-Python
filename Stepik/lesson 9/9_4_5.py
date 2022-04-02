# На вход программе подается строка текста. Напишите программу, которая проверяет,
# что строка заканчивается подстрокой .com или .ru.

s = input()
if s.endswith('.com') == True or s.endswith('.ru') == True:
    print('YES')
else:
    print('NO')
