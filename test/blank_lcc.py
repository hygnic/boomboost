#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/7/27 16:33
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import cv2
import os
from DCcore import dcutility as dc

# image = r"G:\MoveOn\boomboost\image\spring\spring_house.png"
# cv2image = cv2.imread(image, 0)
#
#
# cropped = cv2image[0:128, 0:512] # 裁剪坐标为[y0:y1, x0:x1]
# # cv2.imwrite("./data/cut/cv_cut_thor.jpg", cropped)
#
#
#
# cv2.imshow("kk",cropped)
# cv2.waitKey(0)


os.chdir("../adb")
# os.system("adb connect 127.0.0.1:21501")
ims = dc.ImageMatchSet()
ims.capture_adb()