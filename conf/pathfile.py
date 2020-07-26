#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/7/26 18:50
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import os
import sys

this_adress = os.path.abspath(__file__) # G:\MoveOn\boomboost\conf\pathfile
conf_dir = os.path.dirname(this_adress) # G:\MoveOn\boomboost\conf
main_dir = os.path.dirname(conf_dir) # G:\MoveOn\boomboost
main_dir = os.path.abspath(main_dir) # G:\MoveOn\boomboost
image_f = os.path.join(main_dir,"image")

class Path(object):
	def __init__(self):
		
		# DC主界面标志图模板的地址
		main_menu1= os.path.join(image_f,u"main_menu_flag1.png")
		main_menu2= os.path.join(image_f,u"main_menu_flag2.png")
		main_menu4= os.path.join(image_f,u"main_menu_flag4.png")
		self.mian_flags = [main_menu1, main_menu2, main_menu4]
		
		self.dont_stop()
		
	def dont_stop(self):
		# 一些奇怪事情的比较模板，比如询问是否退出，网络中断等
		self.quit= os.path.join(image_f,u"quit.png")
		self.network_error= os.path.join(image_f,u"network_error_clip.png")
		
if __name__ == '__main__':
	aa = Path()
	print main_dir
	
