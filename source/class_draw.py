# -*- coding: UTF-8 -*-

# Filename : class_draw.py
# author by : （学员ID)

# 目的： 学会初步用 python 绘图的方法
#
# 配套练习
#       try_draw.def

import os
import sys
import io

# import pandas as pd

import numpy as np
import matplotlib.pylab as plt

# 解决输出显示汉字乱码的问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# print (sys.stdout.encoding)  # 确认当前的控制台显示字符的编码
