# На вход программе подается число nn – количество собачьих лет.
# Напишите программу, которая вычисляет возраст собаки в человеческих годах.
y_dog = int(input())
f2year = y_dog - 2
if y_dog == 1 or y_dog == 2:
    y_human = y_dog * 10.5
else:
    y_human = float(2 * 10.5 + f2year * 4)
print(y_human)
