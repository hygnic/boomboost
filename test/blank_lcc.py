#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/7/27 16:33
# Reference: https://blog.csdn.net/zhonglunshun/article/details/78362439?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.channel_param
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import cv2
import os
import subprocess
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
# os.system("adb shell input keyevent 3") # back home
subprocess.Popen("adb shell input keyevent 3") # back home
# ims = dc.ImageMatchSet()
# ims.capture_adb()