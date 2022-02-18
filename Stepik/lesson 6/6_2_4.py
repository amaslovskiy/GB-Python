# Напишите программу, вычисляющую значение тригонометрического выражения
# sin x + cos x + tan^2 x по заданному числу градусов x.
from math import *

degrees = radians(float(input()))
print(sin(degrees) + cos(degrees) + pow(tan(degrees), 2))
