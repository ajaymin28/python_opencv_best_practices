# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 10:59:01 2019

@author: Jaimin
"""
import cv2
import numpy as np

img = cv2.imread('@img/skull.jpg')
img = cv2.resize(img,(640,360))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("grayedImg",gray)
cv2.waitKey(0)
cv2.imwrite("@imgoutput/grayedimg.jpg",gray)
cv2.destroyAllWindows()
