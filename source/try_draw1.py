# -*- coding: UTF-8 -*-

# Filename : try_draw1.py
# author by : （学员ID)

# 目的： 学会初步用 python 绘点图，线图的方法
#       初步了解数列绘图原理
#       初步了解制作数列的 2种方法， for 以及 np.arange
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


# 练习一：绘制一张简单的点图
x = 5
y = 5
# plt.plot(x, y, 'bo')
# plt.show()

# 练习二：列出所有颜色和点的搭配
s_color = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
s_marker = ['.' ,',' ,'o' ,'v' ,'^' ,'<' ,'>' ,'1' ,'2' ,'3' ,'4' ,'s' ,'p' ,'*' ,'h' ,'H' ,'+' ,'x' ,'D' ,'d' ,'|' ,'_' ]
s_line = ['-', '--', '-.', ':']

x = 1
y = 1
for sc in s_color:
    for sm in s_marker:
        x += 1
        y += 1
        fmt = sc + sm
        plt.plot(x, y, fmt, linewidth=1, markersize=6)
# plt.show()

# 练习三：完整的调用方式(点)
#plt.plot(x, y, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12)

# 练习三：用一组数的列表画点图
x = [1,3,5,7]
y = [2,4,6,8]
#plt.plot(x, y, 'ro')
#plt.axis([0, 10, 0, 10])

# 练习四：用一组数的列表画线图
x = [1,2,3]
y = [1,2,3]
fmt = 'go-'
#plt.plot(x, y, fmt, linewidth=3)
x = [4,5,6]
y = [4,5,6]
fmt = 'rs--'
#plt.plot(x, y, fmt, linewidth=3)

# 练习五： 用点+线近似绘制函数 y = ax^2 + bx + c
a = 1.5
b = 2.3
c = -3.7
fmt = 'ro--'
for x in range(0, 20):
    y = a * x **2 + b * x + c
#    plt.plot(x, y, fmt, linewidth=2)

# 练习六： 使用 np.arange
fmt = 'bs--'
x1 = np.arange(0, 10, 0.5)
y1 = a * x1 **2 + b * x1 + c
#plt.plot(x1, y1, fmt, linewidth=2)
print(x1)

plt.show()
