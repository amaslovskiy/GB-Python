num1, num2, math = int(input()), int(input()), input()
if math == '+':
    print(num1 + num2)
elif math == '-':
    print(num1 - num2)
elif math == '*':
    print(num1 * num2)
elif math == '/' and num2 == 0:
    print('На ноль делить нельзя!')
elif math == '/':
    print(num1 / num2)
else:
    print('Неверная операция')
