import cv2          # import open-cv for image methods
import numpy as np  # import numpy for array methods
def halve(img):
    n = img.shape[0]
    half = int(n/2)
    new_image = np.zeros([half, half], dtype=int)
    for i in range(int(n/2)):
        for j in range(int(n/2)):
            for x, y in [(0, 0), (0, 1), (1, 0), (1, 1)]:
                new_image[i, j] = new_image[i, j] + int(img[2*i + x, 2*j + y])
    new_image = (new_image // 4).astype('uint8')
    return new_image
def resize(img):
    n = img.shape[0]
    new_size = n * 2
    new_image = np.zeros([new_size, new_size], dtype='uint8')
    for i in range(n):
        for j in range(n):
            for x, y in [(0, 0), (0, 1), (1, 0), (1, 1)]:
                new_image[2*i + x, 2*j + y] = img[i, j]
    return new_image
    
img = cv2.imread("../input/img4.jpg", 0)
print(img.shape)
img_data = np.copy(img[:512, :512])
cv2.imshow("image-1024", img)
cv2.waitKey(0)
img512 = halve(img)
img256 = halve(img512)
img128 = halve(img256)
img64 = halve(img128)
img32 = halve(img64)
img16 = halve(img32)
cv2.imshow("image-512", img512)
cv2.imshow("image-256", img256)
cv2.imshow("image-128", img128)

img512_resized = resize(img512)
img256_resized = resize(resize(img256))
img128_resized = resize(resize(resize(img128)))
img64_resized = resize(resize(resize(resize(img64))))
img32_resized = resize(resize(resize(resize(resize(img32)))))
img16_resized = resize(resize(resize(resize(resize(resize(img16))))))

cv2.imshow("image-512-resized", img512_resized)
cv2.imshow("image-256-resized", img256_resized)
cv2.imshow("image-128-resized", img128_resized)
cv2.imshow("image-64-resized", img64_resized)
cv2.imshow("image-32-resized", img32_resized)
cv2.imshow("image-16-resized", img16_resized)
cv2.waitKey(10)
cv2.waitKey(0)