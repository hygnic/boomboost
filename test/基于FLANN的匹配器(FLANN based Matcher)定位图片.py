#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/8/19 17:17
# Reference: https://blog.csdn.net/zhuisui_woxin/article/details/84400439
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
# 基于FLANN的匹配器(FLANN based Matcher)定位图片
import numpy as np
import cv2
from matplotlib import pyplot as plt

from DCcore import dcutility as dc


@dc.timewrap
def image_match_SIFT(temp, screen=None, threhold = 0.7):
	# Image Identification
	# template = cv2.imread('template_adjust.jpg', 0)  # queryImage
	# target = cv2.imread('target.jpg', 0)  # trainImage
	template = cv2.imread(temp, 0)  # queryImage '1212_1_0.5size.jpg'
	target = cv2.imread(screen, 0)  # trainImage '1212.png'
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
			
	MIN_MATCH_COUNT = 10  # 设置最低特征点匹配数量为10
	if len(good) > MIN_MATCH_COUNT:
		# 获取关键点的坐标
		src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
		dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
		# 计算变换矩阵和MASK
		M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
		matchesMask = mask.ravel().tolist()
		h, w = template.shape
		# 使用得到的变换矩阵对原图像的四个角进行变换，获得在目标图像上对应的坐标
		pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(
			-1, 1, 2)
		dst = cv2.perspectiveTransform(pts, M)
		cv2.polylines(target, [np.int32(dst)], True, [255, 255, 255], 5, cv2.LINE_8) # 绘制矩形
		print [np.int32(dst)]
	else:
		print("Not enough matches are found - %d/%d" % (len(good), MIN_MATCH_COUNT))
		matchesMask = None
	draw_params = dict(matchColor=(0, 255, 0),
					   singlePointColor=None,
					   matchesMask=matchesMask,
					   flags=2)
	result = cv2.drawMatches(template, kp1, target, kp2, good, None, **draw_params)
	print len(good)
	plt.imshow(result, 'gray')
	plt.show()

if __name__ == '__main__':
	# 1212_1_0.5size.jpg'
	# 	target = cv2.imread(screen, 0)  # trainImage '1212.png'
	image_match_SIFT(temp = '1212_1_0.5size.jpg', )