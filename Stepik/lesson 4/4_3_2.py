side_a, side_b, side_c = int(input()), int(input()), int(input())
if side_a == side_b and side_a != side_c != side_b:
    print('Равнобедренный')
elif side_c == side_b == side_a:
    print('Равносторонний')
else:
    print('Разносторонний')
