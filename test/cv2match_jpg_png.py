#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/8/19 13:21
# Reference:
"""
Description: 测试不同格式图片（png、jpg）之间的匹配
Usage:
"""
# ---------------------------------------------------------------------------
import cv2

# raw_jpg = "T2028.jpg"
# temp = "T2028_1.png"

raw_jpg = "1212.png"
temp = "1212_1.jpg"


raw_jpg = cv2.imread(raw_jpg,0)
temp = cv2.imread(temp,0)
res_array = cv2.matchTemplate(raw_jpg, temp, cv2.TM_CCOEFF_NORMED)
res = res_array.max()
print res