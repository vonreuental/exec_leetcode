def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def febonacci(n):
    if n == 0 or n == 1:
        return n
    return febonacci(n - 1) + febonacci(n - 2)


def pow(x, n):
    # 库函数
    # return x ** n

    # 递归
    # if n <= 1:
    #     return x
    # return x * pow(x, (n - 1))

    # 分治
    # if n == 0:
    #     return 1
    # if n < 0:
    #     return 1 / pow(x, -n)
    # if n % 2 != 0:
    #     return x * pow(x, n - 1)
    # return pow(x * x, n / 2)

    # 位运算
    if n < 0:
        x = 1 / n
        n = - n
    pow = 1
    while n:
        if n & 1:
            pow *= x
        x *= x
        n >>= 1
    return pow


if "__name__" != "__main__":
    x = 5
    n = 3
    print(f'{n}阶乘的结果{factorial(n)}')
    print(f'{n}斐波那契的结果{febonacci(n)}')
    print(f'{x}的{n}次方是{pow(x, n)}')
