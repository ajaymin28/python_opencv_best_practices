# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 11:42:04 2019

@author: Jaimin
"""
try:
    import cv2
    import os
    print("cv2 version found: {}".format(cv2.__version__))
except ImportError:
    raise ImportError('Can not find opencv installation...')
    

class CV2VideoWriter:
    videoFile = None
    isWebCam = False
    saveFilename = ""
    size = None
    FPS = None
    fourcc = None
    codec = None
    FramesToSave = 100
    FilesSaved = []
    extention = None
    writter = None
    capture = None
    initError = None
    def __init__(self,videofile,codec=None,FPS=20,size=(640,360),FramesToSave=100):
        self.initError = False
        self.FPS = FPS
        self.size = size
        self.FramesToSave = FramesToSave
        self.codec = codec
        self.FilesSaved = []
        self.VideoCodecs = ['MJPG','DIVX','XVID', 'X264', 'WMV1', 'WMV2']
        self.FilesSaved.append(self.saveFilename)
        if self.codec is not None:
            try:
                self.fourcc = cv2.VideoWriter_fourcc(*self.codec)
                self.writter = cv2.VideoWriter(self.saveFilename,self.fourcc,self.FPS,self.size)
                self.extention = self.getFileExtention(self.codec)
            except TypeError:
                self.initError = True
                print('Something wrong with the parameters provided by user')
        if self.extention is not None:
            self.saveFilename = "../@videosoutput/output_codec_{}".format(self.codec)+str(self.extention)
        if type(videofile) is int:
            self.isWebCam = True
        self.videoFile = videofile
        self.capture = cv2.VideoCapture(self.videoFile)   
        
    def test_codecs(self):
        """
        codec : 'MJPG','DIVX','XVID', 'X264', 'WMV1', 'WMV2'  \n
        FPS:  frames to save per second \n
        size: save video size \n
        FramesToSave: method will switch to other codec or exit after saving this number of frames.
        """
        if self.initError is not True:
            if self.codec is None:
                print("Testing with all codecs \n")
                for codec in self.VideoCodecs:
                    self.codec = codec
                    self.fourcc = cv2.VideoWriter_fourcc(*self.codec)
                    self.extention = self.getFileExtention(self.codec)
                    self.saveFilename = "../@videosoutput/output_codec_{}".format(self.codec)+str(self.extention)
                    self.writter = cv2.VideoWriter(self.saveFilename,self.fourcc,self.FPS,self.size)
                    ret_file = self.saveFrames()
                    size = self.verify(ret_file)
                    if size==0:
                        print("Codec: {} | Available: {}".format(self.codec,False))
                    else:
                        print("Codec: {} | Available: {}".format(self.codec,True))
            else:
                print("Testing with: {} codec".format(self.codec))
                self.fourcc = cv2.VideoWriter_fourcc(*self.codec)
                ret_file = self.saveFrames()
                size = self.verify(ret_file)
                if size==0:
                    print("Codec: {} | Available: {}".format(self.codec,False))
                else:
                    print("Codec: {} | Available: {}".format(self.codec,True))
    def saveFrames(self):
        framecount = 0
        while self.capture.isOpened():
            cap,frame = self.capture.read()
            if cap is not True:
                print('could not get frame')
                break
            frame = cv2.resize(frame,self.size)
            cv2.imshow("img",frame)
            try:
                self.writter.write(frame)
                framecount +=1
                if framecount>=self.FramesToSave:
                    break
            except:
                print("writing frame failed")
                break
        self.capture.release()
        self.writter.release()        
        cv2.destroyAllWindows()
        return self.saveFilename
    def verify(self,path):
        size = 0
        try:
            s = os.stat(path)
            size = s.st_size
        except:
            return 0
        return size
    def getFileExtention(self,codecname):
        codecname = str(codecname)
        if codecname=="DIVX" or codecname=="WMV1" or codecname=="WMV2" or codecname=="XVID" or codecname=="MJPG":
            return ".avi"
        elif codecname=="X264":
            return ".mp4"
        else:
            return None