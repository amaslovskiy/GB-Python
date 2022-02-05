num1, num2, num3 = int(input()), int(input()), int(input())
n1, n2, n3 = 0, 0, 0
if num1 >= 0:
    n1 = num1
if num2 >= 0:
    n2 = num2
if num3 >= 0:
    n3 = num3
if n1 + n2 + n3 >= 0:
    print(n1 + n2 + n3)
else:
    print(0)
