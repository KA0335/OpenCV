import cv2
import numpy as np
    
def nothing(x):
  pass

cv2.namedWindow('Image')
img = cv2.imread("Lenna.png")
h,w,d = img.shape
c_img = np.zeros((h,w), np.uint8)
r_img = cv2.rectangle(c_img, (200,200), (400,400), 1, thickness=-1)

mask = cv2.bitwise_and(img, img, mask=r_img)
low = 1
high = 40
cv2.imshow("blurred_image", mask)
cv2.createTrackbar('Blur', 'Image',low,high,nothing)
while (True):
    ksize = cv2.getTrackbarPos('Blur', 'Image')
    ksize =2*ksize+1
    image = cv2.blur(img,(ksize,ksize),10)
    out = img.copy()
    out[mask>0] = image[mask>0]
    cv2.imshow('Image', out)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()