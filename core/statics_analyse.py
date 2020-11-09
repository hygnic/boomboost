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
import pathlib

current_path = r'D:\test\gdzldj'
os.chdir(current_path)

excel_path = '耕地质量变更调查表.xls'
sheet = pd.read_excel(excel_path,sheet_name=1)

