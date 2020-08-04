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

from conf import DClocation
from dcutility import humanbeing_click, humanbeing_click_point, sleeptime
from dcutility import screenswipe, cancel_selection
from dcutility import back
from dcutility import ImageMatchSet


lt = DClocation.Farm()
lt_gl = DClocation.General()
# image identification tool class
ims = ImageMatchSet()
# 获取战斗主界面
# main_interface = ims.capture()
# screenshot = ims.screenshots

# 初始，筛选角色星级
def initil():
	cancel_selection()
	time.sleep(0.6)
	# 选择两星的角色
	humanbeing_click(lt_gl.star2X, lt_gl.star2Y)
	back()


def check_level():
	"""levelmax  检查是否满级，如果满级，程序停止运行"""
	# 截取的 20 中的 罗马数字 0
	levelmax = "G:/MoveOn/boomboost/image/farm/levelmax.png"
	levelmax_screen = ims.capture_adb()
	levelmax_screen = levelmax_screen[
					  lt.croppedY[0]:lt.croppedY[1],
					  lt.croppedX[0]:lt.croppedX[1]
					  ]
	res = ims.image_match(levelmax, 0.8, levelmax_screen)
	print res[1]
	if res[0] == 1:
		print "LEVEL UP MAX!"
		sys.exit(0)

count = 1  # 计数，第一次战斗前需要修改角色筛选配置
def team_conf(vacancy):
	"""
	配置队伍，更换满级的角色
	vacancy(Int): 1-5 从右到左替换几位child
	return:
	"""
	global count
	humanbeing_click(lt.fselectX,lt.fselectY)
	# 第一次战斗前需要修改角色筛选配置
	if count == 1:
		initil()
	count+=1
	time.sleep(1)
	flag1 = "G:/MoveOn/boomboost/image/farm/flag1.png"
	flag_res = ims.image_match(flag1)
	if flag_res[0]==1:
		join = "G:/MoveOn/boomboost/image/farm/join_team.png"
		# 重复角色
		repeat = "G:/MoveOn/boomboost/image/farm/error1.png"
		screenswipe((775, 853), (511, 672),(75, 853), (120, 672))  # swipe screen
		time.sleep(1.5)
		
		# loop add child
		for i in xrange(vacancy):
			check_level()
			good = False
			while not good:
				humanbeing_click(lt.join_teamX,lt.join_teamY)
				time.sleep(0.6)
				repeat_res = ims.image_match(repeat)
				if repeat_res[0] == 1:  # 出现重复角色的问题
					# click back button
					humanbeing_click(lt.confirm_backX, lt.confirm_backY)
					# time.sleep(0.2)
					# click leftside child
					humanbeing_click(lt.leftsideX, lt.leftsideY)
					time.sleep(0.2)
				else:
					good =True
			# 将选择好的天子放到队伍中
			# 点击上面的位置
			one_position = lt.position[i]
			humanbeing_click(one_position[0], one_position[1])
			time.sleep(0.3)
		back()

def start(fist_time=False):
	"""
	从战斗配置主界面开始，进行连续战斗
	fist_time(Boolean): Ture>第一次，需要设置连续战斗方式；False> 不需要设置连续战斗方式
		鸡肋 实际发现 每次满级后更换角色都要重新选择连续战斗方式 所以直接设置成Ture
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
	start_button = "G:/MoveOn/boomboost/image/farm/start_button.png"
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
	fight_result_image = "G:/MoveOn/boomboost/image/farm/battle_result.png"
	fighting_res = ims.image_match(fight_result_image)
	if fighting_res[0] == 1:
		finish = True
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
	while True:
		team_conf(4)
		start(fist_time=True)
		fighting(160)