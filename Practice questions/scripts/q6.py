import numpy as np
import cv2

img1 = ((cv2.imread("../input/img5.png", 0)).astype(float))/255
img2 = ((cv2.imread("../input/img6.jpg", 0)).astype(float))/255

cv2.imshow("add", ((img1+img2)*255).astype('uint8'))
cv2.imshow("sub", ((img1-img2)*255).astype('uint8'))
cv2.imshow("mul", ((img1*img2)*255).astype('uint8'))
cv2.imshow("div", ((img1/img2)*255).astype('uint8'))
cv2.waitKey(0)