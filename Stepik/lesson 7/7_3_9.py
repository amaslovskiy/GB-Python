# На вход программе подается натуральное число n, а затем n различных натуральных чисел,
# каждое на отдельной строке. Напишите программу, которая выводит
# наибольшее и второе наибольшее число последовательности.
num = int(input())
largest, large = 0, 0
for i in range(num):
    num = int(input())
    if num > largest:
        large, largest = largest, num
    elif num > large:
        large = num
print(largest, large, sep='\n')


# larg = 1
# num = int(input())
# for i in range(1, num + 1):
#     if num > largest:
#         larg, largest = largest, num
#     elif num > larg:
#         larg = num
# print(largest)
# print(larg)
