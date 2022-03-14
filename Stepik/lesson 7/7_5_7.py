# Дано натуральное число. Напишите программу, которая определяет, является ли последовательность
# его цифр при просмотре справа налево упорядоченной по неубыванию.
num = int(input())
organize = True
ldl = num % 10
while num != 0:
    ld = num % 10
    if ldl > ld:
        organize = False
    else:
        ldl = ld
    num = num // 10

if organize:
    print('YES')
else:
    print('NO')
