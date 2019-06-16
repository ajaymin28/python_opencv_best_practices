# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 11:41:00 2019

@author: Jaimin
"""

videofile = "../@videos/basic.mp4"

from CV2VideoWriter import CV2VideoWriter

writter = CV2VideoWriter(videofile,codec="MJPG")
writter.test_codecs()

"""
capture = cv2.VideoCapture(videofile)


while capture.isOpened():
    ret, frame = capture.read()
    
    if ret is not True:
        print("Not able to get frame exiting...")
        break

    cv2.imshow("frame",frame)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
capture.release()
"""