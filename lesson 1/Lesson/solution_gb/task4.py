user_input = input("Введите число >>> ")

if not user_input.isdigit():  # проверка на число
    print("Не верный формат числа")
    exit()

number = int(user_input)
max_num = 0

while number and max_num != 9:
    print(number)
    current = number % 10
    number = number // 10
    max_num = current if current > max_num else max_num

print(max_num)
