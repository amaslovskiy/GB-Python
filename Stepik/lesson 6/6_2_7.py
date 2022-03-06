# Даны два числа: натуральное число nn и вещественное число aa. Напишите программу, которая находит площадь
# указанного правильного многоугольника
from math import tan, pi

numn, numa = int(input()), float(input())
square = (numn * numa ** 2) / (4 * tan(pi / numn))
print(square
      )