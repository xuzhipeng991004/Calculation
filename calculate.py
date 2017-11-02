# -*- coding:utf-8 -*-

import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from scipy import interpolate
from scipy.optimize import fsolve

matplotlib.rcParams['font.sans-serif'] = ['SimHei']   # 指定默认字体
matplotlib.rcParams['axes.unicode_minus'] = False   # 解决保存图像是负号'-'显示为方块的问题


# 主要用pyplot显示绘图
years = np.linspace(1950, 2010, 7)
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, gdp, color="green", marker="o", linestyle="solid")
plt.title("名义GDP")

plt.ylabel("十亿美元")
plt.xlabel("年份")
# plt.show()


# 练习文件的基本操作
a = np.arange(1, 13)
a.shape = 3, 4
np.savetxt("a.txt", a, fmt="%d", delimiter=", ")

f = open("a.txt", 'rb')
file = np.loadtxt(f, delimiter=", ")
print(file)
f.close()


# 利用fsolve函数进行解方程
def func(x):
    x0 = float(x[0])
    x1 = float(x[1])
    x2 = float(x[2])
    return [x0 + x1 * np.sin(4) + x2 - 2,
            2 * x0 + np.sin(3) * x1 + 4 * x2 - 1,
            3 * x0 + x1 + 3 * x2 - 3]


f = fsolve(func, np.zeros([1, 3]))
print(f)


# 对散点进行线性和样条曲线拟合
x = np.linspace(0, 2*np.pi+np.pi/4, 10)
y = np.sin(x)

x_new = np.linspace(0, 2*np.pi+np.pi/4, 100)
f_linear = interpolate.interp1d(x, y)
tck = interpolate.splrep(x, y)
y_bspline = interpolate.splev(x_new, tck)


plt.figure()
plt.plot(x, y, "o", label="原始数据", color="r")
plt.plot(x_new, f_linear(x_new), label="线性插值", color="g")
plt.plot(x_new, y_bspline, label="B-spline插值", color="b")
plt.xlabel("x轴数据", fontsize=14)
plt.ylabel("y轴数据", fontsize=14)
plt.title("拟合数据关系")
plt.legend()
plt.show()


array = np.mat([2, 3, 4])
"""
比较啰嗦的将这些写在这边，主要用来测试注释的情况
"""
