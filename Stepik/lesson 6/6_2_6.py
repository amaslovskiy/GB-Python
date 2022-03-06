# Даны три вещественных числа a, b, c. Напишите программу, которая находит вещественные корни квадратного уравнения
from math import sqrt

numa, numb, numc = float(input()), float(input()), float(input())
numd = numb ** 2 - 4 * numa * numc
if numd > 0:
    root1, root2 = (- numb + sqrt(numd)) / (2 * numa), (- numb - sqrt(numd)) / (2 * numa)
    print(min(root1, root2), max(root1, root2), sep='\n')
elif numd == 0:
    root1 = - numb / (2 * numa)
    print(root1)
elif numd < 0:
    print('Нет корней')
