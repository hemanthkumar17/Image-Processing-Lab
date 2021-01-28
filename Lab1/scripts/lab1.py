import cv2          # import open-cv for image methods
import numpy as np  # import numpy for array methods
for i in range(1, 16):  # loop through the 16 images
    img = cv2.imread("../input/img"+str(i)+".jpg", 0)   # read the image based on i value
    print("Intensities of image " + str(i))             # print the array - intensity values
    print(img)
    print("Min: " + str(np.amin(img)))                  # print the min intensity
    print("Max: " + str(np.amax(img)))                  # print the max intensity
    print("Average: " + str(np.mean(img)))              # print the average intensity
    cv2.imshow("image" + str(i), img)                   # show the image in an external window
    cv2.waitKey(1000)                                   # wait for 1 second or for a key press
cv2.waitKey(0)                                          # wait infinitely until a key is pressed