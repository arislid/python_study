import cv2
import numpy as np
import matplotlib.pyplot as plt

image_file1 = 'JPG/wow light.jpg'
'''
dst = cv2.resize(image_file1, dsize=(640, 480), interpolation=cv2.INTER_AREA)
# TypeError: Expected Ptr<cv::UMat> for argument 'src'
'''
'''
dst = cv2.resize(cv2.UMat(image_file1), dsize =(640, 480), interpolation=cv2.INTER_AREA)
# TypeError: UMat() missing required argument 'ranges' (pos 2)
'''

img1 = cv2.imread(image_file1, cv2.IMREAD_COLOR)
height = img1.shape # tuple 방식
dst = cv2.resize(img1, dsize =(360, 600), interpolation=cv2.INTER_AREA)
img1_gray = cv2.imread(image_file1, cv2.IMREAD_GRAYSCALE)


cv2.imshow('stars show', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

# %%

 # %%
