# camera.py

import cv2
import time

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you  have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        self.video.release()
        print("VideoCamera __del__ method done")

    def get_frame(self):
        
        # Grab a single frame of video
        ret, frame = self.video.read()
        
        #resize = cv2.resize(frame, dsize = (0,0), fx = 0.7, fy = 0.7, interpolation=cv2.INTER_AREA)
        return frame 


    # # fps 구하는 "메소드(함수 절대아님)"
    # # 웹캠에서 CAP_PROP_FPS를 통해 fps를 구할 수 없다. 따라서 time 모듈과 시간 체크해서
    # # fps를 반환하는 함수를 만들었다.
    # #
    # # 링크->: https://learnopencv.com/how-to-find-frame-rate-or-frames-per-second-fps-in-opencv-python-cpp/

    def get_fps(self):
        #fps = self.video.get(cv2.CAP_PROP_FPS)
        #print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps)) 
        # 무조건 0이 나옴...
        
        num_frames = 120
            
        #print("Capturing {0} frames".format(num_frames))
            
        start = time.time()
        for i in range(0, num_frames):
            ret = self.video.read()
            
        end = time.time()
        seconds = end - start
        #print("Time taken {0} seconds".format(seconds))
            
        self.fps = num_frames / seconds
        #print("Estimated frames per second: {0}".format(fps))
            
        return self.fps
    
if __name__ == '__main__':
    print("camera.py execute...")
    cam = VideoCamera()
    while True:
        frame = cam.get_frame()
        count = 0
        # show the frame
        cv2.imshow("Frame", frame)
                
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
    
    # do a bit of cleanup
    cv2.destroyAllWindows()
    print('finish')
    
