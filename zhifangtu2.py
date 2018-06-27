# -*- coding: utf-8 -*-
"""
Created on Sun May  6 17:08:02 2018

@author: ZC
"""
from PIL import Image
import matplotlib.pyplot as plt
from numpy import *


def histeq(im,nbr_bins=256):
    """ 
    对一幅灰度图像进行直方图均衡化
    """
    # 计算图像的直方图
    imhist,bins = histogram(im.flatten(),nbr_bins,normed=True)
    cdf = imhist.cumsum() # cumulative distribution function
    cdf = 255 * cdf / cdf[-1] # 归一化
    # 使用累积分布函数的线性插值，计算新的像素值
    im2 = interp(im.flatten(),bins[:-1],cdf)
    return im2.reshape(im.shape), cdf


im = array(Image.open('1.jpg').convert('L'))
im2,cdf = histeq(im)
plt.figure("1")
plt.imshow(im2,cmap = cm.gray)
plt.axis("off")

plt.show()