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
    videosource = None
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
    channel = None
    def __init__(self,videosource,codec="MJPG",FPS=30,size=(640,360),FramesToSave=100,channel=1):
        self.initError = False
        self.FPS = FPS
        self.size = size
        self.FramesToSave = FramesToSave
        self.codec = codec
        self.channel = channel
        self.FilesSaved = []
        self.VideoCodecs = ['MJPG','DIVX','XVID', 'X264', 'WMV1', 'WMV2']
        self.FilesSaved.append(self.saveFilename)
        self.fourcc = cv2.VideoWriter_fourcc(*self.codec)
        self.writter = cv2.VideoWriter(self.saveFilename,self.fourcc,self.FPS,self.size,self.channel)
        self.extention = self.getFileExtention(self.codec)
        self.saveFilename = "../@videosoutput/output_codec_{}".format(self.codec)+str(self.extention)
        if type(videosource) is int:
            self.isWebCam = True
        self.videosource = videosource
        self.capture = cv2.VideoCapture(self.videosource)   
        
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
                    self.writter = cv2.VideoWriter(self.saveFilename,self.fourcc,self.FPS,self.size,self.channel)
                    ret_file = self.saveFrames()
                    size = self.verify(ret_file)
                    if size==0:
                        print("Codec: {} | Available: {}".format(self.codec,False))
                    else:
                        print("Codec: {} | Available: {}".format(self.codec,True))
            else:
                print("Testing with: {} codec".format(self.codec))
                self.fourcc = cv2.VideoWriter_fourcc(*self.codec,self.channel)
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
            #cv2.imshow("img",frame)
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
    def setfilename(self,filename):
        self.saveFilename = "filename_output_codec_{}".format(self.codec)+str(self.extention)
    def start_session_frame(self,outputfilename):
        self.setfilename(outputfilename)
        self.fourcc = cv2.VideoWriter_fourcc(*self.codec)
        self.writter = cv2.VideoWriter(self.saveFilename,self.fourcc,self.FPS,self.size,self.channel)
    def save_session_frame(self,frame):
        frame = cv2.resize(frame,(640,360))
        self.writter.write(frame)
    def end_session(self):
        self.capture.release()
        self.writter.release()
        return self.saveFilename
    def getFileExtention(self,codecname):
        codecname = str(codecname)
        if codecname=="DIVX" or codecname=="WMV1" or codecname=="WMV2" or codecname=="XVID" or codecname=="MJPG":
            return ".avi"
        elif codecname=="X264":
            return ".mp4"
        else:
            return None