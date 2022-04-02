# Дано натуральное число n,(n>9). Напишите программу, которая определяет его третью (с начала)цифруnu
num = int(input())
sd = num % 10
while num > 99:
    ld = num % 10
    num = num // 10
    sd = ld
print(sd)
