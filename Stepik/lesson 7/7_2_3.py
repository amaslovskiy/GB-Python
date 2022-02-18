# Даны два целых числа m и n (m>n). Напишите программу, которая выводит все нечетные
# числа от mm до nn включительно в порядке убывания.
num_m, num_n = int(input()), int(input())
for i in range(num_m % 2 - 1 + num_m, num_n - 1, -2):
    print(i)
