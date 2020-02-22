# 奇偶数判断
def exec_1():
    try:
        num = int(input("请输入一个任意整数："))
        print("输入的为奇数") if num % 2 == 1 else print("输入的是偶数")
    except BaseException:
        print("输入错误")


# 闰年判断
def leap_year():
    try:
        num = int(input("请输入一个四位数年份："))
        if num % 400 == 0 or (num % 4 == 0 and num % 100 != 0):
            print(f"{num}年是闰年")
        else:
            print(f"{num}年不是闰年")
    except BaseException:
        print("输入错误")


# 狗年龄转换
def dog_year():
    year_under_2 = 10.5
    year_over_2 = 4
    try:
        num = float(input("请输入狗的年龄："))
        if num <= 0:
            print("输入错误")
            return
        if num >= 2:
            age = (num - 2) * year_over_2 + 2 * year_under_2
        else:
            age = num * year_under_2
        print(f"狗的年龄相当于人类{age}岁")
    except BaseException:
        print("输入错误")


# 期末奖励
def exec_4():
    try:
        num = float(input("请输入小明期末成绩(0-100)："))
        if num > 100 or num < 0:
            print("输入错误")
            return
        if num == 100:
            print("奖励一辆宝马")
        elif num >= 80:
            print("奖励一台iphone")
        elif num >= 60:
            print("奖励一本参考书")
        else:
            print("什么都没有")
    except BaseException:
        print("输入错误")

# exec_1()
# leap_year()
# dog_year()
exec_4()