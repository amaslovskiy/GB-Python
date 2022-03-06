# Напишите программу, которая находит наименьшее и наибольшее из пяти чисел.
num1, num2, num3, num4, num5 = int(input()), int(input()), int(input()), int(input()), int(input())
num_min = min(num1, num2, num3, num4, num5)
num_max = max(num1, num2, num3, num4, num5)
print('Наименьшее число =', num_min)
print('Наибольшее число =', num_max)
