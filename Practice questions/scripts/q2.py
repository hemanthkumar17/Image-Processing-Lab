import numpy as np
import cv2

img = np.zeros([64, 64], dtype="uint8")
for i in range(64):
    for j in range(64):
        img[i, j] = (np.abs(np.cos(np.sqrt(i**2 + j**2)))*255)
print(img)
cv2.imshow("image", img)
cv2.waitKey(0)
