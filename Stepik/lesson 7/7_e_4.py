# На вход программе подается натуральное число n. Напишите программу, которая печатает звездную
# рамку размерами n×19.
num = int(input())
count = 19
for i in range(num):
    for j in range(count):
        if i == 0 or i == (num - 1) or j == 0 or j == (count - 1):
            print('*', end='')
        else:
            print(' ', end='')
    print()
