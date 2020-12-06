#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/11/9 16:45
# Reference:
"""
Description: 对耕地质量等级点位表进行基本分析 统计最值、标准差、变异系数等
Usage:
"""
# ---------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
from os import chdir,path,mkdir

current_path = '.'
chdir(current_path)

excel_path = '耕地质量变更调查表.xls'
sheet = pd.read_excel(excel_path,sheet_name=0)
col_names = ['pH','有机质','土壤容重','有效磷','速效钾',"有效土层厚"]
target_data = pd.DataFrame(sheet,columns = col_names)
raw_data = target_data
"""
      pH   有机质  土壤容重   有效磷  速效钾
0    7.1  64.0  1.04  38.7  310
1    7.8  68.6  1.08  82.6  284
2    8.1  42.7  1.10  30.8   63
3    8.0  40.5  0.92  26.4  100
4    7.7  38.8  1.34  62.8  118
..   ...   ...   ...   ...  ...
"""


"""__________________________________________________________________________"""
"""________________________________数据表_____________________________________"""


target_data = target_data.describe()
"""
               pH         有机质        土壤容重         有效磷         速效钾
count  133.000000  133.000000  133.000000  133.000000  133.000000
mean     7.658647   41.115789    1.370376   24.930075  189.661654
std      0.739075   14.504361    0.147589   21.849274   82.606028
min      5.000000   11.100000    0.920000    2.200000   49.000000
25%      7.400000   29.600000    1.270000    8.800000  127.000000
50%      7.800000   41.300000    1.370000   18.200000  173.000000
75%      8.100000   50.200000    1.470000   31.300000  250.000000
max      8.900000   80.000000    1.690000   92.600000  350.000000
"""

# 移动位置&保留一位小数
target_data = target_data.reindex(['min','max','50%','mean','std']).round(1)
# 重命名
target_data = target_data.rename(index={'min':'最小值','max':'最大值','50%':'中位数','mean':'平均值','std':'标准差'})
# 变异系数
data_cv=(target_data.loc['标准差',:])/(target_data.loc['平均值',:])
data_cv.name = '变异系数（%）' # 添加 serise 名称
"""
pH      0.096502
有机质     0.352769
土壤容重    0.107699
有效磷     0.876422
速效钾     0.435544
Name: 变异系数,dtype: float64
"""
data_cv =(data_cv*100).round(1)
data_table=target_data.append(data_cv)

# 保留一位小数
data_table.to_csv("data.csv", sep=",", index=True, encoding="cp936")
"""
          pH   有机质  土壤容重   有效磷    速效钾
最小值      5.0  11.1   0.9   2.2   49.0
最大值      8.9  80.0   1.7  92.6  350.0
中位数      7.7  42.0   1.4  16.4  173.0
平均值      7.6  41.9   1.4  23.6  193.3
标准差      0.7  14.0   0.1  21.2   84.0
变异系数（%）  9.2  33.4   7.1  89.8   43.5
"""

"""__________________________________________________________________________"""
"""_______________________________数据描述____________________________________"""

list1=[]
for index,row in data_table.T.iterrows():
	info = "{0}变化范围为{1}-{2}，均值为{3}，变异系数为{4}%；".format(
		index,row['最小值'],row['最大值'],row['平均值'],row['变异系数（%）'])
	list1.append(info)
# 拼接字符串
data_describe= ''.join(list1)
"""
pH变化范围为5.0-8.9，均值为7.6，变异系数为9.2%；有机质变化范围为11.1-80.0，均值为41.9，
变异系数为33.4%；土壤容重变化范围为0.9-1.7，均值为1.4，变异系数为7.1%；有效磷变化范围
为2.2-92.6，均值为23.6，变异系数为89.8%；速效钾变化范围为49.0-350.0，均值为193.3，
变异系数为43.5%；
"""



"""__________________________________________________________________________"""
"""_______________________________绘制图形____________________________________"""
import plotly.graph_objects as go
import plotly.express as px

"""-------------------------------点图---------------------------------------"""


def violin_strip_chart(data,y_axis,width=550, height=600,image_form = "png"):
	"""
	基于 plotly 绘制一维数据的分布点图（类似于小提琴图）
	reference: https://plotly.com/python/static-image-export/
	:param data: {Dataframe，Array}
	:param y_axis: {String} 列名
	:param width: {Int}
	:param height: {Int}
	:param image_form: {String} "png" "jpeg" ...
	"""
	fig = px.strip(data, y=y_axis,width=width, height=height,
					title="{}含量分布点图".format(y_axis))
	# fig.write_html('first_figure2.html', auto_open=True)
	if not path.exists("images"):
		mkdir("images")
	name = "{}.{}".format(y_axis,image_form)
	# 输出图片
	fig.write_image("images//"+name, scale=3)
	# fig.write_image("images/fig1.png")
	
for a_c in col_names:
	violin_strip_chart(raw_data,a_c)