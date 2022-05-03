start = int(input("Укажите км за первый день"))
goal = int(input("Укажите желаемый км"))

day_counter = 1

while start < goal:
    day_counter += 1
    start += start * .10
else:
    print(f"День достижения = {day_counter} ")
