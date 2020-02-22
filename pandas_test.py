import pandas as pd
from pandas import Series, DataFrame

food = DataFrame(pd.read_excel('food.xlsx'))

# 转换小写
food['food'] = food['food'].str.lower()

# 绝对值
food['ounces'] = food['ounces'].abs()

# 均值填充空值
food['ounces'].fillna(food['ounces'].mean(), inplace=True)

# 删除重复值
food.drop_duplicates(['food'], inplace=True)

print(food)
