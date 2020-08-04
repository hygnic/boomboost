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
from conf. DClocation import AgateToCoin
from conf.pathfile import ImageAgateToCoin


def enter_raid():
	"""进入raid界面"""
	dc.humanbeing_click(1,2,0.1, 0.3)

def sort():
	"""排序设置"""
	dc.humanbeing_click(1,2,0.1, 0.3)
	pass
	# 排序完成 返回
	dc.back()

def refresh():
	"""点击刷新"""
	dc.sleep(0.5)
	dc.humanbeing_click(1, 2, 0.1, 0.3)
	
def select_boss_battel():
	"""选择合适的副本"""
	
	
	