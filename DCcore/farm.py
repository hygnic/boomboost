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
import sys
import time
import random
import cv2

from conf import DClocation
from dcutility import humanbeing_click,humanbeing_click_point,sleeptime
from dcutility import image_match
from dcutility import back, get_randxy
from dcutility import ImageMatchSet


lt = DClocation.Farm()
# image identification tool class
ims = ImageMatchSet()
# 获取战斗主界面
# main_interface = ims.capture()
# screenshot = ims.screenshots

def farm_setup():
	# to make sure all corrcet!
	os.chdir("../adb")
	# os.system("adb connect 127.0.0.1:21503")
	# make sure the screen is showing the battle configuration interface
	
		
def farm():
	pass

def team_conf(vacancy):
	"""
	配置队伍，更换满级的角色
	vacancy(Int): 1-5 从右到左替换几位child
	return:
	"""

	# humanbeing_click(lt.fselectX,lt.fselectY)
	time.sleep(1)
	flag1 = "G:/MoveOn/boomboost/image/farm/flag1.png"
	flag_res = ims.image_match(flag1)
	if flag_res[0]==1:
		
		
		join = "G:/MoveOn/boomboost/image/farm/join_team.png"
		# 重复角色
		repeat = "G:/MoveOn/boomboost/image/farm/error1.png"
		
		def screenswipe():
			# 向左滑动
			x1, y1 = get_randxy((775, 853), (511, 672))
			x2 = x1 - 700
			y2 = y1
			# 最后一个数字 100 表示整个操作的耗时 单位：毫秒
			# swipe = "adb shell input swipe {} {} {} {} 100".format(474,615,100,615)
			swipe = "adb shell input swipe {} {} {} {} 100".format(x1, y1, x2,
																   y2)
			for screenswipe_time in xrange(0, random.randint(3, 5)):  # 滑动3到5次
				os.system(swipe)
				sleeptime(0.1, 0.4)
		
		def check_level():
			# levelmax , 检查是否满级，如果满级，程序停止运行
			levelmax = "G:/MoveOn/boomboost/image/farm/levelmax.png"
			levelmax_screen = ims.capture()
			levelmax_screen = levelmax_screen[
							  lt.croppedY[0]:lt.croppedY[1],
							  lt.croppedX[0]:lt.croppedX[1]
							  ]
			res = ims.image_match(levelmax,0.8,levelmax_screen)[0]
			if res == 1:
				print "LEVEL UP MAX!"
				sys.exit(0)
		
		screenswipe()  # swipe screen
		# loop add child
		for i in xrange(vacancy):
			check_level()
			humanbeing_click(lt.join_teamX,lt.join_teamY)
			time.sleep(0.2)
			repeat_res = ims.image_match(repeat)
			if repeat_res[0] == 1:  # 出现重复角色的问题
				time.sleep(0.1)
				# click back button
				humanbeing_click(lt.confirm_backX, lt.confirm_backY)
				time.sleep(0.2)
				# click leftside child
				humanbeing_click(lt.leftsideX, lt.leftsideY)
				time.sleep(0.2)
				# click join button
				humanbeing_click(lt.join_teamX, lt.join_teamY)
			# 将选择好的天子放到队伍中
			time.sleep(0.2)
			one_position = lt.position[i]
			humanbeing_click(one_position[0], one_position[1])
			time.sleep(0.2)
		back()

def start(fist_time=False):
	"""
	从战斗配置主界面开始，进行连续战斗
	fist_time(Boolean): Ture>第一次，需要设置连续战斗方式；False> 不需要设置连续战斗方式
	"""
	time.sleep(0.3)
	# 配置自动战斗系统
	if fist_time: # 第一次配置连续战斗界面
		auto_button= "G:/MoveOn/boomboost/image/farm/auto.png"
		res = ims.image_match(auto_button, 0.85)[0]
		if res ==1:
			# 进入连续战斗设置界面
			point = ims.point()
			humanbeing_click_point(point)
			time.sleep(0.2)
			humanbeing_click(lt.loopX,lt.loopY)
			back()
	sleeptime(0.2, 0.51)
	# 匹配开始按键 如果必要，匹配loading（转圈圈那个图案）
	start_button = "xx"
	res = ims.image_match(start_button)[0]
	if res == 1:
		sleeptime(0.3, 0.7)
		humanbeing_click_point(ims.point(0.1))
		
	
	
def fighting(second):
	"""
	second(Int): 预估战斗结束需要的时间
	:return:
	"""
	finish = False
	time.sleep(second)
	fight_result_image = "xxx"
	fighting_res = ims.image_match(fight_result_image)
	if fighting_res[0] == 1:
		finish = True
		humanbeing_click("xx","yy")
	else: # 战斗未结束
		while not finish:
			sleeptime(5, 10)
			fighting_res = ims.image_match(fight_result_image)
			if fighting_res[0] == 1:
				finish = True
	back()
	
	
	



if __name__ == '__main__':
	os.chdir("../adb")
	# os.system("adb connect 127.0.0.1:21503")
	# farm_setup()
	# farm()
	team_conf(3)
	start(fist_time=True)