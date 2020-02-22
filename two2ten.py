def calc(value):
    result = []
    while value:
        result.append(value % 10)
        value = value // 10
    # 逆序，按正常的顺序返回
    return list(reversed(result))


# 二进制转十进制
def two2ten(n):
    list = calc(n)
    result = 0
    for i, val in enumerate(list[-1::-1]):
        if val == 1:
            result += 2 ** i
    return result


# 十进制转二进制
def ten2two(n):
    result = []
    res = ''
    while n > 0:
        result.insert(0, n % 2)
        n //= 2
    for i in result:
        res += str(i)
    return res


print(two2ten(10))
print(ten2two(10))
print(bin(10))
print(0b10)