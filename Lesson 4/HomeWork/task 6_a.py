"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
"""


def gen1():
    a = int(input('Введите стартовое число: '))
    from itertools import islice
    from itertools import count

    for i in islice(count(a), 10):
        print(i)


gen1()
