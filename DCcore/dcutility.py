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
from time import sleep
import random
import os
import cv2
import logging as lg  # TODO 设置其他颜色的日志输出未果
from conf import pathfile
from conf.DClocation import Location

pf = pathfile.Path()
lt = Location()
# 日志信息设置
lg.basicConfig(
	format="%(asctime)s >> %(funcName)s %(levelname)s: %(message)s",
	datefmt="%d-%m-%Y %H:%M:%S", level=lg.DEBUG)


def get_randxy(x, y):  # (570, 650),(240, 310)
	"""产生一个在x,y二维区域内的随机位置,x,y为两个元素的列表，变量范围"""
	xc = random.randint(x[0], x[1])
	yc = random.randint(y[0], y[1])
	print "x,y:", xc, yc
	return xc, yc


def sleeptime(a=0.5, b=1.6):
	"""产生a,b间的随机时间延迟"""
	delay = random.uniform(a, b)
	# print "delay time:", delay
	sleep(delay)


def humanbeing_click(x, y, a=0.2, b =0.6):
	"""
	根据给出的x范围和y范围来随机确定一个其中的点，然后完成点击任务
	:param x: (350, 439) 这是x取值范围
	:param y: (535, 566) 这是y取值范围
	:param a:
	:param b:
	:return:
	"""
	# combine get_randxy(x, y) and sleeptime()
	spring_x, spring_y = get_randxy(x, y)
	click = 'adb shell input tap {} {}'.format(spring_x, spring_y)
	sleeptime(a, b)
	os.system(click)

def humanbeing_click_point(click_point, a=0.2, b =0.6):
	"""
	# 根据指定的点, 拟人化完成adb点击任务
	:param click_point: （x,y）
	:param a: 延迟 秒
	:param b: 延迟 秒
	:return:
	"""
	click = 'adb shell input tap {} {}'.format(click_point[0], click_point[1])
	sleeptime(a, b)
	os.system(click)



def check_screen(match_method=cv2.TM_CCOEFF_NORMED):
	# 预处理，监测当前页面是否存在异常（是否退出界面和重连界面）
	screen_image = cv2.imread("../image/screen_img.png", 0)
	check1 = cv2.imread(pf.quit, 0)
	check2 = cv2.imread(pf.network_error, 0)
	result = cv2.matchTemplate(screen_image, check1, match_method)
	if result.max() > 0.8:
		# 询问退出 填否
		humanbeing_click(lt.no_quitX, lt.no_quitY)
		lg.debug(u"拒绝退出")
		sleep(1.5)
	result = cv2.matchTemplate(screen_image, check2, match_method)
	if result.max() > 0.8:
		# 询问网络问题，确认重连
		humanbeing_click(lt.reconnectX, lt.reconnectY)
		lg.debug(u"重连网络")
		sleep(5)


def image_match(temp, match_value, match_method=cv2.TM_CCOEFF_NORMED):
	"""
	temp(String\Unicode\List): 匹配标志(模板)图片地址
	match_value(Int\Float): 阈值 Threshold，cv2匹配结果大于阈值返回1
	screen(String): default value
	:return: 返回1或者0，以及一个图像识别匹配最大值
	"""
	# 发送图片
	cmd_get = "adb shell screencap -p /sdcard/screen_img.png"
	cmd_send = "adb pull sdcard/screen_img.png G:/MoveOn/boomboost/image"
	os.system(cmd_get)
	os.system(cmd_send)
	# 记录当前屏幕截图
	screen_image = cv2.imread("../image/screen_img.png", 0)
	
	if isinstance(temp, list):
		cv2images = []
		cv2match_result = []
		for i in temp:
			cv2images.append(cv2.imread(i, 0))
		for ii in cv2images:
			result = cv2.matchTemplate(screen_image, ii, match_method)
			cv2match_result.append(result.max())
		# 列表推导式 大于阈值的为1，小于阈值的为0
		judgement_result = [
			1 if i > match_value else 0 for i in cv2match_result]
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


def adb_back(a=0.1, b=0.3):
	# 自带延迟返回
	sleeptime(a, b)
	back_code = "adb shell input keyevent 4"
	os.system(back_code)


# class NewList(list):
# 	def __init__(self,num):
# 		list.__init__([])
# 		self.num = num
# 		slen = len(self)
# 		if slen>num:
# 			self = self[2:]
#
# 	def get_len(self):
# 		pass


class MatchTool(object):
	pf = pathfile.Path()
	
	def __init__(self, method):
		"""
		:param method:
			method usualy :cv2.TM_CCOEFF_NORMED
		"""
		self.method = method
		# cv2.imread 读取的屏幕截图组
		self.screenshots = [1,2,3,4]
		# 最小值的位置、最大值的位置、模板的高、模板的宽，由于我们使用cv2.TM_CCOEFF_NORMED算法，所以只有最大值的位置
		self.location_size = []  # [min_loc, max_loc, h, w]
		
	# use this function to call self.screenshots
	def return_screenshots(self):
		# limit the number of items within 4
		if len(self.screenshots)>3: # TODO 填3才会变成4，不管了，反正只有最后两张图片
			self.screenshots = self.screenshots[-3:]
		return self.screenshots
	
	def screencapture(self):
		# 使用adb内置截屏功能
		# 返回最新截屏的cv2读取数据
		cmd_get = "adb shell screencap -p /sdcard/screen_img.png"
		cmd_send = "adb pull sdcard/screen_img.png G:/MoveOn/boomboost/image"
		os.system(cmd_get)
		os.system(cmd_send)
		# 记录当前屏幕截图（cv2读取数据）
		screen_image = cv2.imread("../image/screen_img.png", 0)
		# 将截图（cv2读取数据）加入self.screenshots列表中
		screens = self.return_screenshots()
		screens.append(screen_image)
		return screen_image
	
	def back_to_main_menu(self):
		# return DC main menu(ongoing)
		sleeptime(1, 1.5)
		cv2value1, cv2real_value = image_match(self.pf.mian_flags, 0.8)
		if 1 not in cv2value1:
			print cv2real_value
			adb_back()
			self.back_to_main_menu()
	
	def image_match(self, temp, threshold=0.8):
		"""
		使用模板文件（temp）与当前屏幕进行实时匹配
		temp(String\Unicode\List): 匹配标志(模板)图片地址或者地址列表
		threshold(Int\Float): 阈值 Threshold，cv2匹配结果大于阈值返回1
		screen(String): default value
		:return: 返回1或者0，以及一个图像识别匹配最大值
		"""
		# get screencapture
		# 1.old method
		# cmd_get = "adb shell screencap -p /sdcard/screen_img.png"
		# cmd_send = "adb pull sdcard/screen_img.png G:/MoveOn/boomboost/image"
		# os.system(cmd_get)
		# os.system(cmd_send)
		# # 记录当前屏幕截图
		# screen_image = cv2.imread("../image/screen_img.png", 0)
		# 2.new method
		# 也可以使用 self.screen_image 来达到各个方法都能方面屏幕截图，
			# 但是可以用事先写好的 self.return_screenshots 获取最近的4张屏幕截图列表
		screen_image = self.screencapture()
		
		if isinstance(temp, list):
			cv2images = []
			cv2match_result = []
			for i in temp:
				cv2images.append(cv2.imread(i, 0))
			for ii in cv2images:
				result = cv2.matchTemplate(screen_image, ii, self.method)
				cv2match_result.append(result.max())
			# 列表推导式 大于阈值的为1，小于阈值的为0
			judgement_result = [
				1 if i > threshold else 0 for i in cv2match_result]
			# return list just like that: [1,0,1]
			return judgement_result, cv2match_result  # [1, 0, 1],[0.934, 0.349, 0.987]
		
		if isinstance(temp, str) or isinstance(temp, unicode):
			temp_image = cv2.imread(temp, 0)  # 只读取灰度图
			result1 = cv2.matchTemplate(screen_image, temp_image, self.method)
			result = result1.max()
			if result > threshold:
				# 显示图像
				self.matched_rectangle(temp_image, result1)
				return 1, result
			else:
				lg.debug("1104 not matched")
				# 显示图像
				self.matched_rectangle(temp_image, result1)
				return 0, result
			
	# 给匹配上的图形添加一个图框，同时显示一个内缩的图框，返回内缩图框中的一个点
	def matched_rectangle(self, cv2temp, result):
		""""""
		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
		
		# 获取模板文件的高和宽，h, w
		h, w = cv2temp.shape[:2]
		max_lefttop = max_loc
		max_rightbottom = (max_lefttop[0] + w, max_lefttop[1] + h)
		self.location_size = [min_loc, max_loc, h, w]
		
		lg.debug("max_lefttop:{}".format(max_lefttop))
		lg.debug("max_rightbottom:{}".format(max_rightbottom))
		
		current_screen = self.return_screenshots()[-1]
		# [255, 245, 152]  [196, 228, 255]
		cv2.rectangle(current_screen, max_lefttop, max_rightbottom, [255, 255, 255], 3)
		lg.debug("show screen detected")
		# cv2.resizeWindow("DC", 90, 100) # 改变大小，不是缩放
		# def show_iamge():
		# 	cv2.imshow("DC detected screen", current_screen)
		# 	# cv2.destroyAllWindows()
		# 	#  cv2.waitKey(0) 使opencv图像显示界面长期存在
		# 	cv2.waitKey(1)
		# show_iamge()
	
	def rectangle_point(self, zoom=0.25):
		"""
		直接在匹配上的区域内选择点，不用手动输入范围了
		如果缩放指数为0，则直接获取匹配上区域内一个点，如果不为0，则在缩放的区域内选择一个点返回
		zoom(Int):  zoom_factor 缩放减去的范围，相当于减少X%的高和宽, 越大缩小的越多
		:return:
		"""
		min_loc, max_loc, height, width = self.location_size
		max_lefttop = max_loc
		if zoom != 0:
			max_rightbottom = (max_lefttop[0] + width, max_lefttop[1] + height)
			# (x1,y1)是左上角的点，(x2,y2)是右下角的点，矩形内缩的话右上角的点值增加，右下角的点值减小
			x1 = max_lefttop[0]
			x2 = max_rightbottom[0]
			y1 = max_lefttop[1]
			y2 = max_rightbottom[1]
			# 进行内缩（负缓冲）操作
			xlength = x2 - x1
			ylength = y2 - y1
			reduce_xlength = int(xlength * zoom // 2)
			reduce_ylength = int(ylength * zoom // 2)
			# new point
			newx1 = x1 + reduce_xlength
			newy1 = y1 + reduce_ylength
			newx2 = x2 - reduce_xlength
			newy2 = y2 - reduce_ylength
			# 绘制缩小和的匹配图框
			cv2.rectangle(
				self.return_screenshots()[-1], (newx1,newy1), (newx2,newy2), [255, 255, 255], 2)
			# 随机获取缩小图框中的一个点
			random_point= self.get_randxy2((newx1, newx2), (newy1, newy2))
			lg.debug("xlength:{},ylength:{}".format(xlength, ylength))
			return random_point # (123,789)
		else: # zoom为0的情况，表示在不缩放的区域内选择一个点
			x = (max_lefttop[0],max_lefttop[0] + width)
			y = (max_lefttop[1],max_lefttop[1] + height)
			return self.get_randxy2(x,y)
		
	@staticmethod
	def get_randxy2(x, y):  # (570, 650),(240, 310)
		"""产生一个在x,y二维区域内的随机位置,x,y为两个元素的列表，变量范围"""
		xc = random.randint(x[0], x[1])
		yc = random.randint(y[0], y[1])
		# print "x,y:", xc, yc
		return xc, yc
	
	def show(self):
		# 显示图像以及识别的图框
		cv2.imshow("DC detected screen", self.return_screenshots()[-1])
		# cv2.destroyAllWindows()
		#  cv2.waitKey(0) 使opencv图像显示界面长期存在
		cv2.waitKey(1)
		



		
if __name__ == '__main__':
	os.chdir("../adb")
	# os.system("adb connect 127.0.0.1:21503")
	mt = MatchTool(cv2.TM_CCOEFF_NORMED)
	mt.image_match(ur"G:\MoveOn\boomboost\image\12.png",0.8)
	point = mt.rectangle_point(0.25)
	humanbeing_click_point(point)
	mt.show()
	sleeptime(2,3)

	
