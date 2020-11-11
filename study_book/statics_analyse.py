#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/11/9 16:45
# Reference:
"""
Description: 对耕地质量等级点位表进行分析统计、绘图
Usage:
"""
# ---------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import os

current_path = '.'
os.chdir(current_path)

excel_path = '耕地质量变更调查表.xls'
sheet = pd.read_excel(excel_path,sheet_name=0)
col_names = ['pH','有机质','土壤容重','有效磷','速效钾']
target_data = pd.DataFrame(sheet,columns = col_names)
"""
      pH   有机质  土壤容重   有效磷  速效钾
0    7.1  64.0  1.04  38.7  310
1    7.8  68.6  1.08  82.6  284
2    8.1  42.7  1.10  30.8   63
3    8.0  40.5  0.92  26.4  100
4    7.7  38.8  1.34  62.8  118
..   ...   ...   ...   ...  ...
"""

target_data = target_data.describe()
"""
               pH         有机质        土壤容重         有效磷         速效钾
count  133.000000  133.000000  133.000000  133.000000  133.000000
mean     7.658647   41.115789    1.370376   24.930075  189.661654
std      0.739075   14.504361    0.147589   21.849274   82.606028
min      5.000000   11.100000    0.920000    2.200000   49.000000
25%      7.400000   29.600000    1.270000    8.800000  127.000000
50%      7.800000   41.300000    1.370000   18.200000  173.000000
75%      8.100000   50.200000    1.470000   31.300000  250.000000
max      8.900000   80.000000    1.690000   92.600000  350.000000
"""

target_data = target_data.reindex(['min','max','50%','mean','std'])
target_data = target_data.rename(index={'min':'最小值','max':'最大值','50%':'中位数','mean':'平均值','std':'标准差'})
print(target_data.round())
target_data.round().to_csv("data.csv", sep=",", index=True,encoding="cp936")