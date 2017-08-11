import numpy as np  
import cv2  
import random
import copy

class bboxSelector():

    def __init__(self, windowName):
        # cv2.namedWindow('image')
        cv2.setMouseCallback(windowName, self._drawBbox)
        self.ix = -1
        self.iy = -1
        self.drawing = -1
        self.stack = []
        self.windowName = windowName
    def rebuild(self, image):

        cv2.setMouseCallback(self.windowName, self._drawBbox)
        self.ix = -1
        self.iy = -1
        self.drawing = -1
        # self.image = image[:][:][:]
        # self.cp_image = image[:][:][:]
        self.image = copy.deepcopy(image)
        self.cp_image = copy.deepcopy(image)
        # stack contains the (ix,iy,x,y) info for cut the sub img from the image at the end.
        self.stack = []
    def finish(self):
        nameStack = []
        for subImg in self.stack:
            tmp_str = "tmp_" + str(int(random.random()*10000))
            nameStack.append(tmp_str)
            cv2.imshow(tmp_str, self.image[subImg[1]:subImg[3],subImg[0]:subImg[2]])
    def _drawBbox(self, event, x, y, flags, param):  
        # self.cp_image = IMG
        if event == cv2.EVENT_LBUTTONDOWN:   
            self.drawing = True 
            self.ix, self.iy = x,y
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.drawing == True:
                pass
        elif event == cv2.EVENT_LBUTTONUP:
            color = (int(random.random()*255),int(random.random()*255),int(random.random()*255))
            cv2.rectangle(self.cp_image, (self.ix, self.iy), (x,y), color, 2)
            self.stack.append([self.ix,self.iy,x,y])

cv2.namedWindow('image')
bboxBoard = bboxSelector("image")
IMG = cv2.imread("timg.jpg")
bboxBoard.rebuild(IMG)

while(True):  
    cv2.imshow('image', bboxBoard.cp_image)  
    k = cv2.waitKey(1)&0xff  
    if k == ord('s'):  
        print 'you typed key s'  
        bboxBoard.finish()
    elif k == 27:  
        break  