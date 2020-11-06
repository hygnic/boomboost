#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/11/3 23:02
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import numpy as np
import pandas as pd

df = pd.DataFrame({'one':[1,2,3,5],'two':[4,6,1,8]}) # 必须一样长
df = pd.DataFrame({'one':[1,2,3,5],'two':[4,6,1,8]},index=['a','b','c','d']) # 必须一样长
df2 = pd.DataFrame({'one':pd.Series([1,2,3,5]),'two':pd.Series([4,6,1])}) # 可以不一样长
df2 = pd.DataFrame({'one':pd.Series([1,2,3,5],index=['a','b','c','d']),'two':pd.Series([4,6,1],index=['a','b','c'])}) # 可以不一样长

ss = df.loc[['a','c'],:]
print(df)
print(df2)
print("=====================")
print(ss)