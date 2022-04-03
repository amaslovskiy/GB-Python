user_input = input("Введите число: ")

if not user_input.isdigit():  # проверка на число
    print("Не верный формат числа")
    exit()

result = 0
for x in range(1, 4):
    result += int(user_input * x)

print(result)

user_number = int(user_input)
characters_count = 0
temp_number = user_number

while temp_number:
    temp_number //= 10
    characters_count += 1

first_level_multiplication = (10 ** characters_count) + 1
second_level_multiplication = (10 ** (characters_count * 2)) + first_level_multiplication

result = user_number + (user_number * first_level_multiplication) + (user_number * second_level_multiplication)

print(result)
