#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/11/3 20:15
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import random
import numpy as np

li = [random.randint(100,200) for _ in range(50)]
a = np.array(li) # 转化为数组对象
a5 = a*5

li2 = [random.randint(23,60) for _ in range(50)]
b = np.array(li2)
axb = a*b

"""=========================================================================="""
"""=========================================================================="""
print(a5)
print(axb)

bb = np.arange(34)
bb2 = bb[(bb>10) & (bb%2==0)]

print(bb2)
