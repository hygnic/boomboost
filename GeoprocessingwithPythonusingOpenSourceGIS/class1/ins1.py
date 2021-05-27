# -*- coding:utf-8 -*-
# -------------------------------------------
# Name:              ins1
# Author:            Hygnic
# Created on:        2021/5/27 15:45
# Version:           
# Reference:         
"""
Description:         
Usage:               
"""
# -------------------------------------------
import sys
try:
    from osgeo import ogr
except:
    import ogr


driver = ogr.GetDriverByName('ESRI Shapefile')
fn = "../ospy_data1/sites.shp"

dataSource = driver.Open(fn, 0)

if dataSource is None:
    print('Could not open ' + fn)
    sys.exit(1) #exit with an error code
    
layer = dataSource.GetLayer()
print("Features Count:{}".format(layer.GetFeatureCount()))
print("Features Extent:{}".format(layer.GetExtent()))

#       Getting features

feature = layer.GetFeature(1)
#       Loop
# feature = layer.GetNextFeature()
# while feature:
#     # do something here
#     feature = layer.GetNextFeature()
    # layer.ResetReading() #need if looping again

#       Getting feature’s attributes

fid = feature.GetField("id")
cover = feature.GetField("cover")
print("cover: ", cover)

geometry = feature.GetGeometryRef()
print(geometry.GetX())
print(geometry.GetY())