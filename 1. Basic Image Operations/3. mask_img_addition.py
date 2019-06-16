# -*- coding: utf-8 -*-
"""
Created on Sun May 26 10:41:32 2019

@author: Jaimin
"""
import cv2
import numpy as np

img = cv2.imread('@img/skull.jpg')
img = cv2.resize(img,(640,360))
cv2.imshow("original front",img)

lower_black = np.array([0,0,0])
upper_black = np.array([50,50,50])

lower_white = np.array([250,250,250])
upper_white = np.array([255,255,255])


mask = cv2.inRange(img,lower_black,upper_black)
mask_white = cv2.inRange(img,lower_white,upper_white)

added_mask = mask + mask_white


background = cv2.imread('@img/hallo.jpg')
background = cv2.resize(background,(640,360))
cv2.imshow("original back",background)

background[mask==0] = [0,0,0]
img[mask!=0] = [0,0,0]

final_img = background + img
cv2.imshow("finalresult",final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
