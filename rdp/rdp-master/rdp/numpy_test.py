# -*- coding:utf-8 -*-
# -------------------------------------------
# Name:              numpy_test
# Author:            Hygnic
# Created on:        2021/5/18 10:34
# Version:           
# Reference:         
"""
Description:         
Usage:               
"""
# -------------------------------------------
from pprint import pprint
import numpy as np

array = np.array([44, 95, 26, 91, 22, 90, 21, 90,
              19, 89, 17, 89, 15, 87, 15, 86, 16, 85,
              20, 83, 26, 81, 28, 80, 30, 79, 32, 74,
              32, 72, 33, 71, 34, 70, 38, 68, 43, 66,
              49, 64, 52, 63, 52, 62, 53, 59, 54, 57,
              56, 56, 57, 56, 58, 56, 59, 56, 60, 56,
              61, 55, 61, 55, 63, 55, 64, 55, 65, 54,
              67, 54, 68, 54, 76, 53, 82, 52, 84, 52,
              87, 51, 91, 51, 93, 51, 95, 51, 98, 50,
              105, 50, 113, 49, 120, 48, 127, 48, 131, 47,
              134, 47, 137, 47, 139, 47, 140, 47, 142, 47,
              145, 46, 148, 46, 152, 46, 154, 46, 155, 46,
              159, 46, 160, 46, 165, 46, 168, 46, 169, 45,
              171, 45, 173, 45, 176, 45, 182, 45, 190, 44,
              204, 43, 204, 43, 207, 43, 215, 40, 215, 38,
              215, 37, 200, 37, 195, 41]).reshape(77, 2)

print("size:{}".format(array.size))
print("shape:{}".format(array.shape))
# pprint(array)
pprint(np.ones(1))

def pldist(point, start, end):
    """
    Calculates the distance from ``point`` to the line given
    by the points ``start`` and ``end``.

    :param point: a point
    :type point: numpy array
    :param start: a point of the line
    :type start: numpy array
    :param end: another point of the line
    :type end: numpy array
    """
    if np.all(np.equal(start, end)):
        print(1)
        return np.linalg.norm(point - start)
    
    # return np.true_divide(
    return np.divide(
        np.abs(np.linalg.norm(np.cross(end - start, start - point))),
        np.linalg.norm(end - start))


print(array[1])
print(array[0])
print(array[-1])
print(pldist(array[1], array[0], array[-1])) # 9.827568072408992


'''result:
size:154
shape:(77, 2)
array([[ 44,  95],
       [ 26,  91],
       [ 22,  90],
       [ 21,  90],
       [ 19,  89],
       [ 17,  89],
       [ 15,  87],
       [ 15,  86],
       [ 16,  85],
       [ 20,  83],
       [ 26,  81],
       [ 28,  80],
       [ 30,  79],
       [ 32,  74],
       [ 32,  72],
       [ 33,  71],
       [ 34,  70],
       [ 38,  68],
       [ 43,  66],
       [ 49,  64],
       [ 52,  63],
       [ 52,  62],
       [ 53,  59],
       [ 54,  57],
       [ 56,  56],
       [ 57,  56],
       [ 58,  56],
       [ 59,  56],
       [ 60,  56],
       [ 61,  55],
       [ 61,  55],
       [ 63,  55],
       [ 64,  55],
       [ 65,  54],
       [ 67,  54],
       [ 68,  54],
       [ 76,  53],
       [ 82,  52],
       [ 84,  52],
       [ 87,  51],
       [ 91,  51],
       [ 93,  51],
       [ 95,  51],
       [ 98,  50],
       [105,  50],
       [113,  49],
       [120,  48],
       [127,  48],
       [131,  47],
       [134,  47],
       [137,  47],
       [139,  47],
       [140,  47],
       [142,  47],
       [145,  46],
       [148,  46],
       [152,  46],
       [154,  46],
       [155,  46],
       [159,  46],
       [160,  46],
       [165,  46],
       [168,  46],
       [169,  45],
       [171,  45],
       [173,  45],
       [176,  45],
       [182,  45],
       [190,  44],
       [204,  43],
       [204,  43],
       [207,  43],
       [215,  40],
       [215,  38],
       [215,  37],
       [200,  37],
       [195,  41]])

'''