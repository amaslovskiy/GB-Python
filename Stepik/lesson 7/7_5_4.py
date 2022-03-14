# Дано натуральное число. Напишите программу, которая вычисляет:
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.
num = int(input())
num_sum, count, prod = 0, 0, 1
ldl = num % 10
while num != 0:
    fd = num % 10
    num_sum += fd
    count += 1
    prod *= fd
    num = num // 10
print(num_sum, count, prod, num_sum / count, fd, fd + ldl, sep='\n')
