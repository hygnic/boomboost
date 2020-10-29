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
from PIL import Image, ImageDraw, ImageFont, ImageGrab
import os


class AddText(object):
    
    def __init__(self,image):
        """
        image(): image path
        ttf(): ttf file path
        size(Int):
        """
        self.image = Image.open(image) # 转换为图像对象
        
        self.size = self.image.size
        self.width = self.size[0] # 图片宽
        self.height = self.size[1] # 图片高
        
        self.draw = ImageDraw.Draw(self.image)
        

    def add_text_column(self, text, postion,ttf,size,color = "black"):
        """
        简单的给图片添加文字（根据指定位置）
        xy{Tuple}: (x, y_delta)
        text{Tuple/Str}: 文字信息
        postion{Tuple}: (x, y, x_delta, y_delta)
        output{}:
        :return: 
        """
        font = ImageFont.truetype(ttf, size)
        
        x, y, x_delta, y_delta = postion
        if isinstance(text, tuple):# 多个字段
            for i, element in enumerate(text):
                postion1 = (x+x_delta, y+i*y_delta)
                self.draw.text(
                    postion1, element, font=font, fill=color, stroke_width=2)
        else: #单个字段
            self.draw.text(
                (x+x_delta,y+y_delta), text, font=font, fill=color)
    
    
    def text_center_y(self, text, y, ttf, size, color = "black"): # 水平居中
        """
        text{Str}:
        y{Int}: 垂直位置
        """
        font = ImageFont.truetype(ttf, size)
        # 计算字体长度
        text_size_x, text_size_y = self.draw.textsize(text, font=font)
        self.draw.text(
            ((self.width - text_size_x) / 2, y),
            text,
            font=font,
            fill=color
        )
    
    def add_text_limit(self,text,postion,ttf,size,color = "black"):
        """
        给图片添加文字（文字右边始终在同一位置）
        text:
        postion{Tuple}:(x1,y) x1表示到最左边的距离
        ttf
        size
        """
        x1,y = postion
        font = ImageFont.truetype(ttf, size)
        # 计算字体长度
        text_size_x, text_size_y = self.draw.textsize(text, font=font)
        postion_apl = (self.width-x1-text_size_x, y)
        self.draw.text(
            postion_apl, text, font=font, fill=color,stroke_width=2)
        
        
    @staticmethod
    def resize(image,height_limit=4400):
        """
        image{Str}: 图片地址
        height_limit{Int}: 限制边的高度（默认为4400）
        """
        img = Image.open(image)
        # img = ImageGrab.grab()  # 截图
        width = img.size[0]  # 获取宽度
        height = img.size[1]  # 获取高度
        resize_para = height_limit/height
        width_limit = (int(width * resize_para))
        img = img.resize((width_limit, height_limit), Image.ANTIALIAS)
        # img.save("love.jpg")
        return img, width_limit, height_limit
    
    def save(self,output):
        # save as
        self.image.save(output)
    
    @property
    def image2(self):
        return self.image
        


def text_space(text):
    # 给两个个中文字符中间添加空格
    text = text.strip()
    single = text.split()
    text = " ".join(single)
    # text = text[:-1]
    # print(text)
    return text
    
        
if __name__ == '__main__':
    # 图片中显示的时间
    data = "2020 年 10 月"
    # 插入的分布图的高
    fbt_image_height = 4400
    """__________________________"""
    """________左第一列___________"""
    texts1 = (
        '面    积：',
        '片  块  数：',
        '地  块  数：',
        '排 灌 工 程 条 件：',
        '作 物 类 型：',
        '管 护 起 始 时 间：',
        '保 护 责 任 单 位：',
        '保 护 责 任 人：'
    )
    """________左第一列___________"""
    """__________________________"""
    os.chdir("G:\MoveOn\ps")
    charactor_font_bd = r"msyhbd.ttf"
    charactor_font = r"msyh.ttf"
    
    ad = AddText('ceshi.jpg')
    ad.add_text_column(texts1, (783,1990,0,560), charactor_font, 200)
    
    title = "成 都 市 金 堂 县 三 星 镇 粮 食 生 产 功 能 区"
    ad.text_center_y(title
                     , 718, charactor_font_bd, 430, color="red")

    ad.add_text_column("标 志 牌 编 号：", (462, 357, 0, 0), charactor_font_bd, 100)
    ad.add_text_limit(
        "金 堂 县 三 星 镇 人 民 政 府   立",
        (630, 6450), charactor_font, 130)
    # 添加右下角的日期
    ad.add_text_limit(data, (630, 6650), charactor_font, 130)
    
    # 设置分布图图片
    fbt_image,fbt_w,fbt_h = ad.resize("新津县1.jpg", fbt_image_height)
    x_topleft, y_topleft =9300-fbt_w, 6400-fbt_h
    x_bottomright, y_bottomright = 9300, 6400
    # 粘贴区域大小
    box=(x_topleft, y_topleft, x_bottomright, y_bottomright)

    ad.image.paste(fbt_image, box)
    
    ad.save("out1.jpg")

    