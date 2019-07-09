# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 11:41:00 2019

@author: Jaimin
"""
import cv2
from CV2VideoWriter import CV2VideoWriter

capture = cv2.VideoCapture(0)

writter = CV2VideoWriter(0,codec="DIVX",channel=0,FPS=10)

writter.start_session_frame("myoutputfilename")

while capture.isOpened():
    ret, frame = capture.read()
    
    if ret is not True:
        print("Not able to get frame exiting...")
        break
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    writter.save_session_frame(gray)
    
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) == ord('q'):
        break

writter.end_session()
cv2.destroyAllWindows()
capture.release()