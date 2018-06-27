# -*- coding: utf-8 -*-
"""
Created on Sun May  6 17:23:42 2018

@author: ZC
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import scipy.signal as signal


# 拉普拉斯算子， 3*3
operator = [[0,1,0],[1,-4,1],[0,1,0]]
Lapalace_operator = np.array(operator).transpose()

# 打开图像并转化成灰度图像
image = Image.open("1.jpg").convert("L")
image_array = np.array(image)


# 图像与拉普拉斯算子进行卷积
image4 = signal.convolve2d(image_array,Lapalace_operator,mode = "same")

# 结果转化到0-255
image4 = (image4/float(image4.max()))*255
         
         

# 显示图像

plt.figure("1")
plt.imshow(image4,cmap=cm.gray)
plt.axis("off")

plt.show()