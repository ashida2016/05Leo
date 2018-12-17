# -*- coding: UTF-8 -*-

# Filename : try_draw2.py
# author by : （学员ID)

# 目的： 进一步了解制作数列的 np.arange
#       了解为图加说明及限制区域的方法

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


# 练习一：进一步了解 np.arange, 用 numpy 制作序列
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
#plt.plot(x, y)

x = np.arange(1, 10)
y = 1.5 * x **2 + 3 * x + 3
#plt.plot(x, y)

x = np.linspace(-np.pi, np.pi, 100, endpoint=True)
y = np.sin(x)
#plt.plot(x, y)

# 练习三： 在同一个图上画2个简单函数
x = np.arange(1, 10, 0.3)

y = 5 * x + 3
z = 1.5 * x **2 + 3 * x + 3
p = 1.5 * x **3 - 2.2 * x **2 + 5 * x - 2
#plt.plot(x, y, 'r--')
#plt.plot(x, z, 'bs')
#plt.plot(x, p, 'g^')

# 练习四： 随机数点图
x = np.random.rand(20)
y = np.random.rand(20)
fmt = 'ro'
#plt.plot(x, y, fmt)

# 练习五： 复杂函数
x = np.arange(0.1, 5.0, 0.1)
y = np.exp(x)
fmt = 'ro'
plt.plot(x, y, fmt)

# 练习五： 加上横轴纵轴说明
plt.xlabel(' X 轴 ')
plt.ylabel(' Y 轴 ')
plt.title('自然对数图形')
plt.grid(True)

# 练习六： 控制大小
#plt.axis([0, 6, 0, 20])


plt.show()
