#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/7/26 0:26
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import time
import random
import os
import cv2
from conf import pathfile
from conf.DClocation import Location

pf = pathfile.Path()
lt =Location()

def get_randxy(x, y):  # (570, 650),(240, 310)
	"""产生一个在x,y二维区域内的随机位置,x,y为两个元素的列表，变量范围"""
	xc = random.randint(x[0], x[1])
	yc = random.randint(y[0], y[1])
	print "x,y:",xc,yc
	return xc,yc

def sleeptime(a=0.5, b=1.6):
	"""产生a,b间的随机时间延迟"""
	delay=random.uniform(a, b)
	print "delay time:",delay
	time.sleep(delay)

def humanbeing_click(x, y, a=0.5, b=1.6):
	# combine get_randxy(x, y) and sleeptime()
	spring_x, spring_y = get_randxy(x,y)
	click = 'adb shell input tap {} {}'.format(spring_x, spring_y)
	sleeptime(a, b)
	os.system(click)


def image_match(temp, match_value, match_method=cv2.TM_CCOEFF_NORMED):
	"""
	temp(String\Unicode\List\Tuple): 匹配标志(模板)图片地址
	match_value(Int\Float): 阈值 Threshold，cv2匹配结果大于阈值返回1
	screen(String): default value
	:return: 返回1或者0，以及一个图像识别匹配最大值
	"""
	# 发送图片
	cmd_get = "adb shell screencap -p /sdcard/screen_img.png"
	cmd_send = "adb pull sdcard/screen_img.png G:/MoveOn/boomboost/image"
	os.system(cmd_get)
	os.system(cmd_send)
	screen_image = cv2.imread("../image/screen_img.png", 0)
	# 预处理
	checks = [pf.quit, pf.network_error]
	check1 = cv2.imread(pf.quit, 0)
	check2 = cv2.imread(pf.network_error, 0)
	result = cv2.matchTemplate(screen_image, check1, match_method)
	if result.max() > 0.8:
		# 询问退出 填否
		humanbeing_click(lt.no_quitX, lt.no_quitY)
		time.sleep(1.2)
	result = cv2.matchTemplate(screen_image, check2, match_method)
	if result.max() > 0.8:
		# 询问网络问题，确认重连
		humanbeing_click(lt.reconnectX, lt.reconnectY)
		time.sleep(5)
	
	if isinstance(temp, list):
		cv2images = []
		cv2match_result = []
		for i in temp:
			cv2images.append(cv2.imread(i, 0))
		for ii in cv2images:
			result = cv2.matchTemplate(screen_image, ii, match_method)
			cv2match_result.append(result.max())
		# 列表推导式 大于阈值的为1，小于阈值的为0
		judgement_result = [1 if i > match_value else 0 for i in
							cv2match_result]
		# return list just like that: [1,0,1]
		return judgement_result, cv2match_result  # [1, 0, 1],[0.934, 0.349, 0.987]
	
	if isinstance(temp, str) or isinstance(temp, unicode):
		temp_image = cv2.imread(temp, 0)  # 只读取灰度图
		result = cv2.matchTemplate(screen_image, temp_image, match_method)
		result = result.max()
		if result > match_value:
			return 1, result
		else:
			return 0, result
		
def adb_back(a=0.1,b=0.3):
	# 自带延迟返回
	sleeptime(a,b)
	back_code = "adb shell input keyevent 4"
	os.system(back_code)

# 不用类 麻烦！
class MatchTool(object):
	pf = pathfile.Path()
	
	def __init__(self):
		print self.pf.mian_flags
	
	def back_to_main_menu(self):
		sleeptime(1,1.5)
		cv2value1,cv2real_value = image_match(self.pf.mian_flags,0.8)
		if 1 not in cv2value1:
			print cv2real_value
			adb_back()
			self.back_to_main_menu()
	
	def image_match(self,temp, match_value, match_method=cv2.TM_CCOEFF_NORMED):
		"""
		temp(String\Unicode\List\Tuple): 匹配标志(模板)图片地址
		match_value(Int\Float): 阈值 Threshold，cv2匹配结果大于阈值返回1
		screen(String): default value
		:return: 返回1或者0，以及一个图像识别匹配最大值
		"""
		# 发送图片
		cmd_get = "adb shell screencap -p /sdcard/screen_img.png"
		cmd_send = "adb pull sdcard/screen_img.png G:/MoveOn/boomboost/image"
		os.system(cmd_get)
		os.system(cmd_send)
		
		screen_image = cv2.imread("../image/screen_img.png", 0)
		# 预处理
		error=0
		checks = [self.pf.quit, self.pf.network_error]
		result = cv2.matchTemplate(screen_image, checks[0], match_method)
		if result > 0.8:
			error += 1
			# 询问退出 填否
			humanbeing_click(lt.no_quitX, lt.no_quitY)
			
		result = cv2.matchTemplate(screen_image, checks[1], match_method)
		if result > 0.8:
			error += 1
			# 询问网络问题，确认重连
			humanbeing_click(lt.reconnectX, lt.reconnectY)
		
		if isinstance(temp, list):
			cv2images = []
			cv2match_result = []
			for i in temp:
				cv2images.append(cv2.imread(i, 0))
			for ii in cv2images:
				result = cv2.matchTemplate(screen_image, ii, match_method)
				cv2match_result.append(result.max())
			# 列表推导式 大于阈值的为1，小于阈值的为0
			judgement_result = [1 if i > match_value else 0 for i in
								cv2match_result]
			# return list just like that: [1,0,1]
			return judgement_result, cv2match_result, error  # [1, 0, 1],[0.934, 0.349, 0.987]
		
		if isinstance(temp, str) or isinstance(temp, unicode):
			temp_image = cv2.imread(temp, 0)  # 只读取灰度图
			result = cv2.matchTemplate(screen_image, temp_image, match_method)
			result = result.max()
			if result > match_value:
				return 1, result,error
			else:
				return 0, result,error


if __name__ == '__main__':
	os.chdir("../adb")