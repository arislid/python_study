import cv2

image_file1 = 'laptop.jpg'
img1 = cv2.imread(image_file1)
height = img1.shape #튜플 형식(y, x, 채널수(rgb 형식이면 3, black-white면 생략))
print(height)

img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
height = img1_gray.shape
print(height)

if height[0] > 1200 or height[1] > 1000:    # 사이즈 비교해서 재조정하기
    dst = cv2.resize(img1, dsize =(0,0), fx = 0.3, fy = 0.1, interpolation=cv2.INTER_LINEAR)
    #fx, fy는 실수형식 -> 상대 배율로 사이즈 재조정
    print(dst.shape)

else:
    dst = cv2.resize(img1, dsize=(640, 480), interpolation=cv2.INTER_AREA)
    # dsize에 절대 길이를 넣어서 사이즈 재조정
    print(dst.shape)



# openCV에서는 rgb로 값을 나타내지 않고 bgr로 나타낸다
b, g, r = cv2.split(dst)

#plt.imshow()함수 사용할 때 b, r을 서로 바꿔서 Merge처리 해야한다.
dst_rgb = cv2.merge([r, g, b])

#plt.imshow(dst_rgb)
cv2.imshow('dst', dst)
cv2.waitKey(0)  #keybord 입력할 때까지 대기
cv2.destroyAllWindows() #keybord 입력하면 강종