# -*- coding: UTF-8 -*-

# Filename : try_draw4.py
# author by : （学员ID)

# 目的： 进一步了解制作数列的 np.arange
#

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

# 练习一 ： 用 三位数方式画 9个图 (限制，图的个数必须小于10， 只能1-9)
x = np.arange(1, 10, 1)
y = 1.5 * x **2 + 3 * x + 3

plt.figure(1)
position = ''
seq = 0
nrows = 3
ncols = 3
for seq in range(1, nrows*ncols+1):
    position = str(nrows) + str(ncols) + str(seq)
    plt.subplot(int(position))
    plt.plot(x, y, 'ro')


# 练习二： 用数组方式画 n 个图
nrows = 5
ncols = 6
fig, axs = plt.subplots(nrows, ncols)

for i in range(nrows):
    for j in range(ncols):
        axs[i, j].plot(x, y, 'b^')


# 练习三： 为每个小图加上固定的标签
nrows = 5
ncols = 6
fig, axs = plt.subplots(nrows, ncols)

# 定义轴标签
box_x = dict(facecolor='blue', pad=5, alpha=0.2)
box_y = dict(facecolor='green', pad=5, alpha=0.2)

# 循环作图
for i in range(nrows):
    for j in range(ncols):
        axs[i, j].plot(x, y, 'g--')
        title = (" 图(%d - %d)" % (i + 1, j + 1))
        axs[i, j].set_title(title)
        axs[i, j].set_xlabel(' 我是x轴标签 ', bbox=box_x)
        axs[i, j].set_ylabel(' 我是y轴标签 ', bbox=box_y)

# 调整各子图之间的间距
fig.subplots_adjust(left=0.2, wspace=0.6)

plt.show()
