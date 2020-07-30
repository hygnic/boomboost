#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/7/25 14:32
# Reference:
"""
Description:
Usage:
adb shell input keyevent 4
每个数字与keycode对应表如下：
	0 -->  "KEYCODE_UNKNOWN"
	1 -->  "KEYCODE_MENU"
	2 -->  "KEYCODE_SOFT_RIGHT"
	3 -->  "KEYCODE_HOME"
	4 -->  "KEYCODE_BACK"
	5 -->  "KEYCODE_CALL"
	6 -->  "KEYCODE_ENDCALL"
	7 -->  "KEYCODE_0"
	8 -->  "KEYCODE_1"
	9 -->  "KEYCODE_2"
	10 -->  "KEYCODE_3"
	11 -->  "KEYCODE_4"
	12 -->  "KEYCODE_5"
	13 -->  "KEYCODE_6"
	14 -->  "KEYCODE_7"
	15 -->  "KEYCODE_8"
	16 -->  "KEYCODE_9"
	17 -->  "KEYCODE_STAR"
	18 -->  "KEYCODE_POUND"
	19 -->  "KEYCODE_DPAD_UP"
	20 -->  "KEYCODE_DPAD_DOWN"
	21 -->  "KEYCODE_DPAD_LEFT"
	22 -->  "KEYCODE_DPAD_RIGHT"
	23 -->  "KEYCODE_DPAD_CENTER"
	24 -->  "KEYCODE_VOLUME_UP"
	25 -->  "KEYCODE_VOLUME_DOWN"
	26 -->  "KEYCODE_POWER"
	27 -->  "KEYCODE_CAMERA"
	28 -->  "KEYCODE_CLEAR"
	29 -->  "KEYCODE_A"
	30 -->  "KEYCODE_B"
	31 -->  "KEYCODE_C"
	32 -->  "KEYCODE_D"
	33 -->  "KEYCODE_E"
	34 -->  "KEYCODE_F"
	35 -->  "KEYCODE_G"
	36 -->  "KEYCODE_H"
	37 -->  "KEYCODE_I"
	38 -->  "KEYCODE_J"
	39 -->  "KEYCODE_K"
	40 -->  "KEYCODE_L"
	41 -->  "KEYCODE_M"
	42 -->  "KEYCODE_N"
	43 -->  "KEYCODE_O"
	44 -->  "KEYCODE_P"
	45 -->  "KEYCODE_Q"
	46 -->  "KEYCODE_R"
	47 -->  "KEYCODE_S"
	48 -->  "KEYCODE_T"
	49 -->  "KEYCODE_U"
	50 -->  "KEYCODE_V"
	51 -->  "KEYCODE_W"
	52 -->  "KEYCODE_X"
	53 -->  "KEYCODE_Y"
	54 -->  "KEYCODE_Z"
	55 -->  "KEYCODE_COMMA"
	56 -->  "KEYCODE_PERIOD"
	57 -->  "KEYCODE_ALT_LEFT"
	58 -->  "KEYCODE_ALT_RIGHT"
	59 -->  "KEYCODE_SHIFT_LEFT"
	60 -->  "KEYCODE_SHIFT_RIGHT"
	61 -->  "KEYCODE_TAB"
	62 -->  "KEYCODE_SPACE"
	63 -->  "KEYCODE_SYM"
	64 -->  "KEYCODE_EXPLORER"
	65 -->  "KEYCODE_ENVELOPE"
	66 -->  "KEYCODE_ENTER"
	67 -->  "KEYCODE_DEL"
	68 -->  "KEYCODE_GRAVE"
	69 -->  "KEYCODE_MINUS"
	70 -->  "KEYCODE_EQUALS"
	71 -->  "KEYCODE_LEFT_BRACKET"
	72 -->  "KEYCODE_RIGHT_BRACKET"
	73 -->  "KEYCODE_BACKSLASH"
	74 -->  "KEYCODE_SEMICOLON"
	75 -->  "KEYCODE_APOSTROPHE"
	76 -->  "KEYCODE_SLASH"
	77 -->  "KEYCODE_AT"
	78 -->  "KEYCODE_NUM"
	79 -->  "KEYCODE_HEADSETHOOK"
	80 -->  "KEYCODE_FOCUS"
	81 -->  "KEYCODE_PLUS"
	82 -->  "KEYCODE_MENU"
	83 -->  "KEYCODE_NOTIFICATION"
	84 -->  "KEYCODE_SEARCH"
	85 -->  "TAG_LAST_KEYCODE"



"""
# ---------------------------------------------------------------------------
import os
import cv2
from dcutility import image_match

# cmd_get = "adb shell screencap -p /sdcard/screen_img.png"
# # 发送图片口令
# # cmd_send = 'adb pull sdcard/screen_img.png F:/yys'
# cmd_send = "adb pull sdcard/screen_img.png G:/MoveOn/boomboost/image"
# cmd_click = 'adb shell input tap {} {}'.format(129, 294)
# back = "adb shell input keyevent 4"
os.chdir("../adb")
# os.system("adb connect 127.0.0.1:21503")
# 截屏和发送操作
# os.system(cmd_get)
# os.system(cmd_send)

# os.system(cmd_click)
# os.system(back)
# temp = u"G:/MoveOn/boomboost/image/spring/change_towel.png"
# image = u"G:/MoveOn/boomboost/image/spring/screen_changet.png"
# image = cv2.imread(image,0)
# temp = cv2.imread(temp,0)
# res = cv2.matchTemplate(image,temp,cv2.TM_CCOEFF_NORMED)
# maxres = res.max()
# print "maxres:",maxres
# print "res:", res
# main_menu = [u"../image/main_menu_flag1.png",
# 			 u"../image/main_menu_flag2.png",
# 			 u"../image/main_menu_flag3.png",
# 			 u"../image/main_menu_flag4.png"]
# res1,res2=dcutility.image_match(main_menu,0.8)
# print res1
# print res2 # [0.95081216, 0.94556034, 0.8740529, 0.951997]

rea1,ress2 = image_match(ur"G:\MoveOn\boomboost\image\spring\after_spa.png",0.85)
print ress2