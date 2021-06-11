import face_recog
import camera
import face_recognition
import numpy as np
from PIL import Image
import cv2 as cv

class Blur():
    def __init__(self):
        print("Blur execute...")

if __name__ == '__main__':
    print("unknown_blur.py execute ...")
    img = face_recognition.load_image_file("my sample2.jpg") # <class 'numpy.ndarray'>
    #print("img datatype ...", type(img))
    face_img = face_recognition.face_locations(img) # <class 'list'>
    #print("face_img datatype...", type(face_img))
    
    for face_location in face_img:
        top, right, bottom, left = face_location
        ksize = 100
        faceblur = img[top:bottom, left:right]
        faceblur = cv.blur(faceblur, (ksize, ksize))
        
        #pil_roi = Image.fromarray(roi)
        #pil_roi.show()
        img[top:bottom, left:right] = faceblur
        
        pil_image = Image.fromarray(img)
        pil_image.show()
        
    cv.waitKey(0)
    cv.destroyAllWindows()
    #img_cvt = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    #kernel = np.ones((5,5), np.float32)/100
    #dst = cv.filter2D(img_cvt,-1,kernel)
    #pil_img = Image.fromarray(dst)
    #pil_img.show()
    