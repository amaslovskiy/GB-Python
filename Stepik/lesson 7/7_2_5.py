# Дано натуральное число n. Напишите программу, которая выводит таблицу умножения на n
num_n = int(input())
j = 0
for i in range(num_n, num_n * 11, num_n):
    j = j + 1
    print(num_n, 'x', j, '=', i)
