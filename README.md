# OpenCV-Bbox-Player
## Usage
This project is a mini desktop application to play video/usb camera/rtsp. It can easily get screenshot and drawing bbox on the video and get the containing image in the bboxs. :neckbeard: :neckbeard:
### Relays ###
> Opencv 3.x <br>
> python 2.7 + / python 3.x <br>
> numpy <br>

### Video Player and Screenshot 
Set the trackerbar to 0 and press the key "p" to get a screenshot.
![part1](/img&video/part1.gif)
### Create Bbox and Capture inside image
When the video is paused, you can directly draw bboxs on the video. And if you press "s", it will return all the bbox images.
![part2](/img&video/part3.gif)
## APIs
**ReIDPlayer(source, windowName)**
ReIDPlayer is a class to create a video player.
+ <i>source</i> can be the video file's path or numbers(such as 0 represent the first camera on your devices) or a rtsp address.
+ <i>windowName</i> is the player's window's title.
```
player = ReIDPlayer("videos/init.mp4","opencvPlayer")
player.play()
```
**bboxSelector(windowName)**
bboxSelector is a class to draw bbox on images.
+ <i>window</i> is a opencv window you have created to contain an image.
> **bboxSelector.rebuild(image)** <br>
> + <i>image</i> is a numpy array contains rgb info of an image. 
> + used to re-initialize the painting board on the image; usually used in video frame operation. 

> **bboxSelector.finish()** <br>
> + used to end the painting board on the image. Must be used if the board will be used in future.
```
bboxBoard = bboxSelector(self.windowName)
bboxBoard.rebuild(frame)
bboxBoard.finish()
```
