import cv2

img = cv2.imread('laptop.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.imread('laptop.jpg', cv2.IMREAD_GRAYSCALE)
print("debug complte~")


import numpy as np
image = np.zeros((100, 100, 3), np.uint8)

cv2.imshow("keytest", image)
ret = cv2.waitKey(0)
print('pressed key is {0}'.format(ret))