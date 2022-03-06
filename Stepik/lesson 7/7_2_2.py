# Даны два целых числа m и n. Напишите программу, которая выводит все числа от m до n включительно
# в порядке возрастания, если m < n, или в порядке убывания в противном случае.
num_m, num_n = int(input()), int(input())
if num_m < num_n:
    for i in range(num_m, num_n + 1):
        print(i)
elif num_m > num_n:
    for i in range(num_m, num_n - 1, -1):
        print(i)
elif num_m == num_n:
    num_n = num_m
    print(num_m)
