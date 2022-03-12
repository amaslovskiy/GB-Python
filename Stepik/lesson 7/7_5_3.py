# Дано натуральное число n,(n≥10). Напишите программу, которая определяет его максимальную и
# минимальную цифры.
num = int(input())
max_num = 0
min_num = 9
while num != 0:
    if num % 10 < min_num:
        min_num = num % 10
    if num % 10 > max_num:
        max_num = num % 10
    num = num // 10
print('Максимальная цифра равна', max_num, '\nМинимальная цифра равна', min_num)
