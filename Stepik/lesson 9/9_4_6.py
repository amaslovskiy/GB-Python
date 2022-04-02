# На вход программе подается строка текста. Напишите программу, которая выводит на экран символ,
# который появляется наиболее часто.

s = input()
count_d = 0
count_c = ' '
for i in range(len(s)):
    if s.count(s[i]) >= count_d:
        count_d = s.count(s[i])
        count_c = s[i]
print(count_c)
