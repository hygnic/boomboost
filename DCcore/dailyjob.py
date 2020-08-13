#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/8/13 23:00
# Reference:
"""
Description: DC 日常任务
Usage:
"""
# ---------------------------------------------------------------------------
import os
import dcutility as dc
from conf.DClocation import General
from conf.pathfile import ImageDaily

ims =  dc.ImageMatchSet()
lt_gl = General()
image = ImageDaily("daily")

def UG():
	# 进入 night world
	dc.humanbeing_click(lt_gl.nightworldX, lt_gl.nightworldY)
	ims.whileset(image.image_ug)
	dc.humanbeing_click_point(ims.point(zoom=0.1))
	


if __name__ == '__main__':
	os.chdir("../adb")
	os.system("adb connect 127.0.0.1:21503")
	UG()