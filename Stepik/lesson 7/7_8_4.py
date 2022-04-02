# Дано нечетное натуральное число n. Напишите программу, которая печатает равнобедренный звездный
# треугольник с основанием, равным n в соответствии с примером
num = int(input())
for i in range(num // 2 + 1):
    for j in range(i + 1):
        print('*', end='')
    print()
for k in range(num // 2 - 1, -1, -1):
    for s in range(k + 1):
        print('*', end='')
    print()
