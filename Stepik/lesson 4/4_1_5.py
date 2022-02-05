num1, num2, num3, num4 = int(input()), int(input()), int(input()), int(input())
if num1 > num2:
    num1 = num2
if num3 > num4:
    num3 = num4
if num1 < num3:
    print(num1)
else:
    print(num3)
