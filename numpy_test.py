#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np


persontype = np.dtype({
    'names': ['name', 'chinese', 'math', 'english'],
    'formats': ['S32', 'i', 'i', 'i']})
peoples = np.array([("zhangfei", 66, 65, 30), ("guanyu", 95, 85, 98),
                    ("zhaoyun", 93, 92, 96), ("huangzhong", 90, 88, 77), ('dianwei', 80, 90, 90)],
                   dtype=persontype)
chineses = peoples[:]['chinese']
maths = peoples[:]['math']
englishs = peoples[:]['english']
print(f'语文平均成绩为{np.mean(chineses)}分')
print(f'数学平均成绩为{np.mean(maths)}分')
print(f'英语平均成绩为{np.mean(englishs)}分')

print(f'语文最小成绩为{np.amin(chineses)}分')
print(f'数学最小成绩为{np.amin(maths)}分')
print(f'英语最小成绩为{np.amin(englishs)}分')

print(f'语文最大成绩为{np.amax(chineses)}分')
print(f'数学最大成绩为{np.amax(maths)}分')
print(f'英语最大成绩为{np.amax(englishs)}分')

print(f'语文标准差为{np.std(chineses)}')
print(f'数学标准差为{np.std(maths)}')
print(f'英语标准差为{np.std(englishs)}')

print(f'语文方差为{np.var(chineses)}')
print(f'数学方差为{np.var(maths)}')
print(f'英语方差为{np.var(englishs)}')

print(sorted(chineses + maths + englishs, reverse=True))
print(np.sum(peoples))