# Напишите программу, которая находит полное число метров по заданному числу сантиметров.
#
# Формат входных данных
# На вход программе подаётся натуральное число – количество сантиметров.
#
# Формат выходных данных
# Программа должна вывести одно число – полное число метров.
num = int(input())
num_met = num // 100
print(num_met)