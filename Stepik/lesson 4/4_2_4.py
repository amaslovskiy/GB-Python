n_num = int(input())
if 1000 <= n_num <= 9999 and (n_num % 7 == 0 or n_num % 17 == 0):
    print('YES')
else:
    print('NO')
