# Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет можно ли
# из длин этих строк построить возрастающую арифметическую прогрессию.(2b-c-a)(2c-b-a)(2a-b-c) = 0
str1, str2, str3 = input(), input(), input()
numa, numb, numc = len(str1), len(str2), len(str3)
if (2 * numb - numc - numa) * (2 * numc - numb - numa) * (2 * numa - numb - numc) == 0:
    print('YES')
else:
    print('NO')
