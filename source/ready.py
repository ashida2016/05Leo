# -*- coding: UTF-8 -*-

# Filename : ready.py
# author by : （学员ID)

# 目的： 学会初步用 python 绘图的方法
#       加深理解 numpy

import os
import sys
import io

# import pandas as pd

import numpy as np
import matplotlib.pylab as plt


# 解决输出显示汉字乱码的问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# print (sys.stdout.encoding)  # 确认当前的控制台显示字符的编码

# 练习一：用 numpy 制作序列
print("---练习一---")

# 指定起点，终点，步长的方式
print("设定 起点->终点 +步长 的方式：")
print(np.arange(3)) # 默认起点为0
print(np.arange(3,7))
print(np.arange(3,9,2))
print(np.arange(10,11,0.1))

# 指定起点，终点，总样本数的方式
print("\n设定 起点->终点 +总样本数 的方式：")
print(np.linspace(1, 10, 10, endpoint=True))
print(np.linspace(1, 10, 10, endpoint=False))

# 练习二：画出一个简单函数（初中，高中数学公式范围内）
print("---练习二---")
x = np.arange(1, 10)
y = 5 * x + 3
plt.plot(x, y)
plt.show()

x = np.arange(1, 10)
y = 1.5 * x **2 + 3 * x + 3
plt.plot(x, y)
plt.show()

x = np.linspace(-np.pi, np.pi, 100, endpoint=True)
y = np.sin(x)
plt.plot(x, y)
plt.show()

# 练习三： 在同一个图上画2个简单函数
x = np.arange(1, 10)

y = 5 * x + 3
z = 1.5 * x **2 + 3 * x + 3
p = 1.5 * x **3 - 2.2 * x **2 + 5 * x - 2
plt.plot(x, y)
plt.plot(x, z)
plt.plot(x, p)
plt.show()
