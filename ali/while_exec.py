# 求100以内所有奇数之和
def sum_singular():
    count = 1
    sum = 0
    while count < 100:
        sum += count
        count += 2
    print(f"100以内的奇数之和为{sum}")


# 求100以内7的倍数之和，以及个数
def sum_seven():
    count = 1
    sum = 0
    while count * 7 < 100:
        sum += count * 7
        count += 1
    print(f"100以内7的倍数和为{sum}, 个数为{count - 1}")


# 1000以内水仙花数
def daffodils():
    num = 100
    while num < 1000:
        a = num // 100
        b = (num - a * 100) // 10
        c = num % 10
        if a ** 3 + b ** 3 + c ** 3 == num:
            print(num)
        num += 1


# 判断输入数字是否是质数
def Prime_num():
    num = int(input("请输入一个数字："))
    i = 2
    is_prime = True
    while i < num:
        if num % i == 0:
            print(f"{num}不是质数")
            is_prime = False
            break
        i += 1
    if is_prime:
        print(f"{num}是质数")


# sum_singular()
# sum_seven()
# daffodils()
# Prime_num()
a = dict(([1, 2], [3, 4]))
print(a)
