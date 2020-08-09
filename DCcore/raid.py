#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/8/4 17:07
# Reference:
"""
Description: 用于raid自动打车， 自动买砖石
Usage:
"""
# ---------------------------------------------------------------------------
import os
import sys
import logging as lg
import dcutility as dc
from conf. DClocation import General
from conf. DClocation import Raid
from conf.pathfile import Imageraid


lt_raid = Raid()
ims = dc.ImageMatchSet()
imageraid = Imageraid()

def enter_raid():
	"""进入raid界面"""
	dc.humanbeing_click(1,2,0.1, 0.3)
	pass

def filter_sort():
	"""标志物检测和排序设置"""
	
	# 标志物检测
	ims.whileset(imageraid.raid_flag)
	# print imageraid.raid_flag
	# ims.show(0)
	# 排序设置
	# 点击过滤按键
	dc.humanbeing_click(lt_raid.raid_filterX, lt_raid.raid_refreshY, 0.3)
	# 点击 未参加
	dc.humanbeing_click(lt_raid.raid_23X, lt_raid.raid_23Y, 0.3)
	# 点击 按 HP 排序
	dc.humanbeing_click(lt_raid.raid_12X, lt_raid.raid_12Y, 0.3)
	# 点击确认键以返回
	dc.humanbeing_click(lt_raid.filter_OKX, lt_raid.filter_OKY, 0.3)

def refresh():
	"""点击刷新"""
	dc.sleeptime(5,6)
	dc.humanbeing_click(lt_raid.raid_refreshX, lt_raid.raid_refreshY)
	
def select_boss_battle():
	"""select level-40 boss to beat"""
	# dc.sleep(1)
	res = ims.image_match(imageraid.level40)
	if res[0] == 0: # 不存在level40
		# refresh
		refresh()
		select_boss_battle()
	if res[0] == 1: # 存在40级的
		# 点击 level40 标志
		dc.humanbeing_click_point(ims.point(zoom=0))
		dc.sleeptime(0.3, 0.6)
		# 确认进入到raid配置界面
		ims.whileset(imageraid.raid_battle, 0.8, 1)
		# battle-button icon
		battle_icon = ims.point(zoom=0.3)
		dc.humanbeing_click_point(battle_icon)
		# auto buy tickets function
		buy_ticket(battle_icon)

def buy_ticket(point):
	"""
	auto buy tickets while there is showing no ticket
	point(Object) such as: ims.point(zoom=0)
	"""
	dc.sleep(4)
	res = ims.image_match(imageraid.buy_ticket)
	if res[0] ==1:
		print "<<Buying Tickets!>>"
		# The comfirm button of buy tickets
		dc.humanbeing_click(lt_raid.buy_ticketX, lt_raid.buy_ticketY)
		dc.back(0.8,1)
		# need click battle button after buy tickets
		dc.humanbeing_click_point(point)
		
def raid_detect(time):
	"""Detecting the boss raid battle whether finished"""
	dc.sleep(time)
	ims.whileset(imageraid.raid_complete)
	res = ims.image_match(imageraid.raid_complete)
	dc.back()
	dc.sleep(4)
	
	
if __name__ == '__main__':
	# 1080X2340
	os.chdir("../adb")
	# os.system("adb connect 127.0.0.1:21503")
	# ims.capture_adb()
	
	while True:
		filter_sort()
		select_boss_battle()
		raid_detect(265)