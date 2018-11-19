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

# to generate gauss operator
def gauss_func(x,y,sigma=1):
    return 100*(1/(2*np.pi*sigma))*np.exp(-((x-2)**2+(y-2)**2)/(2.0*sigma**2))

# the method to generate mean operator
def mean_func(x,y):
    return 1/25

# to generate gauss operator with std = 2, size = 5*5
gauss_operator = np.fromfunction(Gauss_func,(5,5),sigma= 0.2)

# to get mean operator 
mean_operator = 1/25*np.ones((5,5))

image = Image.open("1.jpg").convert("L")
image_array = np.array(image)

# Gauss kernel convolution for image
image2 = signal.convolve2d(image_array,gauss_operator,mode="same")

# mean operator convolution for image
image3 = signal.convolve2d(image_array,mean_operator,mode = "same")

# transfer result to 0-255
image2 = (image2/float(image2.max()))*255
image3 = (image3/float(image3.max()))*255     
         
         

# Display image
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
