#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 13:17:34 2019
CobaltChicken, 10/18, challenge 3
Sources:
https://stackoverflow.com/questions/26392336/importing-images-from-a-directory-python
https://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
@author: dawsoncook
"""

import glob
from PIL import Image 
import numpy as np
import matplotlib.pyplot as mplot

userinp = input ("Enter a number between 0-255: ")
userinp=int(userinp)
if userinp > 254 or userinp < 1:
    print("Invalid number")
else:
    
    #opens all images and appends all imgs to Image List
    image_list = []
    for filename in glob.glob('p*.jpg'):
        im=Image.open(filename)
        im=np.float64(im)
        image_list.append(im)
        #print(image_list)


    #loop through image list and find sum of all
    meanarr = np.array(image_list)
    meanarr = np.mean(meanarr, axis=0)      

   

    #find the SD
    arr = np.array(image_list)
    arr =np.std(arr, axis=0)

  
    
    mplot.imshow(np.uint8(arr))
    mplot.show()

    mplot.imshow(np.uint8(meanarr))
    mplot.show()



    #loop through height and width
    for height in range(len(meanarr)):
        for width in range(len(meanarr[height])):
            if arr[height][width][0] > userinp and arr[height][width][1] > userinp and arr[height][width][2] > userinp :
                meanarr[height][width] = (255, 0, 0)
        
    mplot.imshow(np.uint8(meanarr))
    mplot.show()




