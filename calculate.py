# -*- coding: utf-8 -*-
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

years = np.linspace(1950, 2010, 7)
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, gdp, color="green", marker="o", linestyle="solid")
plt.title("名义GDP")

plt.ylabel("十亿美元")
plt.show()


my_mat = np.zeros([5, 4])
print(my_mat)
