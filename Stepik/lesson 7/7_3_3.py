# На вход программе подается натуральное число nn. Напишите программу, которая вычисляет значение выражения
# (1 + 1/2 + 1/3 + .. + 1/n) - ln(n)

from math import log
total = 0
total2 = 1
num_n = int(input())
for i in range(1, num_n + 1):
    total += 1 / i
    total2 = total - log(num_n)
print(total2)
