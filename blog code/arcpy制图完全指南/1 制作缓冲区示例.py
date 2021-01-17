# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2021/1/17 14:53

import arcpy
import os

class InitPath(object):
    """初始化工作空间，创建gdb数据库（如果没有的话）"""
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            # if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance
    def __init__(self):
        """_________________________create folder____________________________"""
        scratch_path = "D:\doc\Scratch"
        try:
            if not os.path.isdir(scratch_path):
                os.makedirs(scratch_path)
        except:
            scratch_path = "E:\doc\Scratch"
            if not os.path.isdir(scratch_path):
                os.makedirs(scratch_path)
        """_________________________create folder____________________________"""
        # make gdb
        scratch_gdb = os.path.join(scratch_path, "Scratch.gdb")
        if not arcpy.Exists(scratch_gdb):
            arcpy.CreateFileGDB_management(scratch_path, "Scratch")
        arcpy.env.workspace = scratch_path
        arcpy.env.overwriteOutput = True
        
        self.scratch_path = scratch_path
        self.scratch_gdb = scratch_gdb
    
    def __iter__(self):
        return (i for i in (self.scratch_path, self.scratch_gdb))

folder_path, gdb_path = InitPath()
arcpy.env.workspace = gdb_path
arcpy.env.overwriteOutput = True