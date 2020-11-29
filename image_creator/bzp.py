#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/10/23 16:55
# Reference:
"""
Description: 使用一张底图文件
             一张数据表
             分布图
             
             快速生成 “两区” 标志牌
Usage:
"""
# ---------------------------------------------------------------------------
from PIL import Image, ImageDraw, ImageFont, ImageGrab
from os import path
import pandas as pd


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
        
        _x, _y, _x_delta, _y_delta = postion
        if isinstance(text, tuple) or isinstance(text, list):# 多个字段
            for i, element in enumerate(text):
                postion1 = (_x+_x_delta, _y+i*_y_delta)
                self.draw.text(
                    postion1, element, font=font, fill=color, stroke_width=2)
        else: #单个字段
            self.draw.text(
                (_x+_x_delta,_y+_y_delta), text, font=font, fill=color)
    
    
    def text_center_y(self, text, y_postion, ttf, size, color = "black"):
        """
         文字水平居中于图片
        text{Str}:
        y_postion{Int}: 垂直位置
        """
        font = ImageFont.truetype(ttf, size)
        # 计算字体长度
        text_size_x, text_size_y = self.draw.textsize(text, font=font)
        self.draw.text(
            (((self.width - text_size_x) / 2), y_postion),
            text,
            font=font,
            fill=color
        )
    
    def text_center_y_2(self, text, position, ttf, size, color = "black"):
        """
        # 水平居中于指定范围位置的中间
        text{Str}:
        y{Int}: 垂直位置
        size 字体大小
        position{Tuple}: (x,x2,y) x和x2坐标组成一个长度，x2大于x；y表示固定高度
        """
        _x, _x2, _y = position
        width = _x2-_x
        font = ImageFont.truetype(ttf, size)
        # 字体的长和高
        text_size_x, text_size_y = self.draw.textsize(text, font=font)
        self.draw.text(
            (((width - text_size_x) / 2)+_x, _y),
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
        _x1,_y = postion
        font = ImageFont.truetype(ttf, size)
        # 计算字体长度
        text_size_x, text_size_y = self.draw.textsize(text, font=font)
        postion_apl = (self.width-_x1-text_size_x, _y)
        self.draw.text(
            postion_apl, text, font=font, fill=color,stroke_width=2)
        
        
    @staticmethod
    def resize(image,height_limit=4400):
        """
        image{Str}: 图片地址
        height_limit{Int}: 限制边的高度（默认为4400）
        """
        Image.MAX_IMAGE_PIXELS = None  # could be decompression bomb DOS attack
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
    text1 = text.strip()
    single = [_x for _x in text1]
    # print(single)
    text = " ".join(single)
    # text = text[:-1]
    # print(text)
    # print(text)
    return text
    
    
    
    
"""_________________________________EXCEL____________________________________"""
"""_________________________________EXCEL____________________________________"""


if __name__ == '__main__':
    city_name = "遂宁市"
    county_name = "安居区"
    excel_path = "标志牌信息1.xls"
    charactor_font_bd = r"msyhbd.ttf"
    charactor_font = r"msyh.ttf"
    fbt_image_path = r"G:\遂宁安居区\分布图\cliped"
    # fbt_image = r"G:\遂宁安居区\分布图\cliped\白马镇.jpg"
    
    nomal_size = 180 # 普通字体大小 200
    right_distance = 400 # 右侧到图片边缘的距离
    rd = right_distance
    data = "2020 年 11 月" # 图片中显示的时间
    fbt_image_height = 4400 # 插入的分布图的高度 4400 3500
    fbt_name_y = 1500 # 1620 2600
    
    
    dataf = pd.read_excel(excel_path)
    for bzp_data in dataf.itertuples():
        ad = AddText('imag1.jpg')  # 底图
        # print(bzp_data)
        # break
    
    
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
        value1= [getattr(bzp_data, '面积'),
                 getattr(bzp_data, '片块数'),
                 getattr(bzp_data, '地块数'),
                 getattr(bzp_data, '机井数量'),
                 getattr(bzp_data, '蓄水池数量'),
                 getattr(bzp_data, '提罐站数量'),
                 getattr(bzp_data, '作物类型'),
                 getattr(bzp_data, '管护起始时间'),
                 getattr(bzp_data, '保护责任单位'),
                 getattr(bzp_data, '保护责任人')
                 ]
        
        # 排灌工程条件
        pggctj = ""
        jijin = int(value1[3])
        if jijin !=0:
            pggctj = pggctj+"机井 {} 个 ".format(jijin)
            # print("1")
        xsc = int(value1[4])
        if xsc !=0:
            pggctj = pggctj+"蓄水池 {} 个  ".format(xsc)
            # print(2)
        tgz = int(value1[5])
        if tgz !=0:
            pggctj = pggctj+"提灌站 {} 个".format(tgz)
            # print(3)
        # print(pggctj) # 蓄水池 12 个
        
        value1_1= ["{} 公 顷".format(value1[0]),
                   "{} 块".format(value1[1]),
                   "{} 块".format(value1[2]),
                   pggctj,
                   value1[6],
                   text_space(value1[7]),
                   text_space(value1[8]),
                   text_space(value1[9]),
                   ]
        
        """________左第一列___________"""
        """___________________________"""
        
        ad.add_text_column(texts1, (650,1990,0,560), charactor_font, nomal_size)
        # ad.add_text_column(value1_1, (2550,1990,0,560), charactor_font, nomal_size)
        ad.add_text_column(value1_1, (2250,1990,0,560), charactor_font, nomal_size)
        # 标题
        XJQYMC = getattr(bzp_data, "乡镇名称")
        title = text_space(city_name + county_name+XJQYMC)
        print("标题：",title)
        title = "{} 粮 食 生 产 功 能 区".format(title)
        ad.text_center_y(title
                         , 718, charactor_font_bd, 430, color="red")
        # 绘制标志牌
        bzp_number = str(getattr(bzp_data,"标志牌编号"))
        ad.add_text_column("标 志 牌 编 号：", (462, 357, 0, 0), charactor_font_bd, 100)
        ad.add_text_column(bzp_number, (1200, 357, 0, 0), charactor_font_bd, 100)
        
        # 绘制右下角文字
        # 金 堂 县 三 星 镇 人 民 政 府   立
        gov=text_space("安居区{} 立".format(value1[-2]))
        ad.add_text_limit(gov, (rd, 6450), charactor_font, 130)
        # 添加右下角的日期
        ad.add_text_limit(data, (rd, 6650), charactor_font, 130)
        
        # 设置分布图图片
        fbt_image = path.join(fbt_image_path,XJQYMC+".jpg")
        try: # 如果没有找到和表格数据对应的图片会报错
            fbt_image,fbt_w,fbt_h = ad.resize(fbt_image, fbt_image_height)
        except FileNotFoundError as e:
            print(e.strerror)
            continue
        x_topleft, y_topleft =9450-fbt_w, 6180-fbt_h  # 9400
        x_bottomright, y_bottomright = 9450, 6180
        # 粘贴区域大小
        box=(x_topleft, y_topleft, x_bottomright, y_bottomright)
        ad.image.paste(fbt_image, box)
        
        # 分布图名称 居中
        title_1 = text_space("{}“两区”农田空间分布图".format(XJQYMC))
        x2= 9921-rd
        x=x2-fbt_w
        y=fbt_name_y
        ad.text_center_y_2(title_1,(x,x2,y),charactor_font_bd, 180, color="black")
        
        # bzp_bm = bzp_data{}
        ad.save("BZP"+bzp_number+".jpg")
    