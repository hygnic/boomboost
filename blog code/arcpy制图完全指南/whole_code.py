#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2021/1/23 16:56
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
from __future__ import absolute_import
from __future__ import unicode_literals
import arcpy

"""__________________________________________________________________________"""
"""____________________________global_values_________________________________"""
# 地址
mxd_template = r"E:\doc\Scratch\tempMXDS"  # 模板文件位置
output_dir = r"E:\doc\Scratch\out"  # 输出位置
gdb_path = r"E:\doc\Scratch\arcpy指南.gdb"  # 数据库地址
# 重要常量
FIELD = "CITY" # 检索字段
MI = "MappingIndex" # 制图索引文件名称
SCALE = 200000 # 制图的比例尺
"""____________________________global_values_________________________________"""
"""__________________________________________________________________________"""
arcpy.env.overwriteOutput = True
arcpy.env.workspace = gdb_path

def check_field(layer, field):
    return field in arcpy.ListFields(layer)
    



class MinimumBounding(object):
    """
    用于生成最小边界几何
    """
    def __init__(self, mapdocument):
        self.mxd = mapdocument
        if not check_field(MI,"MBG_Width"): # 没有计算过最小几何边界
            self.layer = self.minimum_bounding()
            
            
    def minimum_bounding(self):
        """
        计算最小边界几何，并用结果图层覆盖初始图层;计算过最小边界几何的图层有"MBG_Width"字段
        创建PAGRSIZE 字段
        :return: 制图索引文件的要素图层
        """
        arcpy.MinimumBoundingGeometry_management(MI,
                                                 "mapping_index_out",
                                                 "ENVELOPE",
                                                 "LIST",
                                                 FIELD,
                                                 True)
        arcpy.Delete_management(MI, "FeatureClass")
        arcpy.Rename_management("mapping_index_out", MI, "FeatureClass")
        arcpy.AddField_management(MI, "PAGESIZE", "TEXT", field_length = 100)
        # 图层要素 用于设置定义查询 以匹配大小
        mapping_index_layer = arcpy.mapping.ListLayers(self.mxd, MI)[0]
        return mapping_index_layer

    def page_size(self, scale):
        with arcpy.da.UpdateCursor(self.layer,["MBG_Width", "MBG_Length"]) as cursor:
            for row in cursor:
                width = row[0]
                length = row[1]
        
        


# mxd = arcpy.mapping.MapDocument("CURRENT")
mxd = arcpy.mapping.MapDocument(r"E:\doc\Scratch\tempMXDS\arcpy完全制图指南.mxd")
MinimumBounding(mxd)