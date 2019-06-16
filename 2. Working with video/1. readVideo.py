# -*- coding: utf-8 -*-
import cv2

videofile = "@videos/basic.mp4"

capture = cv2.VideoCapture(videofile)


while capture.isOpened():
    frameAvialable, frame = capture.read()
    
    if frameAvialable is not True:
        print("Not able to get frame exiting...")
        break

    cv2.imshow("frame",frame)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
capture.release()