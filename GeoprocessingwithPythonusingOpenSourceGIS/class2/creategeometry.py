# -*- coding:utf-8 -*-
# -------------------------------------------
# Name:              creategeometry
# Author:            Hygnic
# Created on:        2021/5/27 22:53
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


#       Create New SHP
driver = ogr.GetDriverByName('ESRI Shapefile')
pointds = driver.CreateDataSource("test.shp")
layer = pointds.CreateLayer('test', geom_type=ogr.wkbLineString)

#       Create New Field
fieldDefn = ogr.FieldDefn('name', ogr.OFTString)
fieldDefn.SetWidth(30)
# Add field to the shp
layer.CreateField(fieldDefn)


#       Add Geometry
line = ogr.Geometry(ogr.wkbLineString)
line.AddPoint(10, 20)
line.AddPoint(18, 58)
# line.SetPoint(0, 20, 89)

featureDefn = layer.GetLayerDefn()
feature = ogr.Feature(featureDefn)
# feature.SetGeometryDirectly(line)
feature.SetGeometry(line)
layer.CreateFeature(feature)