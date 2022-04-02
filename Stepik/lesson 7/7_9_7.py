# На вход программе подается два натуральных числа a и b (a< b). Напишите программу,
# которая находит все простые числа от a до b включительно.
num_a, num_b = int(input()), int(input())
for i in range(num_a, num_b + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i)
