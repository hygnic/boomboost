#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/8/4 17:07
# Reference:
"""
Description: 该程序主要用于raid自动打车，自动买票
				20200810
					1.未考虑钻石不够的情况
					2.开始会有标志物匹配的过程，所以每期的raid标志物可能不同
Usage:
"""
# ---------------------------------------------------------------------------
import os
import sys
import logging as log
import dcutility as dc
from conf. DClocation import Raid, RaidPhone1080X2340
from conf.pathfile import ImageRaid


def check_flag():
	"""标志物检测"""
	ims.whileset(imageraid.raid_flag)

def filter_sort():
	"""排序设置"""
	# 排序设置
	# 点击过滤按键
	dc.humanbeing_click(lt_raid.raid_filterX, lt_raid.raid_refreshY, 0.3)
	# 点击 未参加
	dc.humanbeing_click(lt_raid.raid_23X, lt_raid.raid_23Y, 0.5)
	# 点击 按 HP 排序
	dc.humanbeing_click(lt_raid.raid_12X, lt_raid.raid_12Y, 0.8)
	# 点击确认键以返回
	dc.humanbeing_click(lt_raid.filter_OKX, lt_raid.filter_OKY, 0.8)

def refresh():
	"""点击右侧刷新按键"""
	dc.sleeptime(5,6)
	dc.humanbeing_click(lt_raid.raid_refreshX, lt_raid.raid_refreshY)
	
def select_boss_battle():
	"""main funtion: select level-40 boss to beat"""
	# dc.sleep(1)
	res = ims.image_match(imageraid.level40)
	if res[0] == 0: # 不存在level40
		# refresh
		refresh()
		select_boss_battle()
	if res[0] == 1: # 存在40级的
		# 点击 level40 标志
		point = ims.point(zoom=0.3)
		dc.humanbeing_click_point(point)
		dc.sleeptime(0.3, 0.6)
		# 确认进入到raid配置界面
		res = ims.whileset(imageraid.raid_battle, 0.8, 1, loop=False)
		if res == 0: # 未进入到 raid_battle icon 界面 再点一次
			refresh()
			select_boss_battle()
		# battle-button icon
		battle_icon = ims.point(zoom=0.3)
		dc.humanbeing_click_point(battle_icon)
		# auto buy tickets function
		buy_ticket(battle_icon)
		check_done()
		
def check_done():
	"""在我们点击battle按键后，检测battle是否已经被别人完成"""
	dc.sleep(2)
	res = ims.image_match(
		imageraid.already_done, threshold=0.7, screen_image=ims.screenshots[-1])
	if res[0] == 1:
		dc.back(0.1, 0.2)
		check_flag()
		select_boss_battle()
	

def buy_ticket(point):
	"""
	auto buy tickets while there is showing no ticket
	point(Object) such as: ims.point(zoom=0) 那个红色的X按键
	"""
	dc.sleep(2)
	res = ims.image_match(imageraid.no_ticket)
	if res[0] ==1:
		dc.back()
		# button of buy tickets
		dc.humanbeing_click(lt_raid.buy_ticket_buttonX, lt_raid.buy_ticket_buttonY, a=0.6, b =1.2)
		# The comfirm button of buy tickets
		dc.sleep(0.5)
		dc.humanbeing_click(lt_raid.buy_ticketX, lt_raid.buy_ticketY)
		print "<<Buying Tickets!>>"
		dc.back(1,2)
		# need click battle button after buy tickets
		dc.humanbeing_click_point(point)
		
def raid_detect(time):
	"""Detecting the boss raid battle whether finished"""
	dc.sleep(time)
	ims.whileset([imageraid.raid_complete, imageraid.raid_complete2])
	# res = ims.image_match(imageraid.raid_complete)
	# dc.sleep(1)
	
	dc.back()
	dc.sleep(4)
	
	
	
if __name__ == '__main__':
	dc.log_settin(log.DEBUG)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	# 适配 emulator
	# lt_raid = Raid()
	# imageraid = ImageRaid("raid")

	lt_raid = RaidPhone1080X2340()
	imageraid = ImageRaid("raid_phone")
	# 适配phone 1080X2340
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	
	os.chdir("../adb")
	os.system("adb connect 127.0.0.1:21503")
	# ims.capture_adb()
	ims = dc.ImageMatchSet()
	while True:
		check_flag()
		filter_sort()
		select_boss_battle()
		raid_detect(228)