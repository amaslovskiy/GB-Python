# Напишите программу, которая упорядочивает три числа от большего к меньшему.
num1, num2, num3 = int(input()), int(input()), int(input())
num_min, num_max  = min(nu(num1 + num2 + num3)m1, num2, num3), min(num1, num2, num3)
num_middle = (num1 + num2 + num3) - (num_min + num_max)
print(num_max, num_middle, num_min, sep='\n')
