number = int(input("Enter some number: "))  # запрашиваем число
n = str(number)  # приводим переменную к строковому типу
number2 = n + n  # складываем строки и помещаем в number2
number3 = n + n + n  # складываем строки и помещаем в number3
summ = number + int(number2) + int(number3)  # приводим строки к целому типу и все складываем
print("Result is: ", summ)  # выводим результат
