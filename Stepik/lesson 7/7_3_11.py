# Напишите программу, которая считывает натуральное число nn и выводит первые nn чисел последовательности Фибоначчи.
num = int(input())
total, total2 = 0, 1
for i in range(0, num):
    total, total2 = total2, total + total2
    print(total, end=' ')
