#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/7/25 15:26
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------


class Spring(object):
	def __init__(self):
		self.spring()
		self.settings()
	
	def settings(self):
		# 询问退出
		self.no_quitX = (350, 439)
		self.no_quitY = (535, 566)
		# 重连网络
		self.reconnectX = (550, 652)
		self.reconnectY = (535, 564)
		
		self.nightwordX = (904, 993)
		self.nightwordY = (700, 779)
	
	
	def spring(self):
		# spring
		self.menu_springX = (570, 650)
		self.menu_springY = (240, 310)
		# 4th floor
		self.spring4fX = (490,568)
		self.spring4fY = (370,447)
		# 3rd floor
		self.spring3fX = (645, 697)
		self.spring3fY = (479, 558)
		# 2nd floor
		self.spring2fX = (644, 667)
		self.spring2fY = (536, 558)
		
		# 1st floor
		self.spring1fX = (484, 506)
		self.spring1fY = (697, 705)
		self.spring_house = [
			
			
			[self.spring3fX,self.spring3fY],
			[self.spring4fX,self.spring4fY]
		]
		
		# 温泉进入按钮
		self.enter_hotspringX =(457,5477)
		self.enter_hotspringY =(649,683)
		# 结束泡温泉（批量5个）
		self.end_spaX =(949,966)
		self.end_spaY =(263,280)
		# 更换毛巾
		self.change_towelX =(347,463)
		self.change_towelY =(809,848)
		# skip zoom 加速区域
		self.spring_skipX = (335, 695)
		self.spring_skipY = (114, 733)
		
		# after spa 五个爵角色重新入浴后有一个确认键要点, 这个键位于中间
		self.after_spaX = (456, 540)
		self.after_spaY = (500, 530)
	

class Farm(object):
	def __init__(self):
		self.fram()
		
	def fram(self):
		self.fselectX = (396, 602)
		self.fselectY = (173, 200)
		
		# ----------------------------------------------------------------------
		# battle position 五个上场位置 从左到右
		
		self.first_poltX = (309, 373)
		self.first_poltY = (79, 254)
		
		self.second_poltX = (385, 454)
		self.second_poltY = (76, 251)
		
		self.third_poltX = (473, 537)
		self.third_poltY = (77, 240)
		
		self.fourth_poltX = (550, 618)
		self.fourth_poltY = (64, 256)
		
		self.fifth_poltX = (626, 696)
		self.fifth_poltY = (91, 253)
		# ----------------------------------------------------------------------
		# join_team
		self.join_teamX = (316, 422)
		self.join_teamY = (426, 456)
		# 上面五个位置的列表，*从右到左
		self.position = [
			[self.fifth_poltX, self.fifth_poltY],
			[self.fourth_poltX, self.fourth_poltY],
			[self.third_poltX, self.third_poltY],
			[self.second_poltX, self.second_poltY],
			[self.first_poltX, self.first_poltY]
						 ]
		
		
		# 重复角色 返回
		self.confirm_backX = (442, 555)
		self.confirm_backY = (499, 537)
		
		# selcet leftside child 遇到重复的天子，点击以选择左边的天子
		self.leftsideX = (264, 320)
		self.leftsideY = (539, 683)
		
		# 循环战斗按钮
		self.loopX = (302, 319)
		self.loopY = (284, 299)
		
		# 裁剪等级显示区域
		# 裁剪结果示例 数字 1 "G:\MoveOn\boomboost\image\示例文件\1.png"
		self.croppedX = (401,405)
		self.croppedY = (600,621)
		
		
class General(object):
	"""通常设置的常见按键的位置 """
	def __init__(self):
		self.charater_interface()
		
	def charater_interface(self):
		# 进入筛选按钮 （中间靠右黑色）
		self.filterX = (667, 749)
		self.filterY = (360, 388)
		
		# 裁剪 勾选影藏选项 （右上角）
		self.auto_hideX = (630, 648)
		self.auto_hideY = (79, 98)
		
		# 排序按钮 （靠上）
		self.sortX = (503, 565)
		self.sortY = (75, 100)
		
		# 排序方式 第一个
		self.sort1X = (360, 563)
		self.sort1Y = (137, 166)
		
		# 排序方式 第二个
		self.sort2X = (350, 632)
		self.sort2Y = (188, 220)
		
		# 点击一颗星的
		self.star1X = (320, 413)
		self.star1Y = (495, 523)
		
		# 点击二颗星的
		self.star2X = (450, 552)
		self.star2Y = (495, 523)
		
		# 点击角色右边
		self.rightsideX = (420, 485)
		self.rightsideY = (527, 691)
		
		# 角色右侧裁剪区域，用于判断右边是否还有角色
		self.cropped_rightsideX = (432, 632)
		self.cropped_rightsideY = (429, 708)
		
		
class AgateToCoin(object):
	def __init__(self):
		# 查看角色属性的按键
		self.open_attributeX = (290, 421)
		self.open_attributeY = (702, 736)
		
		# 打开提升友好度的按键
		self.open_attributeX = (290, 421)
		self.open_attributeY = (702, 736)
		
		# 裁剪友好度显示区域
		# 使用 G:\MoveOn\boomboost\image\agate2coin\point_zero.png 与裁剪结果比较
		self.croppedX = (410, 518)
		self.croppedY = (142, 148)
		
		# 点击D class、C class之类的
		self.impression_classX = (395, 432)
		self.impression_classY = (379, 428)
		
		# 红色的确认键
		self.improve_impression_confirmX = (457, 543)
		self.improve_impression_confirmY = (586, 618)
		
		# 上方粉色的确认键
		self.rewardX = (456, 543)
		self.rewardY = (180, 209)
		
		
		