#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/11/6 10:57
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------

import pandas as pd
import os


current_path = r'D:\test\gdzldj'
os.chdir(current_path)

excel_path = '耕地质量变更调查表.xls'
sheet = pd.read_excel(excel_path,sheet_name=1)
# 输出csv文件
# sheet.to_csv("data.csv", sep=",", index=False,encoding="cp936")
pH_des = sheet["pH"]
row = pH_des.std()
print(pH_des)
print(row)

import pandas as pd
import numpy as np

# 模拟数据
data = pd.DataFrame({'price': np.random.randn(1000),
                     'amount': 100*np.random.randn(1000)})

# 等分价格为10个区间
quartiles = pd.cut(data.price, 10)

# 定义聚合函数
def get_stats(group):
    return {'amount': group.sum()}

# 分组统计
grouped = data.amount.groupby(quartiles)
price_bucket_amount = grouped.apply(get_stats).unstack()
print("'''''''''''''''''''''''''''''''''''")
# print(grouped)
print(price_bucket_amount)