#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/7/25 22:12
# Reference:
"""
Description: # DC 温泉操作
Usage:
"""
# ---------------------------------------------------------------------------
import os
import time
from conf import DClocation,pathfile
from dcutility import humanbeing_click
from dcutility import image_match,sleeptime,back
pf = pathfile.Path()
lt = DClocation.Spring()

def mian():
	os.chdir("../adb")
	# c从主界面开始
	cv2value1, cv2real_value = image_match(pf.mian_flags, 0.8)
	if 1 not in cv2value1:
		print u"请从主界面开始"
		exit()
	# 点击夜世界
	humanbeing_click(lt.nightwordX, lt.nightwordY)
	time.sleep(2)
	humanbeing_click(lt.menu_springX, lt.menu_springY)
	time.sleep(3)
	judgment_value, match_value = image_match(
		u"G:/MoveOn/boomboost/image/spring/flag1.png",0.7)
	if judgment_value == 1:
		print "0001 judgment_value:{} match_value:{}".format(judgment_value,match_value)
		for i in lt.spring_house:
			replace_towels(i[0], i[0])
	else:
		print "\npostion1 not matched!"
		
def replace_towels(housex, housey):
	# 点击温泉是哪一楼
	# humanbeing_click(lt.spring2fX, lt.spring2fY) # 点击浴场的位置
	time.sleep(3)
	humanbeing_click(housex, housey)  # 点击浴场的位置
	time.sleep(5)
	# 进入泡温泉界面
	humanbeing_click(lt.enter_hotspringX, lt.enter_hotspringY)
	time.sleep(8)
	judgment_value, match_value = image_match(
		u"G:/MoveOn/boomboost/image/spring/flag2.png", 0.8)
	if judgment_value == 1: # 有感叹号，可以进行收获！
		print "0002 judgment_value:{} match_value:{}".format(judgment_value,match_value)
		print "!"
		# click ! 点击右上角的感叹号
		humanbeing_click(lt.end_spaX, lt.end_spaY)
		# 加速点击
		humanbeing_click(lt.spring_skipX, lt.spring_skipY, a=0.5, b=0.7)
		time.sleep(4)
		
		two_condition = [
			u"G:/MoveOn/boomboost/image/spring/change_towel.png",
			u"G:/MoveOn/boomboost/image/spring/levelup.png",
		]
		for i in [0,1,2,3,4]: # 循环五次
			res,real_res = image_match(two_condition, 0.8)
			time.sleep(2)
			# 加速点击
			humanbeing_click(lt.spring_skipX, lt.spring_skipY, a=0.5, b=0.7)
			if res[0] == 1: # not levelup
				humanbeing_click(lt.change_towelX, lt.change_towelY)
			elif res[1] == 1: # leveluped
				os.system("adb shell input keyevent 4") # back tap
				time.sleep(5)
				humanbeing_click(lt.change_towelX, lt.change_towelY)
			else:
				print u"0005 有问题，温泉"
			time.sleep(8)
			
			# re1,re2 = image_match(ur"G:\MoveOn\boomboost\image\spring\after_spa.png",0.85)
			humanbeing_click(lt.after_spaX, lt.after_spaY)
			time.sleep(1)
			back()
			time.sleep(5)
	
	else:
		print "no !"
		back() # 没有感叹号，返回房子那里
		time.sleep(5)
	

	
if __name__ == '__main__':
	mian()