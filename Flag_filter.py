# India flag filter 

import cv2
import numpy as np

canvas=np.zeros((450,600,3),dtype='uint8')

#creating a flag
cv2.rectangle(canvas,(0,0),(600,150),(0,150,255),-1)
cv2.rectangle(canvas,(0,150),(600,300),(255,255,255),-1)
cv2.rectangle(canvas,(0,300),(600,450),(40,255,0),-1)
cv2.circle(canvas,(300,225),75,(255,0,0),2)


cv2.line(canvas,(300,150),(300,300),(255,0,0),2)
cv2.line(canvas,(300-75,150+75),(300+75,150+75),(255,0,0),2)


cv2.line(canvas,(300-66,150+37),(300+66,150+75+37),(255,0,0),2)
cv2.line(canvas,(300+66,150+37),(300-66,150+75+37),(255,0,0),2)

cv2.line(canvas,(300-33,150+10),(300+33,300-10),(255,0,0),2)
cv2.line(canvas,(300+33,150+10),(300-33,300-10),(255,0,0),2)

cv2.line(canvas,(300-15,150+3),(300+15,300-3),(255,0,0),2)
cv2.line(canvas,(300-73,150+95),(300+73,150+55),(255,0,0),2)

cv2.line(canvas,(300+15,150+3),(300-15,300-3),(255,0,0),2)
cv2.line(canvas,(300+73,150+95),(300-73,150+55),(255,0,0),2)

cv2.line(canvas,(300-52,150+23),(300+52,300-23),(255,0,0),2)
cv2.line(canvas,(300+52,150+23),(300-52,300-23),(255,0,0),2)

img=canvas

#video capturing
vid=cv2.VideoCapture(0)

while True:
	ret,frame=vid.read()
	new_frame=cv2.resize(frame,(600,450))
	new_frame=cv2.flip(new_frame,1)

	res_frm=cv2.addWeighted(img,0.4,new_frame,1,0)  #flag image + frame 
	cv2.imshow('IND_Flag filter',res_frm)
	cv2.imwrite("Capture_img.jpg",res_frm)       # storing captured image 
	if cv2.waitKey(1) & 0xff == ord('q'):		  #on clicking q video will bw terminate
		break
vid.release()
cv2.destroyAllWindows()