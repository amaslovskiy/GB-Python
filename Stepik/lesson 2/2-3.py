# n школьников делят k мандаринов поровну, неделящийся остаток остается в корзине.
# Сколько целых мандаринов достанется каждому школьнику? Сколько целых мандаринов останется в корзине?
# Формат входных данных
# На вход программе подаётся два целых числа: количество школьников и количество мандаринов,
# каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести два числа: количество мандаринов, которое достанется каждому школьнику,
# и количество мандаринов, которое останется в корзине, каждое на отдельной строке.
pupils, tang = int(input()), int(input())
num_tang, tang_left = tang // pupils, tang % pupils
print(num_tang)
print(tang_left)
