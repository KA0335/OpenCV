import cv2
import numpy as np
import time

print("""
starting.... """)

#use cv2.VideoCapture(1) if external camera is to be used.
cap = cv2.VideoCapture(0)
time.sleep(3)
background=0
for i in range(30):
	ret,background = cap.read()

background = np.flip(background,axis=1)

while(cap.isOpened()):
	_, img = cap.read()
	
	# Flipping the image (Can be uncommented if needed)
	img = np.flip(img,axis=1)
	
	# bgr to HSV color space.
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	value = (45, 45)
	
	blurred = cv2.GaussianBlur(hsv, value,0)
	
	# Defining lower and upper range.
	lower_red = np.array([0, 120, 70])
	upper_red = np.array([10, 255, 255])
	m1 = cv2.inRange(hsv,lower_red,upper_red)
	
	
	lower_red = np.array([170, 120, 70])
	upper_red = np.array([180, 255, 255])
	m2 = cv2.inRange(hsv,lower_red,upper_red)
	
	# generating the final mask
	mask = m1+m2
	mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))
	
	# Replacing pixels corresponding to cloak with the background pixels.
	img[np.where(mask==255)] = background[np.where(mask==255)]
	cv2.imshow('Display',img)
	k = cv2.waitKey(10)
	if k == 27:
		break
