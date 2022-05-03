gain = int(input("Введи выручку фирмы: "))
cost = int(input("Введи издержки фирмы: "))

if gain > cost:
    income = gain - cost
    ros = income / gain * 100
    print(f"Твоя фирма работает с прибылью, рентабельность выручки {ros:.2f}%")
    mem = int(input("Введите количество сотрудников: "))
    p_cost = income / mem
    print("Прибыль фирмы в расчете на одного сотрудника", round(p_cost, 2))
else:
    print("Фирма работает в убыток")
