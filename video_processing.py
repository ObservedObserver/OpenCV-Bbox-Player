# import cv2

# class ReIDVideo():
# 	def __init__(self, source):
# 		self.video = cv2.VideoCapture(source)
# 	def rawPlayer(self):
# 		while(True):
# 			success,frame = self.video.read()
# 			cv2.imshow("tmp2017001",frame)
# 			if cv2.waitKey(1) & 0xFF == ord('q'):
# 				break

# 		cv2.destroyAllWindows()

# tmp = ReIDVideo("init.mp4")
# tmp.rawPlayer()

# import cv2.cv as cv

# capture = cv.CaptureFromFile('init.mp4')

# nbFrames = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_COUNT))

# #CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream
# #CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream

# fps = cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FPS)

# wait = int(1/fps * 1000/1)

# duration = (nbFrames * fps) / 1000

# print 'Num. Frames = ', nbFrames
# print 'Frame Rate = ', fps, 'fps'
# print 'Duration = ', duration, 'sec'

# for f in xrange( nbFrames ):
#     frameImg = cv.QueryFrame(capture)
#     print cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_POS_FRAMES)
#     cv.ShowImage("The Video", frameImg)
#     cv.WaitKey(wait)


import cv2

# def nothing():
# 	pass
videoCapture = cv2.VideoCapture('init.mp4')
# cv2.namedWindow("ReID")
# size = (int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
# print(size)
# length = videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)
# length = int(length)
# print(length)
# cv2.createTrackbar("Controller","ReID",0,length,nothing)

# fps = videoCapture.get(cv2.cv.CV_CAP_PROP_FPS)
# size = (int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))

success,frame = videoCapture.read()
print(frame)
# pos = 0
while success:
	# if pos != cv2.getTrackbarPos("Controller","ReID"):
	# 	pos = cv2.getTrackbarPos("Controller","ReID")
	# else:
	# 	pos += 1
	# print(pos)
	# print(videoCapture.get(cv2.cv.CV_CAP_PROP_POS_FRAMES))
	cv2.imshow('ReID', frame)
	# cv2.waitKey(int(1000/fps))
	# videoCapture.set(cv2.cv.CV_CAP_PROP_POS_FRAMES,pos)
	# cv2.setTrackbarPos("Controller","ReID",pos)
	success, frame = videoCapture.read()
cv2.destroyAllWindows()
print("finish")
