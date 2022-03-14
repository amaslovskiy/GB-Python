# Дано натуральное число n(n>9). Напишите программу, которая определяет его вторую (с начала) цифру.
num = int(input())
sd = num % 10
while num > 9:
    ld = num % 10
    num = num // 10
    sd = ld
print(sd)
