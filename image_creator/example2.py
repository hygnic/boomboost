#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/10/23 15:55
# Reference:
"""
Description: 用于操作psd图层
Usage:
"""
# ---------------------------------------------------------------------------
import psd_tools as ps
import os

os.chdir("E:/psd/自贡自流井区")
psd = ps.PSDImage.open('测试.psd')
psd.composite().save('测试.png') # psd.composite().save('测试.pnf') >> OSError: cannot write mode CMYK as PNG

for layer in psd:
    print(layer)
    image = layer.composite()