import numpy as np
import cv2

img = cv2.imread("../input/img4.jpg", 0)

cv2.imshow("image", img)

new_img = np.zeros([img.shape[0], img.shape[1]], dtype="uint8")
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        new_img[i, j] = ((np.floor(img[i, j]/255 * 4 ) / 4)* 255).astype("uint8")
        
cv2.imshow("quant_image", new_img)
cv2.waitKey(0)