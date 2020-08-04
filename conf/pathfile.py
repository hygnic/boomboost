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

# image_f = os.path.join(main_dir,"image")
# 中文版
image_f = os.path.join(main_dir,"image/image_CN")

general_dir = os.path.join(image_f,"general")
agate2coin_dir = os.path.join(image_f,"agate2coin")
farm = os.path.join(image_f,"farm")

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

class ImageDCGeneral(object):
	def __init__(self):
		# 筛选界面的选中小按钮
		self.selcted = os.path.join(general_dir, "selected.png")
		# 角色选择界面的标志物(参照),用于程序的返回
		self.flag_selcte_interface = os.path.join(general_dir, "flag_selcte_interface.png")
		# 勾选排除所有满级child
		self.auto_hide = os.path.join(general_dir, "exclude_max_level.png")
		# 角色列表从左到右 结束 角色右边显示全黑
		self.none_charater = os.path.join(general_dir, "none_charater.png")


# 将玛瑙转化为金币的一些图片
class ImageAgateToCoin(ImageDCGeneral):
	def __init__(self):
		ImageDCGeneral.__init__(self)
		# 提升好感度的按键
		self.improve_impression = os.path.join(agate2coin_dir,
												"improve_impression.png")
		# 空的好感进度条 empty prograssbar
		self.check_impression = os.path.join(agate2coin_dir, "point_zero.png")
		
		# screencapture of "S class" mark
		self.s_class = os.path.join(agate2coin_dir, "S_class.png")
		
		# 点击child的s class 提升后有一个进化动画，结束后出现该按键
		self.improve_finish = os.path.join(agate2coin_dir, "finish.png")
		
		
class ImageFarm(ImageDCGeneral):
	def __init__(self):
		ImageDCGeneral.__init__(self)
		
		# 满级
		self.levelmax = os.path.join(farm, "levelmax.png")
		
		# 重复角色
		self.repeat = os.path.join(farm, "error1.png")
		# 自动
		self.auto = os.path.join(farm, "auto.png")
		# 开始战斗
		self.start_button = os.path.join(farm, "start_button.png")
		# 战斗结束
		self.battle_result = os.path.join(farm, "battle_result.png")



if __name__ == '__main__':
	aa = Path()
	print main_dir
	
