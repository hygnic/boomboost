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
from __future__ import print_function
from __future__ import division
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

# name:width height
page_size_d = {
    "pagesize1":(1180,950),
    "pagesize2":(1180,1350),
    "pagesize3":(1380,850),
    "pagesize4":(880,650),
}


# page_size_d2 = {k:(v[0], v[1], v[0]*v[1], v[0]/v[1]) for k,v in page_size_d.items()}
#
#
# test_v = [1170, 1250]
# tes_w = test_v[0]
# tes_h = test_v[1]
# tes_div = tes_w/tes_h
#
#
# # 符合该制图单位的模板大小的字典
# new_dict = {k:v for k, v in page_size_d2.items() if v[0]>tes_w and v[1]>tes_h}
# d_len = len(new_dict)
# d2l = zip(new_dict.keys(), new_dict.values()) # 字典转换成元组组成的列表 [...(u'pagesize4', (880, 650, 572000, 1.353846153846154))...]
# d2l_sorted = sorted(d2l, key=lambda x: x[1][2]) # 以面积之和作为排序的值
# if d_len > 2:
#     # _dict2 = dict(d2l_sorted[:2])
#     two_remaind = d2l_sorted[:2]
#     print(two_remaind)
#     dd = min(two_remaind, key=lambda x: abs(x[1][3]-tes_div))
#     print(dd) # (u'pagesize1', (1180, 950, 1121000, 1.2421052631578948))
# elif d_len==1:
#     print(d2l_sorted[0][0])

def select_template_size(size, template_size):
    """
    
    :param size:  such as:[659.8490915000066, 822.3146429999917]
    :param template_size: 制图模板大小
    :return: 返回制图模板大小的名称（键），如果找不到适合的制图模板就返回 -1
    """
    map_w, map_h = size[0], size[1]
    map_div = map_w/map_h
    # 符合该制图单位的模板大小的字典
    template_size_fit = {k:(v[0], v[1], v[0]*v[1], v[0]/v[1]) for k,v in template_size.items() if v[0]>map_w and v[1]>map_h}
    d_len = len(template_size_fit)
    d2l = zip(template_size_fit.keys(), template_size_fit.values()) # 字典转列表
    d2l_sorted = sorted(d2l, key=lambda x: x[1][2]) # 按元组中第三个数大小排序
    if d_len > 2:
        two_remaind = d2l_sorted[:2]
        print(two_remaind)
        res = min(two_remaind, key=lambda x: abs(x[1][3]-map_div)) # (u'pagesize3', (1380, 850, 1173000, 1.6235294117647059))
        return res[0]
    elif d_len==2:
        res = d2l_sorted[0]
        return res[0]
    elif d_len==1:
        return d2l_sorted[0][0]
    else:
        # info="存在超出页面大小的制图单位!"
        return -1
    


# new_tup = [(u'pagesize4', (880, 650, 572000, 1.353846153846154)), (u'pagesize1', (1180, 950, 1121000, 1.2421052631578948)), (u'pagesize3', (1380, 850, 1173000, 1.6235294117647059)), (u'pagesize2', (1180, 1350, 1593000, 0.8740740740740741))]
# new_tup_sorted = sorted(new_tup, key=lambda tup: tup[1][2])

# if len(feasible_page) >2:
#     new_tup = zip(page_size_d2.keys(), page_size_d2.values())
#
#     print(new_tup_sorted)
#
# elif len(feasible_page) == 2:
#     pass
# elif len(feasible_page) == 1:
#     pass
# else:
#     print("存在超出页面大小的制图单位!")


"""
[659.8490915000066, 822.3146429999917]
[745.6436624999996, 894.4534104999899]
[884.2221694999934, 1113.4568605000059]
[651.0624269999936, 655.3824560000003]
[448.7290259999968, 657.0491914999858]
[775.5384144999925, 1009.642475499995]
"""
"""____________________________global_values_________________________________"""
"""__________________________________________________________________________"""
arcpy.env.overwriteOutput = True
arcpy.env.workspace = gdb_path

def check_field(layer, field):
    return field in arcpy.ListFields(layer)
    


class PageSizeMatch(object):
    """
    适配页面大小
    """
    def __init__(self, mapdocument):
        # self.mxd = mapdocument
        # self.mapping_index_layer = arcpy.mapping.ListLayers(self.mxd, "MappingIndex")[0] #  图层要素 用于设置定义查询 以匹配大小
        
        self.minimum_bounding()
        # self.page_size(SCALE)
        self.check_width_height()
        
    @staticmethod
    def minimum_bounding():
        """
        计算最小边界几何，并用结果图层覆盖初始图层;计算过最小边界几何的图层有"MBG_Width"字段
        创建PAGRSIZE 字段
        :return: 制图索引文件的要素图层
        """
        if not check_field(MI,"MBG_Width"): # 没有计算过最小几何边界
            print("NO MBG_Width")
            short_f = arcpy.MinimumBoundingGeometry_management
            # arcpy.MinimumBoundingGeometry_management(MI,
            #                                          "mapping_index_out",
            #                                          "ENVELOPE",
            #                                          "LIST",
            #                                          FIELD,
            #                                          True)
            short_f(MI, "mapping_index_out", "ENVELOPE", "LIST", FIELD, True)
            arcpy.Delete_management(MI, "FeatureClass")
            arcpy.Rename_management("mapping_index_out", MI, "FeatureClass")
        if not check_field(MI,"PAGESIZE"): # 没有计算过最小几何边界
            arcpy.AddField_management(MI, "PAGESIZE", "TEXT", field_length = 100)
        print("minimum_bounding")

    def check_width_height(self, ):
        short_f = arcpy.FeatureVerticesToPoints_management
        # 要素折叠转点要素
        feature_vertices = "feature_vertices"
        # short_f(self.mapping_index_layer, feature_vertices, "ALL") # ERROR 000840: 该值不是 要素图层。
        short_f(MI, feature_vertices, "ALL")
        cursor = arcpy.da.SearchCursor(feature_vertices, [FIELD, "SHAPE@Y"])
        cursor_l = [(x[0], x[1]) for x in cursor]
        # 仅将前两位、6 7位、11 12.. 取出组成列表
        # 前两位（右下角的点，右上角的点，y坐标的差值就是高 height）
        height_info = zip(cursor_l[::5], cursor_l[1::5])
        for k ,v in height_info:
            print(k[0], k[1],v[0], v[1])
        print(height_info)
        
        
        # with arcpy.da.SearchCursor(feature_vertices, [FIELD, "SHAPE@Y"]) as cursor:
        #     for key_f, height in cursor:
        #         if key_f
            #     pass
                
        
    
    def page_size(self, scale):
        with arcpy.da.UpdateCursor(MI, ["MBG_Width", "MBG_Length"]) as cursor:
            for row in cursor:
                # width = row[0]
                # length = row[1]
                new_row = [x/scale*1000 for x in row] # 单位换算成了毫米 mm [659.8490915000066, 822.3146429999917]
                print(new_row)
                # res = select_template_size(new_row, page_size_d)
                # print(res)
        
        
class MakeMXD(object):
    
    def __init__(self, mapdocument, layers):
        """
        :param mapdocument: {Object} MXD文件对象
        :param layers: {List} 需要设置定义查询语句图层的名称列表
        """
        self.mxd = mapdocument
        self.df = arcpy.mapping.ListDataFrames(self.mxd)[0]
        self.layers = layers
        self.mapping_index_layer = arcpy.mapping.ListLayers(self.mxd, MI)[0]
        self.make_mxd()
        
    def make_mxd(self):
        with arcpy.da.SearchCursor(self.mapping_index_layer,FIELD) as cursor:
            for row in cursor: # 提前解包？
                name = row[0]
                self.define_query(name) # 定义查询
                self.center_scale(name) # 居中
                arcpy.SelectLayerByAttribute_management(self.mapping_index_layer, "CLEAR_SELECTION") # 取消该图层的所有选择选择项目
                self.saveacopy(name) # 另存
    
    def define_query(self, value):
        """
        定义查询
        :param value: {String/Int/Float} 用于定义查询的值
        :return: None
        """
        for layer in self.layers:
            print(layer)
            lyr = arcpy.mapping.ListLayers(self.mxd, layer)[0]
            d_q = ['"',FIELD,'"'," = ","'",value,"'"]
            # lyr.definitionQuery = '"' + FIELD + '"' + " = " + "'" + value + "'"
            lyr.definitionQuery = "".join(d_q)
    
    def center_scale(self, name):
        """
        使图框居中并设置比例尺
        :param name: {String/Int/Float} 用于查询语句的值
        :return: None
        """
        where_clause = "NEW_SELECTION", "{} = '{}'".format(FIELD, name)
        arcpy.SelectLayerByAttribute_management(self.mapping_index_layer,where_clause)
        self.df.extent = self.mapping_index_layer.getSelectedExtent()
        if SCALE:
            self.df.scale = SCALE
        
        
    def saveacopy(self, name):
        self.mxd.saveACopy(output_dir+'/'+name+'.mxd')
        print("save complete: ",name)
        

# mxd = arcpy.mapping.MapDocument("CURRENT")
mxd = arcpy.mapping.MapDocument(r"E:\doc\Scratch\tempMXDS\880x650.mxd")
PageSizeMatch(mxd)
# MakeMXD(mxd,["roads","railways","landuse"])

