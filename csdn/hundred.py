# 尾数6前移，结果是原数的四倍
def end_first():
    for i in range(100, 1000000, 1):
        if 10 ** len(str(i)) * 6 + i == 4 * (i * 10 + 6):
            print(i * 10 + 6)


end_first()

