# Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
num = int(input())
same_number = True
ldl = num % 10
while num != 0:
    ld = num % 10
    if ldl != ld:
        same_number = False
    num = num // 10

if same_number:
    print('YES')
else:
    print('NO')
