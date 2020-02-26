# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 00:05:57 2020

@author: simiyu
"""

import cv2

img = cv2.imread('flower.jpg')

print("Image Properties")
print("- Number of Pixels: " + str(img.size))
print("- Shape/Dimensions: " + str(img.shape))