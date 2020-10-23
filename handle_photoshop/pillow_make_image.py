#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/10/23 16:55
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os


os.chdir("E:/psd/自贡自流井区")
charactor_font = r"C:/Windows/Fonts/Arial.TTF"

def tianzi(image, postion, text, output):
    # 打开初始文件
    image = Image.open(image)
    # print('原图长宽:', image.size)
    font = ImageFont.truetype(charactor_font, 300)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 输出文字(可以连续写入):
    draw.text(postion, text, font=font, fill='#000000')
    # 模糊并保存:
    image.filter(ImageFilter.BLUR)
    image.save(output)
	
if __name__ == '__main__':
	
    pic = '测试.png'  # 原图路径
    site = (384, 120)  # 距离：上角位置
    txt = '要填充的文字'  # 填充文字
    path = '2.png'  #
    tianzi(pic, site, txt, path)