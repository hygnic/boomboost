#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/8/13 14:29
# Reference: https://stackoverflow.com/questions/54878453/compress-adb-screencap-on-python
"""
Description:直接读取adb图像，简化截屏、拉取、读取的操作
Usage:
"""
# ---------------------------------------------------------------------------
import os
import time
import cv2
import numpy as np
import subprocess

os.chdir("../adb")


    

def timewrap(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print('Program time consuming: ',end - start)
    return inner


def timewrap_cpu(func):
    def inner():
        start = time.clock()
        func()
        end = time.clock()
        print('CPU time consuming: ',end - start)
    return inner



@timewrap
def read21():
    pipe = subprocess.Popen("adb shell screencap -p",
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE, shell=True)
    image_bytes = pipe.stdout.read().replace(b'\r\n', b'\n')
    image = cv2.imdecode(np.fromstring(image_bytes, np.uint8), 0)  # cv2.IMREAD_COLOR   1
    cv2.namedWindow("", cv2.WINDOW_NORMAL) # cv2.WINDOW_NORMAL 可修改窗口大小
    cv2.imshow("", image)
    cv2.waitKey(1000) # one second
    cv2.destroyWindow("")

@timewrap
def read11():
    cmd_get = "adb shell screencap -p /sdcard/screen_img.png"
    # cmd_get = "adb exec-out screencap -p > xxx.png"
    # cmd_get = "adb shell screencap -p | perl -pe 's/\x0D\x0A/\x0A/g' > screen.png"
    # cmd_get = "adb shell screencap -p | sed 's/^M$//' > screenshot.png"
    cmd_send = "adb pull sdcard/screen_img.png G:/MoveOn/boomboost/image"
    os.system(cmd_get)
    os.system(cmd_send)
    # 记录当前屏幕截图（cv2读取数据）
    screen_image = cv2.imread("../image/screen_img.png", 0)
    
        
        
if __name__ == '__main__':
    # for i in xrange(9):
        read21()
        # read11()
    