#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/7/26 14:07
# Reference:
"""
Description: 自动刷图，角色等级满级后自动换上新角色，开始界面必须是小队配置界面！
Usage:
"""
# ---------------------------------------------------------------------------
import os
import time

from conf import DClocation
from dcutility import humanbeing_click
from dcutility import image_match
from dcutility import adb_back, get_randxy
from dcutility import ImageMatchSet


lt = DClocation.Location()
# image identification tool class
ims = ImageMatchSet()


def farm_setup():
	# to make sure all corrcet!
	os.chdir("../adb")
	# os.system("adb connect 127.0.0.1:21503")
	# make sure the screen is showing the battle configuration interface
	judgment_value, match_value = image_match(
			u"G:/MoveOn/boomboost/image/farm/select.png",0.7)
	print "0011 judgment_value:{} match_value:{}".format(judgment_value,
														 match_value)
	if judgment_value == 0:
		print "program exits"
		exit()
		
def farm():
	pass

def change_charactor():
	humanbeing_click(lt.fselectX,lt.fselectY)
	time.sleep(3)
	##################$$
	# 向左滑动
	x1,y1 = get_randxy((775,853),(511,672))
	x2 = x1-700
	y2 = y1
	# 最后一个数字 100 表示整个操作的耗时 单位：毫秒
	swipe = "adb shell input swipe {} {} {} {} 100".format(x1,y1,x2,y2)
	# os.system(swipe)
	# os.system(swipe)
	os.system(swipe)
	os.system(swipe)
	#######################
	# adb_back()
	image_match("G:/MoveOn/boomboost/image/farm/select.png")
	
	
if __name__ == '__main__':
	farm_setup()
	farm()
	change_charactor()