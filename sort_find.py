import random
import time


# 冒泡排序
def bubbleSort(test_list):
    if len(test_list) <= 0:
        return
    for i in range(len(test_list)):
        no_change = False
        for j in range(len(test_list) - i - 1):
            if (test_list[j]) > test_list[j + 1]:
                test_list[j], test_list[j + 1] = test_list[j + 1], test_list[j]
                no_change = True
        if not no_change:
            break
    return test_list


# 插入排序
def insertSort(test_list):
    if len(test_list) <= 0:
        return
    for i in range(len(test_list)):
        tmp = test_list[i]
        j = i - 1
        while j >= 0:
            if test_list[j] > tmp:
                test_list[j + 1] = test_list[j]
            else:
                break
            j -= 1
        test_list[j + 1] = tmp
    return test_list


# 快速排序
def quickSort(test_list, p, r):
    if p >= r:
        return
    q = partition(test_list, p, r)
    quickSort(test_list, p, q - 1)
    quickSort(test_list, q + 1, r)
    return test_list


# 快速排序-寻找分区点
def partition(test_list, p, r):
    pivot = test_list[r]
    i = j = p
    while j <= r - 1:
        if test_list[j] < pivot:
            tmp = test_list[i]
            test_list[i] = test_list[j]
            test_list[j] = tmp
            i += 1
        j += 1
    tmp = test_list[i]
    test_list[i] = test_list[r]
    test_list[r] = tmp
    return i


# 二分查找（第一个给定的数字）
def two_find(find_list, value):
    low = 0
    high = len(find_list) - 1
    while low <= high:
        mid = int(low + (high - low) / 2)
        if find_list[mid] > value:
            high = mid - 1
        elif find_list[mid] < value:
            low = mid + 1
        else:
            if mid == 0 or find_list[mid - 1] != value:
                return mid
            else:
                high = mid - 1
    return False


if __name__ == '__main__':
    # tmp_list = [int(random.random() * 99) for _ in range(5000)]
    #
    # start = time.time()
    # test_list = tmp_list.copy()
    # bubble_res = bubbleSort(test_list)
    # print(f'冒泡排序后{bubble_res}')
    # end = time.time()
    # print(end - start)
    #
    # start1 = time.time()
    # test_list1 = tmp_list.copy()
    # insert_res = insertSort(test_list1)
    # print(f'插入排序后{insert_res}')
    # end1 = time.time()
    # print(end1 - start1)
    #
    # start2 = time.time()
    # test_list2 = tmp_list.copy()
    # quick_res = quickSort(test_list2, 0, len(test_list2) - 1)
    # print(f'快速排序后{quick_res}')
    # end2 = time.time()
    # print(end2 - start2)
    #
    # assert bubble_res == insert_res
    # assert insert_res == quick_res

    find_list = [1, 3, 4, 4, 4, 4, 4, 4, 11, 18]
    print(two_find(find_list, 4))
