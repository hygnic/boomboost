#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/7/28 17:19
# Reference: https://amrbook.com/coding/python/automate-adb-with-python/
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import os
import time

# path for the adb which come with NOX emulator.
path = "C:\\Program Files (x86)\\Nox\\bin"

# Change the directory to it.
os.chdir(path)

# checking for connected devices
device = os.popen("adb devices").read().split('\n', 1)[1].split("device")[0].strip()

# connect to the selected device 172.0.0.1:62001
print("Waiting for connection ...")
connect = os.popen("adb connect " + device ).read()
print(connect)

#start Epic application
os.system("adb shell monkey -p com.getepic.Epic -c android.intent.category.LAUNCHER 1")

# select PARENTS button
time.sleep(3)
os.system("adb shell input tap 340 1030")

# swipe the page
time.sleep(5)
os.system("adb shell input tap 340 1030 340 650 100")

# press back key
os.system("adb shell input keyevent 4")