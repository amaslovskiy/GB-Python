# На вход программе подается натуральное число n. Напишите программу, которая подсчитывает сумму тех чисел
# от 1 до n (включительно) квадрат которых оканчивается на 2, 5 или 8.
total = 0
num_n = int(input())
for i in range(1, num_n + 1):
    if i ** 2 % 10 == 5:
        total += i
print(total)