from math import sqrt

num_a, num_b = float(input()), float(input())
average, geom = (num_a + num_b) / 2, sqrt(num_a * num_b)
harmon, square = (2 * num_a * num_b) / (num_a + num_b), sqrt((num_a ** 2 + num_b ** 2) / 2)
print(average, geom, harmon, square, sep='\n')
