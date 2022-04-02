# На вход программе подается два натуральных числа aa и b (a < b). Напишите программу,
# которая находит натуральное число из отрезка [a;b] с максимальной суммой делителей.
num_a, num_b = int(input()), int(input())
count, largest = 0, 0
for i in range(num_a, num_b + 1):
    total = 0
    for j in range(1, i + 1):
        if i % j == 0:
            total += j
        if total >= count and i >= largest:
            count = total
            largest = i
print(largest, count)
