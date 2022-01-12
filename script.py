import cv2
import numpy as np
  

def save_image(image,addr,num):
	address = addr + str(num)+ '.jpg'
	cv2.imwrite(address,image)
  
videoCapture = cv2.VideoCapture("xxx.mp4")

success, frame = videoCapture.read()
i = 0
timeF = 4
j=0

while success :
  i = i + 1
  if (i % timeF == 0):
    j = j + 1
    save_image(frame,'xxx/image',j)
    print('save image:',i)
  success, frame = videoCapture.read()
