# -*- coding: UTF-8 -*-

# Filename : try_draw3.py
# author by : （学员ID)

# 目的： 进一步了解制作数列的 np.arange
#       学会使用 subplot 制作多图

import os
import sys
import io

# import pandas as pd

import numpy as np
import matplotlib.pylab as plt

# 解决输出显示汉字乱码的问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# print (sys.stdout.encoding)  # 确认当前的控制台显示字符的编码
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号


# 练习一： 在一张图上 分上下两个图显示  fig-1
x = np.arange(0.0, 1.0, 0.01)
y1 = np.sin(2*np.pi*x)
y2 = np.cos(2*np.pi*x)

plt.figure(1)
plt.subplot(211)
plt.plot(x, y1, 'ro')
plt.title(' X 轴 - sin()')
plt.ylabel(' Y 轴 ')
plt.grid(True)


plt.subplot(212)
plt.plot(x, y2, 'go')
plt.xlabel(' X 轴 - cos()')
plt.ylabel(' Y 轴 ')
plt.grid(True)

# 练习二： 同时画2张图 fig-2
plt.figure(2)
plt.plot(x, y1, 'b^')

plt.figure(3)
plt.plot(x, y2, 'b^')

#练习三： 用  subplot 画1张图 fig-3,4,5,6
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

#Creates just a figure and only one subplot
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('第一张图：一个简单的 plot')

#练习四： 用  subplot 画 2张图，并共享 y 轴， 放大函数
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(x, y)
ax1.set_title('第二张图：共享 Y 轴')
#ax2.scatter(x, y)
ax2.plot(x, 2*y, 'b-')

#练习五： 用  subplot 画4张图， axes 数组方式， 4个不同函数
fig, axes = plt.subplots(2, 2)
#plt.subplots(2, 2, sharex='col')
x = np.linspace(0, 10, 100)
y01 = 5 * x + 3
axes[0, 0].set_title('一次函数型增长：y=ax+b ')
axes[0, 0].plot(x, y01)

y02 = 1.5*x**2 - 5*x - 10
axes[0, 1].set_title('二次函数型增长：y=ax^2+bx+c ')
axes[0, 1].plot(x, y02)

y03 = 0.5*x**3 -2*x**2 + 1.5*x -25
axes[1, 0].set_title('三次函数型增长：y=ax^3+bx^2+cx+d ')
axes[1, 0].plot(x, y03)

y04 = np.exp(x)
axes[1, 1].set_title('指数型增长：y=exp(x) ')
axes[1, 1].plot(x, y04)

"""
#Share a X axis with each column of subplots
plt.subplots(2, 2, sharex='col')

#Share a Y axis with each row of subplots
plt.subplots(2, 2, sharey='row')

#Share both X and Y axes with all subplots
plt.subplots(2, 2, sharex='all', sharey='all')

#Note that this is the same as
plt.subplots(2, 2, sharex=True, sharey=True)

#Creates figure number 10 with a single subplot
#and clears it if it already exists.
fig, ax=plt.subplots(num=10, clear=True)

"""
plt.show()
