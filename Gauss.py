# -*- coding: utf-8 -*-
"""
Created on Sun May  6 09:06:46 2018

@author: ZC
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import scipy.signal as signal

# 生成高斯算子的函数
def Gauss_func(x,y,sigma=1):
    return 100*(1/(2*np.pi*sigma))*np.exp(-((x-2)**2+(y-2)**2)/(2.0*sigma**2))

# 生成均值算子的函数
def Mean_func(x,y):
    return 1/25
# 生成标准差为2的5*5高斯算子
Gauss_operator = np.fromfunction(Gauss_func,(5,5),sigma= 0.2)

# 生成均值平滑算子，5*5
Mean_operator = 1/25*np.ones((5,5))

# 打开图像并转化成灰度图像
image = Image.open("1.jpg").convert("L")
image_array = np.array(image)

# 图像与高斯算子进行卷积
image2 = signal.convolve2d(image_array,Gauss_operator,mode="same")

# 图像与均值算子进行卷积
image3 = signal.convolve2d(image_array,Mean_operator,mode = "same")

# 结果转化到0-255
image2 = (image2/float(image2.max()))*255
image3 = (image3/float(image3.max()))*255     
         
         

# 显示图像
#plt.subplot(2,1,1)
'''
plt.figure("1")
plt.imshow(image_array,cmap=cm.gray)
plt.axis("off")
'''
#image_array.save('C:\\Users\\ZC\\Desktop\\2.jpg')
#plt.subplot(2,1,2)
'''
plt.figure("2")
plt.imshow(image2,cmap=cm.gray)
plt.axis("off")
#image2.save('C:\\Users\\ZC\\Desktop\\3.jpg')
'''
plt.figure("3")
plt.imshow(image3,cmap=cm.gray)
plt.axis("off")

plt.show()