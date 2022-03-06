# На вход программе подается натуральное число n. Напишите программу, которая вычисляет n!.
total = 1
num_n = int(input())
for i in range(2, num_n + 1):
    total *= i
print(total)
