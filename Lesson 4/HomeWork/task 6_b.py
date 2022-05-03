def gen2():
    lst = [1, 77, 0, "repeat"]

    from itertools import islice
    from itertools import cycle

    for el in islice(cycle(lst), 10):
        print(el)


gen2()
