user_input = input("Введите время в секундах >> ")

if not user_input.isdigit():
    print("Не верный формат числа")
    exit()

user_seconds = int(user_input)
hours = user_seconds // 3600
minuts = (user_seconds % 3600) // 60
seconds = (user_seconds % 3600) % 60

# hourse, minuts, seconds = user_seconds // 3600, (user_seconds % 3600) // 60,  (user_seconds % 3600) % 60
# кортежный синтаксис

print(f"{hours:>02}:{minuts:>02}:{seconds:>02}")
