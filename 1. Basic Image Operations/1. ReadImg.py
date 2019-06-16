# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 10:58:25 2019

@author: Jaimin
"""
import cv2
import numpy as np

img = cv2.imread('@img/skull.jpg')
img = cv2.resize(img,(640,360))
cv2.imshow("original front",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
