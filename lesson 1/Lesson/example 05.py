max_count = int(input("Maximum number >>>"))
delimiter = int(input("Number to divide >>>"))

current_count = 0

while True:
    if current_count == max_count:
        break

    current_count += 1

    if current_count % delimiter == 0:
        continue

    print(current_count)
