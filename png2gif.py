#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/10/13 11:00
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import os
import imageio


def create_gif(image_list, gif_name, duration=1.0):
    """
    :param image_list: 这个列表用于存放生成动图的图片
    :param gif_name: 字符串，所生成gif文件名，带.gif后缀
    :param duration: 图像间隔时间
    :return:
    """
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return


def main():
    # 这里放上自己所需要合成的图片
    path = r"C:\Users\Administrator\Desktop\新建文件夹"
    os.chdir(path)
    image_list = [
        '带描边_wanzheng.jpg',
        '无描边.jpg', '无描边.jpg'
    ]
    gif_name = '1.gif'
    duration = 0.55
    create_gif(image_list, gif_name, duration)


if __name__ == '__main__':
    main()