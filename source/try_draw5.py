# -*- coding: UTF-8 -*-

# Filename : try_draw5.py
# author by : （学员ID)

# 目的： 了解离散统计函数的意义和使用方法
#

import os
import sys
import io

# import pandas as pd

import numpy as np
import matplotlib.pylab as plt
import random
# 引入统计函数包
from scipy.stats import *

# 解决输出显示汉字乱码的问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# print (sys.stdout.encoding)  # 确认当前的控制台显示字符的编码
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号


# 练习一： 正态分布
fig,ax = plt.subplots(1,1)

# 所有连续分布 loc 和 scale 作为关键字参数来调整分布的位置和规模，
# 例如，对于标准正态分布，位置是平均值，尺度是标准差。
# 正态分布定义
# 若随机变量X服从一个数学期望为μ、方差为σ^2的正态分布，记为N(μ，σ^2)。
# 其概率密度函数为正态分布的期望值μ决定了其位置，其标准差σ决定了分布的幅度。
# 当μ = 0,σ = 1时的正态分布是标准正态分布。

loc = 38
scale = 8.0
#平均值, 方差, 偏度, 峰度
mean,var,skew,kurt = norm.stats(loc,scale,moments='mvsk')
print(mean,var,skew,kurt)
#ppf:累积分布函数的反函数。q=0.01时，ppf就是p(X<x)=0.01时的x值。
start = norm.ppf(0.01,loc,scale)
ending = norm.ppf(0.99,loc,scale)
numbers = 10000
x = np.linspace(start, ending, numbers)
y = norm.pdf(x, loc, scale)

ax.plot(x, y, 'ro', label = '正态分布')
plt.title(u'正太分布概率密度函数 norm')


# 练习二：随机取值（年龄）
fig = plt.figure(2)
# 设定年龄上限和下限
max_age = 60
min_age = 16

# 生成 x 轴坐标序列
x = []
for i in range(min_age, max_age+1):
    x.append(str(i))

# 生成 y 轴坐标序列 = 每个年龄的人数总和
count = [0] * (max_age - min_age + 1)  # 数组初始化，注意个数
numbers = 10
for i in range(numbers): # 随机生成 numbers 次
    age = random.randint(min_age, max_age)  # 在指定的年龄段内获取年龄
y = count

#print(x)
#print(y)
plt.bar(x, y)


plt.show()