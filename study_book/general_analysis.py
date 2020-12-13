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
from os import path,mkdir


excel_path = '耕地质量变更调查表.xls'
sheet = pd.read_excel(excel_path, sheet_name=0)
col_names = ['pH','有机质','土壤容重','有效磷','速效钾',"有效土层厚"]
target_data = pd.DataFrame(sheet, columns=col_names)
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

# 使用describe() 方法可以快速获取数据的基本信息
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
# 变异系数（标准差/平均值）
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
# 将变异系数加入表中
data_table=target_data.append(data_cv)

"""__________________________________________________________________________"""
"""________________________________data table________________________________"""
# 保留一位小数 输出表
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
"""______________________________data describe_______________________________"""

list1=[]
for index,row in data_table.T.iterrows():
	info = "{0}变化范围为{1}-{2}，均值为{3}，中位数为{4}，标准差为{5}，变异系数为{6}%；".format(
		index,row['最小值'],row['最大值'],row['平均值'],row['中位数'],row['标准差'],row['变异系数（%）'])
	list1.append(info)
# 拼接字符串
data_describe= ''.join(list1)
print(data_describe)
"""
文字输出示例如下：
pH变化范围为5.0-8.9，均值为7.6，中位数为7.7，标准差为0.7，变异系数为9.2%；
有机质变化范围为11.1-80.0，均值为41.9，中位数为42.0，标准差为14.0，变异系数为33.4%；
土壤容重变化范围为0.9-1.7，均值为1.4，中位数为1.4，标准差为0.1，变异系数为7.1%；
有效磷变化范围为2.2-92.6，均值为23.6，中位数为16.4，标准差为21.2，变异系数为89.8%；
速效钾变化范围为49.0-350.0，均值为193.3，中位数为173.0，标准差为84.0，变异系数为43.5%；
有效土层厚变化范围为33.0-160.0，均值为70.6，中位数为67.0，标准差为22.2，变异系数为31.4%；
"""



"""__________________________________________________________________________"""
"""_______________________________make chart_________________________________"""
import plotly.express as px

"""-------------------------------point chart--------------------------------"""
class PlotChart(object):
	def __init__(self, output_image=True, output="image"):
		"""
		:param output_image: {Boolean} Ture: output image; False: output html
		:param output: {String} output path
		"""
		self.output_image = output_image
		self.output = output
		self.width = 550
		self.height = 600
		self.image_format = ".png"
		if not path.exists(self.output):
			mkdir(self.output)
	
	def create_chart(self, fig, name):
		"""
		:param fig: (PLotlt) 生成的PLotlt对象
		:param name: 名字
		:return:
		"""
		if self.output_image:
			# 输出图像
			fig.write_image("images//"+name+self.image_format, scale=3)
		else:
			# 输出交互式web版
			fig.write_html(name+'.html', auto_open=True)


class ViolinStripChart(PlotChart):
	"""
	小提琴点图
	"""
	def __init__(self, data, y):
		PlotChart.__init__(self)
		self.data = data
		self.y = y
		self.title = "{}含量分布点图".format(self.y)
		fig = self.create_fig()
		self.create_chart(fig, self.title)
		
		
	def create_fig(self):
		fig = px.strip(self.data, y=self.y, width=self.width, height=self.height,
					   title="{}含量分布点图".format(self.y))
		return fig
	
for y in col_names:
	ViolinStripChart(raw_data,y)


#
# """__________________________________________________________________________"""
# """_______________________________make chart_________________________________"""
# import plotly.express as px
#
# """-------------------------------point chart--------------------------------"""
#
#
# def violin_strip_chart(data, y_axis, width=550, height=600, image_form="png"):
# 	"""
# 	基于 plotly 绘制一维数据的分布点图（类似于小提琴图）
# 	reference: https://plotly.com/python/static-image-export/
# 	:param data: {Dataframe，Array}
# 	:param y_axis: {String} 列名
# 	:param width: {Int}
# 	:param height: {Int}
# 	:param image_form: {String} "png" "jpeg" ...
# 	"""
# 	fig = px.strip(data, y=y_axis, width=width, height=height,
# 				   title="{}含量分布点图".format(y_axis))
# 	# fig.write_html('first_figure2.html', auto_open=True)
# 	if not path.exists("images"):
# 		mkdir("images")
# 	name = "{}.{}".format(y_axis, image_form)
# 	# 输出图片
# 	fig.write_image("images//" + name, scale=3)
#
#
# # fig.write_image("images/fig1.png")
#
# for y in col_names:
# 	violin_strip_chart(raw_data, y)