# Дано натуральное число n. Напишите программу, которая печатает численный треугольник с высотой
# равной n, в соответствии с примером
num = int(input())
total = 1
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(total, end=' ')
        total += 1
    print()
