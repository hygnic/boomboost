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
# from __future__ import absolute_import
from time import sleep
import time
import random
import os
import sys
import subprocess
import numpy as np
from matplotlib import pyplot as plt
import cv2
import logging as log  # TODO 设置其他颜色的日志输出未果
from AUTO_ADB.conf.DClocation import General
from AUTO_ADB.conf import pathfile
from AUTO_ADB.conf.DClocation import Spring


image_pf = pathfile.Path() # 部分配置的图片地址信息 #TODO 我也不知道是哪里的
image_g = pathfile.ImageDCGeneral() # 通用配置的图片地址信息

lt_sp = Spring()  # 温泉位置位置信息 #TODO 之后删除这个
lt_gl = General()  # 位置信息


# 日志信息设置
def log_settin(level): # dc.log_settin(log.debug)
	log.basicConfig(
		format="%(asctime)s >> %(funcName)s %(levelname)s: %(message)s",
		datefmt="%d-%m-%Y %H:%M:%S", level=level)

# 装饰函数 计算程序运行时间
def timewrap(func):
	def inner():
		start = time.time()
		func()
		end = time.time()
		print('Program time consuming: ',end - start)
	return inner

# 装饰函数 计算CPU执行时间
def timewrap_cpu(func):
	def inner():
		start = time.clock()
		func()
		end = time.clock()
		print('CPU time consuming: ',end - start)
	return inner

def get_randxy(x, y):  # (570, 650),(240, 310)
	"""产生一个在x,y二维区域内的随机位置,x,y为两个元素的列表，变量范围"""
	xc = random.randint(x[0], x[1])
	yc = random.randint(y[0], y[1])
	return xc, yc

def screenswipe(rx, ry, rx2, ry2):
	# 向左滑动
	# x1, y1 = get_randxy((775, 853), (511, 672))
	# x2, y2 = get_randxy((75, 853), (120, 672))
	
	x1, y1 = get_randxy(rx, ry)
	x2, y2 = get_randxy(rx2, ry2)
	# 毫秒 随机
	millisecond = random.randint(86, 101)
	# 最后一个数字 100 表示整个操作的耗时 单位：毫秒
	# swipe = "adb shell input swipe {} {} {} {} 100".format(474,615,100,615)
	swipe = "adb shell input swipe {} {} {} {} {}".format(x1, y1, x2,
														   y2,millisecond)
	for screenswipe_time in xrange(0, random.randint(3, 5)):  # 滑动3到5次
		os.system(swipe)
		sleeptime(0.6, 0.8)


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
	check1 = cv2.imread(image_pf.quit, 0)
	check2 = cv2.imread(image_pf.network_error, 0)
	result = cv2.matchTemplate(screen_image, check1, match_method)
	if result.max() > 0.8:
		# 询问退出 填否
		humanbeing_click(lt_sp.no_quitX, lt_sp.no_quitY)
		log.debug(u"拒绝退出")
		sleep(1.5)
	result = cv2.matchTemplate(screen_image, check2, match_method)
	if result.max() > 0.8:
		# 询问网络问题，确认重连
		humanbeing_click(lt_sp.reconnectX, lt_sp.reconnectY)
		log.debug(u"重连网络")
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


def back(a=0.1, b=0.3):
	# 自带延迟返回
	sleeptime(a, b)
	back_code = "adb shell input keyevent 4"
	subprocess.Popen(back_code)
	log.debug("call Android Back")
	# print "call Android Back"
	
# back home
def home_adb():
	subprocess.Popen("adb shell input keyevent 3")

class ImageMatchSet(object):
	image_pf = pathfile.Path()
	
	def __init__(self, method = cv2.TM_CCOEFF_NORMED):
		"""
		:param method:
			method usualy :cv2.TM_CCOEFF_NORMED
		"""
		self.method = method
		# cv2.imread 读取的屏幕截图组
		self.__screenshots = [1, 2, 3, 4]
		# 最小值的位置、最大值的位置、模板的高、模板的宽，由于我们使用cv2.TM_CCOEFF_NORMED算法，所以只有最大值的位置
		self.location_size = []  # [min_loc, max_loc, h, w]
		self.count = 0 # 用于 whileset 循环计数，实现超过次数后关闭程序
		
	# use this function to call self.__screenshots
	
	@property
	def screenshots(self):
		"""
		limit the number of screenshots within 4
		warn:The reason why not use self.__screenshots directly is to make sure the
		screenshots list within 4 or less item.
		:return: last 4 screenshot picture
		"""
		if len(self.__screenshots)>=4:
			self.__screenshots = self.__screenshots[-4:]
		return self.__screenshots
	
	def pullimage_adb(self):
		"""
		使用adb内置截屏功能，在安卓端生成png图片然后拉取到本地读取信息，加入self.__screenshots中
		:return: 返回最新截屏的cv2读取数据
		"""
		cmd_get = "adb shell screencap -p /sdcard/screen_img.png"
		cmd_send = "adb pull sdcard/screen_img.png G:/MoveOn/boomboost/image"
		os.system(cmd_get)
		os.system(cmd_send)
		# 记录当前屏幕截图（cv2读取数据）
		screen_image = cv2.imread("../image/screen_img.png", 0)
		self.screenshots.append(screen_image)
		return screen_image
		
	def capture_adb(self):
		"""
		使用adb内置截屏功能，直接读取当前屏幕信息，然后将截屏图片加入self.__screenshots中
		:return: 返回最新截屏的cv2读取数据
		"""
		pipe = subprocess.Popen("adb shell screencap -p",
								stdin=subprocess.PIPE,
								stdout=subprocess.PIPE, shell=True)
		# 安卓二进制和Windows有细小差别
		image_bytes = pipe.stdout.read().replace(b'\r\n', b'\n')
		screen_image = cv2.imdecode(np.fromstring(image_bytes, np.uint8),
							 0)  # cv2.IMREAD_COLOR   1
		# 将截图（cv2读取数据）加入self.screenshots列表中
		self.screenshots.append(screen_image)
		return screen_image
	
	def backhome(self, backs, sec=0.8):
		"""
		return DC main menu
		backs(Int): 返回次数
		sec(Float): time second
		:return:
		"""
		for i in xrange(backs-1):
			sleep(sec)
			back()
		# 循环监测，循环back
		self.whileset(image_g.quit, loop=True, func=back)
		humanbeing_click(lt_gl.noX, lt_gl.noY)
	
	def image_match(self, temp, threshold=0.8, screen_image=None):
		"""
		使用模板文件（temp）与当前屏幕进行实时匹配
		temp(String\Unicode\List): 匹配标志(模板)图片地址或者地址列表
		screen_image(cv2.imread): 与模板比较的cv2图片数据，如果不指定，截取当前屏幕
		threshold(Int\Float): 阈值 Threshold，cv2匹配结果大于阈值返回1
		screen(String): default value
		return:
			模板是单个文件（String\Unicode）:返回1或者0，以及一个图像识别匹配最大值
		"""
		# if not assign screen_image, function self.capture() assign to screen_image
		if screen_image is None:
			screen_image = self.capture_adb()
		if isinstance(temp, list): # 这个基本没有使用，没有更新
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
			self.result_array = cv2.matchTemplate(screen_image, temp_image, self.method)
			result = self.result_array.max()
			if result > threshold:
				# 显示图像
				self.rectangle(temp_image, self.result_array)
				return 1, result
			else:
				log.warn("<1104> <{}> not matched!".format(temp))
				# 显示图像
				self.rectangle(temp_image, self.result_array)
				return 0, result
			
	def rectangle(self, cv2temp, result):
		"""
		添加一个图框，不用手动，与self.image_match()方法绑定
		:param cv2temp: 模板文件
		:param result: 匹配结果
		:return:
		"""
		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
		# 获取模板文件的高和宽，h, w
		h, w = cv2temp.shape[:2]
		max_lefttop = max_loc
		max_rightbottom = (max_lefttop[0] + w, max_lefttop[1] + h)
		# 将模板数据保存于 self.location_size，可以全局共享
		self.location_size = [min_loc, max_loc, h, w]
		
		# log.debug("max_lefttop:{}".format(max_lefttop))
		# log.debug("max_rightbottom:{}".format(max_rightbottom))
		
		current_screen = self.screenshots[-1]
		cv2.rectangle(current_screen, max_lefttop, max_rightbottom, [255, 255, 255], 3)
	
	# @dc.timewrap
	def image_match_SIFT(self, temp, threhold=0.7, screen_image=None, show=False):
		"""基于FLANN的匹配器(FLANN based Matcher)定位图片
		temp(String/Unicode): 匹配模板，地址
		threhold:
		target_image(cv2.imread): 通过cv2.imread读取的与模板相比较的图片数据，如果不指定，截取当前屏幕
		:return:
		"""
		# Image Identification
		# template = cv2.imread('template_adjust.jpg', 0)  # queryImage
		# target = cv2.imread('target.jpg', 0)  # trainImage
		if screen_image is None: # get screenshot(cv2.imread)
			screen_image = self.capture_adb()
		template = cv2.imread(temp, 0)  # queryImage '1212_1_0.5size.jpg'
		target = screen_image  # trainImage '1212.png'
		# target = cv2.imread(target_image, 0)
		
		# Initiate SIFT detector创建sift检测器
		sift = cv2.xfeatures2d.SIFT_create()
		# find the keypoints and descriptors with SIFT
		kp1, des1 = sift.detectAndCompute(template, None)
		kp2, des2 = sift.detectAndCompute(target, None)
		# 创建设置 FLANN 匹配
		FLANN_INDEX_KDTREE = 0
		index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
		search_params = dict(checks=50)
		flann = cv2.FlannBasedMatcher(index_params, search_params)
		matches = flann.knnMatch(des1, des2, k=2)
		# store all the good matches as per Lowe's ratio test.
		good = []
		# 舍弃大于0.7的匹配
		for m, n in matches:
			if m.distance < 0.7 * n.distance:
				good.append(m)
		
		print len(good)
		MIN_MATCH_COUNT = 10  # 设置最低特征点匹配数量为10
		if len(good) > MIN_MATCH_COUNT: # 大于最低特征点匹配数量时才绘制匹配框
			# 获取关键点的坐标
			src_pts = np.float32(
				[kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
			dst_pts = np.float32(
				[kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2)
			# 计算变换矩阵和MASK
			M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
			matchesMask = mask.ravel().tolist()
			h, w = template.shape
			# 使用得到的变换矩阵对原图像的四个角进行变换，获得在目标图像上对应的坐标
			pts = np.float32(
				[[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(
				-1, 1, 2)
			dst = cv2.perspectiveTransform(pts, M)
			cv2.polylines(target, [np.int32(dst)], True, [255, 255, 255], 5,
						  cv2.LINE_8)  # 绘制矩形
			print [np.int32(dst)]
			# [array([[[ 387,  746]],[[ 387, 1081]],[[ 727, 1081]],[[ 727,  746]]])]
		else:
			print("Not enough matches are found - %d/%d" % (
			len(good), MIN_MATCH_COUNT))
			matchesMask = None
		# show match result graphically
		if show:
			draw_params = dict(matchColor=(0, 255, 0),
							   singlePointColor=None,
							   matchesMask=matchesMask,
							   flags=2)
			result = cv2.drawMatches(template, kp1, target, kp2, good, None,
									 **draw_params)
			plt.imshow(result, 'gray')
			plt.show()
	
	# 在图框区域选一个点
	def point(self, zoom=0.25, x_add=0, y_add =0):
		"""
		直接在匹配上的区域内选择点，不用手动输入范围了
		如果缩放指数为0，则直接获取匹配上区域内一个点，如果不为0，则在缩放的区域内选择一个点返回
		zoom(Int):  zoom_factor 缩放减去的范围，相当于减少X%的高和宽, 越大缩小的越多
		x_add(Float): 在某个偏移距离内的方形中选取点
		y_add(Float): 在某个偏移距离内的方形中选取点
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
			# 绘制缩小的匹配图框
			cv2.rectangle(
				self.screenshots[-1], (newx1, newy1), (newx2, newy2), [255, 255, 255], 2)
			# 随机获取缩小图框中的一个点
			random_point= self.get_randxy2(
				(newx1+x_add, newx2+x_add), (newy1+y_add, newy2+y_add)
			)
			# log.debug("xlength:{},ylength:{}".format(xlength, ylength))
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
	
	def show(self, para):
		"""
		显示图像以及识别的图框
		para(Int): cv2.waitKey(0) 使opencv图像显示界面长期存在，其余数字表示显示多少秒
		"""
		cv2.imshow("DC detected screen", self.screenshots[-1])
		# cv2.destroyAllWindows()
		#  cv2.waitKey(0)
		cv2.waitKey(para)
		
	@property
	def loopcount(self):
		return self.count
	
	def loopout(self, shutdown=True, count=26):
		"""循环匹配次数超过限制时，触发该方法"""
		if self.count >= count:
			if shutdown:
				home_adb()
			sys.exit("<<loop out>>")
	
	def whileset(self, image, a=4, b=6, threshold=0.8, loop = True, func = None):
		"""循环等待，直到最新的屏幕内容与图片匹配成功，退出
		image(Str/Unicode/List): 需要匹配的图片的地址，也可以是列表
		a b(Second): 等待时间的范围（sec）
		loop(Boolean): whether loop if match fail; Defualt Ture
		func(Function): 未匹配成功时启动该函数 默认无功能函数
		:returns: break loop if match fail when set loop=False, return 0
		"""
		self.count = 0
		if isinstance(image, list):
			finish = False
			while not finish:
				self.count += 1
				self.loopout() # 循环匹配次数超过限制时，结束app，结束程序
				sleeptime(a, b)
				for i in image:
					whileset_res1 = self.image_match(i,threshold=threshold)
					# whileset_res2 = self.image_match(
					# 	i, threshold=0.8, screen_image=self.__screenshots[-1])[0]
					if whileset_res1[0] == 1:
						finish = True
						break
					else:
						# print whileset_res1[1]
						log.debug("{} [whileset] not complete {} times".format(image,self.count))
						if func:
							func()
						if not loop:
							return 0
			print "Image: '{}' matched!".format(image)
		else: # 单个图片
			finish = False
			while not finish:
				self.count += 1
				self.loopout() # 循环匹配次数超过限制时，结束app，结束程序
				sleeptime(a, b)
				whileset_res = self.image_match(image, threshold=threshold)
				if whileset_res[0] == 1:
					finish = True
				else:
					log.debug("{} [whileset] not complete {} times".format(image,self.count))
					if func:
						func()
					if not loop:
						return 0
			print "Image: '{}' matched!".format(image)
		
	def backtopage(self, flag, a=1.4, b=1.6):
		"""
		返回到有标志物（参照）的界面
		flag(String\Unicode): 标志物（参照）图片地址
		"""
		back()
		sleeptime(a, b)
		flag_res = self.image_match(flag, 0.89)[0]
		if flag_res == 0:
			self.backtopage(flag)
		# else:
		# 	print "Back to flag: '{}' page successed!".format(flag)
			
			
			
			
			
			
			
""">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""
""">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""
""">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""
""">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""
""">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""
""">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""
ims = ImageMatchSet()


def cancel_selection():
	"""
	1.取消所有筛选条件，然后停留在筛选界面
	2.进入排序界面，自动选择第二种降序排列
	"""
	humanbeing_click(lt_gl.filterX, lt_gl.filterY)
	sleeptime(0.76, 1.1)
	selected = True
	while selected:
		res = ims.image_match(image_g.selcted, 0.85)
		if res[0] == 1:
			humanbeing_click_point(ims.point(0.1, 70), 0.1, 0.25)
		else:  # 全部取消完成
			selected = False
			print "dc_general.py: cancel all selection!"
	
	"""
	# # 进行排序
	# dc.humanbeing_click(lt_gl.sortX, lt_gl.sortY)
	# dc.sleep(0.5)
	# dc.humanbeing_click(lt_gl.sort1X, lt_gl.sort1Y,0.1,0.2)
	# dc.humanbeing_click(lt_gl.sort2X, lt_gl.sort2Y,0.06, 0.12)
	"""

def auto_hide(flag):
	"""在队伍配置界面，设置是否自动隐藏满级角色
	flag(Boolean): Ture: auto hide, Fales: always show"""
	ensure = image_g.auto_hide
	screen = ims.capture_adb()
	screen = screen[
					  lt_gl.auto_hideY[0]:lt_gl.auto_hideY[1],
					  lt_gl.auto_hideX[0]:lt_gl.auto_hideX[1]
					  ]
	res = ims.image_match(ensure, threshold=0.9,screen_image=screen)
	if flag: # 需要隐藏
		if res[0] == 0:
			humanbeing_click(lt_gl.auto_hideX, lt_gl.auto_hideY)
	else: # 不需要隐藏
		if res[0] == 1:
			humanbeing_click(lt_gl.auto_hideX, lt_gl.auto_hideY)

	
if __name__ == '__main__':
	os.chdir("../adb")
	# os.system("adb connect 127.0.0.1:21505")
	mt = ImageMatchSet(cv2.TM_CCOEFF_NORMED)
	# mt.backhome(1)
	# s_image = cv2.imread("../test/1212.png",0)
	# mt.image_match_SIFT('../test/1212_1_0.5size.jpg', screen_image=s_image)
	s_image = cv2.imread("../test/f1.png",0)
	mt.image_match_SIFT('../test/star.png', screen_image=s_image, show=True)
	
	
