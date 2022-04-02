# Дано натуральное число n. Напишите программу, которая выводит значение суммы 1!+2!+3!+…+n!.
num = int(input())
count, prod = 0, 1
for i in range(1, num + 1):
    prod *= i
    count += prod
print(count)
