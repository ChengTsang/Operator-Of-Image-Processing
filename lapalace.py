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

# lapalace operator， 3*3
operator = [[0,1,0],[1,-4,1],[0,1,0]]
lapalace_operator = np.array(operator).transpose()

# Open the image and transform it into a grayscale image.
image = Image.open("1.jpg").convert("L")
image_array = np.array(image)

# image and lapalace operator convolve
image4 = signal.convolve2d(image_array,lapalace_operator,mode = "same")

# transferm the result to 0-255
image4 = (image4/float(image4.max()))*255
         
# display the image

plt.figure("1")
plt.imshow(image4,cmap=cm.gray)
plt.axis("off")

plt.show()
