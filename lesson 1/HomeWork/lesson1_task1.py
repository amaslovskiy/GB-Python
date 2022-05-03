value = 7  # какая то переменная 1
name = "Usver"  # какая то переменная 2
print(name, value)  # вывод на экран 2 переменных

day = int(input("Please input your day of birth: "))  # запрос дня рождения
month = input("Please input your month of birth: ")  # запрос месяца
year = int(input("Please input your year of birth: "))  # запрос года
sex = input("What is your sex? ")  # указание пола
marital_status = input("Tell me your marital status <single/married/etc> : ")  # семейное положение
print(f"Hi, Usver 7! Your birthday is {day} {month} {year} , and your sex is {sex}. You are {marital_status}, good luck!")
