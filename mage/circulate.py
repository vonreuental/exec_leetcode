import math


def nine_nine():
    for i in range(1, 10):
        result = []
        for j in range(1, 10):
            if i >= j:
                result.append(f'{j} x {i} = {i * j}')
        print(result)


def diamond(n):
    i = 1
    j = n // 2 + 1
    while i <= n:
        if i < j:
            print(' ' * (j - i) + '*' * (n - 2 * (j - i)))
        elif i == j:
            print("*" * n)
        elif i > j:
            print(' ' * (i - j) + '*' * (n - 2 * (i - j)))
        i += 1


def febonacci(n):
    i = 0
    j = 1
    feb = []
    while j < n:
        feb.append(j)
        i, j = j, i + j
    print(feb)


def feb_rec():
    i = 0
    j = 1
    count = 1
    while count <= 101:
        i, j = j, i + j
        count += 1
    print(j)


def prime_number(n):
    prime_list = [2, 3, 5, 7]
    for i in range(2, n):
        if i % 2 and i % 3 and i % 5 and i % 7:
            prime_list.append(i)
        else:
            continue
    print(prime_list)


def yang_tri(n):
    tri_all = [[1],[1, 1]]
    for i in range(3, n + 1):
        tri_row = [1]
        for j in range(i - 2):
            tri_row.append(tri_all[i - 2][j] + tri_all[i - 2][j + 1])
        tri_row.append(1)
        tri_all.append(tri_row)
    for i in tri_all:
        print(i)


# nine_nine()
# diamond(11)
# febonacci(100)
# feb_rec()
# prime_number(100000)
yang_tri(6)