# -*- coding: UTF-8 -*-


# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
def test_case_1():
    for i in (range(1, 5)):
        for j in range(1, 5):
            for k in range(1, 5):
                if i != j and j != k and k != i:
                    print(i, j, k)


# 数轴来分界，定位问题
def test_case_2():
    '''
    利润(I)低于或等于10万元时，奖金可提10%；
    利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
    20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
    60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成
    '''

    profit = int(input(f"请输入利润:"))
    gap = [1000000, 600000, 400000, 200000, 100000, 0]
    rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    result = 0
    for i in range(6):
        if profit > gap[i]:
            result += (profit - gap[i]) * rate[i]
            profit = gap[i]
    print(result)


# test_case_1()
test_case_2()
