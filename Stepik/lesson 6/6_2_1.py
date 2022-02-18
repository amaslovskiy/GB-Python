from math import sqrt

num_x1, num_y1, num_x2, num_y2 = float(input()), float(input()), float(input()), float(input())
evkl = sqrt((num_x1 - num_x2) ** 2 + (num_y1 - num_y2) ** 2)
print(evkl)
