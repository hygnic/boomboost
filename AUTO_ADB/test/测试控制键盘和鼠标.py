#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/7/21 18:02
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import pyautogui,time,sys
i=0
try:
	while i < 10:
		pyautogui.click(1015,362,clicks=2,button='left')
		time.sleep(1)
		pyautogui.click(1282,226,clicks=1,button='left')
		time.sleep(1)
		pyautogui.click(1102,160,clicks=2,button='left')
		time.sleep(3)
		i=i+1
	while i % 5 == 0:
		pyautogui.click(1015,362,clicks=2,button='left')
		break
except KeyboardInterrupt:
	sys.exit(0)