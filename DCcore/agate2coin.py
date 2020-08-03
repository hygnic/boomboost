#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/7/31 23:27
# Reference:
"""
Description: 将玛瑙换为金币 python2.7
Usage:
"""
# ---------------------------------------------------------------------------
import os
import sys
import logging as lg
import dcutility as dc
from conf. DClocation import General
from conf. DClocation import AgateToCoin
from conf.pathfile import ImageAgateToCoin

ims = dc.ImageMatchSet()
lt_gl = General()  # 位置
lt_a2c = AgateToCoin()  # 位置
image = ImageAgateToCoin()
lg.basicConfig(
	format="%(asctime)s >> %(funcName)s %(levelname)s: %(message)s",
	datefmt="%d-%m-%Y %H:%M:%S", level=lg.DEBUG)

# 初始化 目前程序从队伍查看界面开始
def initil():
	dc.cancel_selection()
	dc.sleep(1)
	# 选择一星和两星的角色 # TODO 还要取消自动隐藏选项
	dc.humanbeing_click(lt_gl.star1X, lt_gl.star1Y)
	dc.humanbeing_click(lt_gl.star2X, lt_gl.star2Y)
	dc.back()
	dc.sleep(0.5)
	dc.screenswipe((113, 253), (498, 650), (600, 740), (503, 640),)  # swipe screen
	
# main function
def get_money():
	dc.humanbeing_click(lt_a2c.open_attributeX, lt_a2c.open_attributeY)
	dc.sleep(1.2)
	# 点击进入好感度提升界面
	res = ims.image_match(image.improve_impression)
	dc.humanbeing_click_point(ims.point(0.3))
	dc.sleep(0.6)
	# 检查好感进度条，留下为0的
	cropped = ims.capture()
	cropped = cropped[
			  lt_a2c.croppedY[0]:lt_a2c.croppedY[1],
			  lt_a2c.croppedX[0]:lt_a2c.croppedX[1]
			  ]
	res = ims.image_match(image.check_impression,threshold=0.86, screen_image= cropped)
	if res[0] == 1: # 0 好感的
		improve_click()
	else: # 有好感了，返回
		# lg.DEBUG("已经存在好感度! 返回")
		ims.backtopage(image.flag_selcte_interface)
		
		dc.sleep(1)
		next_chara()
		get_money()
		
# 完成好感提升的几个点击动作，之后再返回角色选择界面
def improve_click():
	for improve_click_count in xrange(4): # 4 times
		dc.sleep(1)
		dc.humanbeing_click(lt_a2c.impression_classX, lt_a2c.impression_classY)
		dc.sleep(0.6)
		# 点击红色的确认按键
		dc.humanbeing_click(
			lt_a2c.improve_impression_confirmX, lt_a2c.improve_impression_confirmY)
		dc.sleeptime(0.7,1)
		dc.back()
	dc.sleeptime(2)
	# 点击最后一个S class 按键，由于这个位置不确定，使用图像匹配的方法来确认位置
	# 图像匹配 S class
	ims.image_match(image.s_class, 0.9)
	dc.humanbeing_click_point(ims.point( zoom=0.2, x_add=0, y_add =-58))
	dc.sleep(0.3)
	# 点击红色的确认按键
	dc.humanbeing_click(
		lt_a2c.improve_impression_confirmX, lt_a2c.improve_impression_confirmY)
	
	ims.whileset(image.improve_finish, 6, 7)
	dc.humanbeing_click_point(ims.point(zoom=0))
	dc.back()
	dc.sleep(0.3)
	# 获取奖励
	dc.humanbeing_click(lt_a2c.rewardX, lt_a2c.rewardY)
	dc.sleep(2)
	
	# 返回天子选择界面
	ims.backtopage(image.flag_selcte_interface)
	
def next_chara():
	"""向右点击，获取下一位child"""
	# 将屏幕中角色选择区域右侧截取
	next_chara_cropped = ims.capture()
	next_chara_cropped = next_chara_cropped[
						 lt_gl.cropped_rightsideY[0]:lt_gl.cropped_rightsideY[1],
						 lt_gl.cropped_rightsideX[0]:lt_gl.cropped_rightsideX[1]
						  ]
	res = ims.image_match(image.none_charater, threshold=0.8, screen_image=next_chara_cropped)
	if res[0] == 1: # 右边没有角色
		print " All charater improved"
		sys.exit(0)
	else:
		# 向右点击，获取下一位child
		dc.humanbeing_click(lt_gl.rightsideX, lt_gl.rightsideY)
		
	
if __name__ == '__main__':
	# TODO 存在的问题 在升级一个橘色后，角色顺序会变
	
	os.chdir("../adb")
	# # os.system("adb connect 127.0.0.1:21503")
	# initil() # TODO 修改排序
	dc.sleep(0.5)
	while True:
		# 点击角色下方查看属性并进入友好度提升界面
		get_money()
		dc.sleeptime(0.2, 0.3)
		next_chara()
	
	
	