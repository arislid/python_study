import cv2 as cv

cap = cv.VideoCapture(0)
while True:
    ret, img_frame = cap.read()
    
    if ret == False:
        print("캡쳐 실패")
        break
    cv.imshow('Colot', img_frame)
    key = cv.waitKey(1)
    if key == 27:
        break
cap.release()
cv.destroyAllWindows()