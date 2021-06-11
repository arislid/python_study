import cv2
import numpy as np
#import matplotlib.pyplot as plt
#트랙바 조정 함수
def on_trackbar(x):
    pass

#트랙바 붙일 윈도우 생성
cv2.namedWindow('Canny')
#트랙바 생성
cv2.createTrackbar('low threshold', 'Canny', 0, 250, on_trackbar)
cv2.createTrackbar('high threshold', 'Canny', 0, 1000, on_trackbar)
#트랙바 초기값 설정
#트랙바 이름, 붙어있는 경우 윈도우 이름으로 접근
cv2.setTrackbarPos('low threshold', 'Canny', 50)
cv2.setTrackbarPos('high threshold', 'Canny', 150)

#gray scale 이미지 불러오기
img = cv2.imread('laptop.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.imread('laptop.jpg', cv2.IMREAD_GRAYSCALE)
img_gray1 = cv2.resize(img_gray, dsize=(800, 640), interpolation=cv2.INTER_AREA)

#트랙바가 조정시 canny함수에 반영되도록 조정
while(1):
    low = cv2.getTrackbarPos('low threshold', 'Canny')
    high = cv2.getTrackbarPos('high threshold', 'Canny')
    
    #트랙바로부터 가져운 값으로 파라미터 조정
    img_canny = cv2.Canny(img_gray1, low, high)
    
    cv2.imshow('Canny', img_canny)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
'''
image_file1 = 'JPG/wow light.jpg'

dst = cv2.resize(image_file1, dsize=(640, 480), interpolation=cv2.INTER_AREA)
# TypeError: Expected Ptr<cv::UMat> for argument 'src'
'''
'''
dst = cv2.resize(cv2.UMat(image_file1), dsize =(640, 480), interpolation=cv2.INTER_AREA)
# TypeError: UMat() missing required argument 'ranges' (pos 2)


img1 = cv2.imread(image_file1, cv2.IMREAD_COLOR)
height = img1.shape # tuple 방식
dst = cv2.resize(img1, dsize =(360, 600), interpolation=cv2.INTER_AREA)
dst_gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)


cv2.imshow('stars show', dst_gray)
cv2.imshow('color star', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
# %%

 # %%
