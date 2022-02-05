num_a, num_b, num_c = int(input()), int(input()), int(input())
if num_a < num_b + num_c and num_b < num_a + num_c and num_c < num_a + num_b:
    print('YES')
else:
    print('NO')
