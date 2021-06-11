import cv2

vidcap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
success, image = vidcap.read()
count = 0

while True:
    height, width, layers = image.shape
    new_h = int(height / 2)
    new_w = int(width / 2)
    resize = cv2.resize(image, dsize = (new_w, new_h), interpolation=cv2.INTER_AREA)
    cv2.imshow("resize video", resize)
    success, image = vidcap.read()
    count += 1
    
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
    
    # do a bit of cleanup
cv2.destroyAllWindows()