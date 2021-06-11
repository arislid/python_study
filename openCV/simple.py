import face_recognition
import cv2
from face_recognition.api import face_locations
import numpy as np
from PIL import Image

vcap = cv2.VideoCapture(0 , cv2.CAP_DSHOW)

vcap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
vcap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

my_face = [ "my sample/my sample1.jpg"]
known_face_names = ["Park Minji"]

known_face_encodings = []

for face_img in my_face :
    load_image = face_recognition.load_image_file(face_img)
    #print("Image Load : ", face_img)
    #print(load_images)
    
    known_face_encodings.append(face_recognition.face_encodings(load_image))
    #print("load_image ==>")
    #print(load_image])
    #print("*****************************")
    #print(known_face_encodings)
    #print(" ")
    
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
show_name = []

while True:
    ret, frame = vcap.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
        
    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame, model="cnn") # (모델 설정 가능)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        #print("known_face_engodings => ")
        #print(known_face_encodings)
        #print("face_endocing =>")
        #print(face_encodings)
        
        for face_encoding in face_encodings :
            # 매칭 얼굴 비교 하기
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            
            print("matches : ", matches)  
            name = "Unknown" # 기본적으로 모르는 사람으로 표시

            # frame의 이미지 와 입력된 얼굴과의 매칭시 가장낮은 값이 가장 비슷한 비율값 
            face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
            print("face_distance : ", face_distance)  

            # 인식된 얼굴의 최소 틀림 값의 index 반환 
            best_match_index = np.argmin(face_distance)
            print("best_match_index : ", best_match_index)  

            # 최소 매칭값의 index가 존재하는지 체크 후 해당 가족의 이름을 가져온다.
            if matches[best_match_index] : 
            # IndexError: list index out of range
                name = known_face_names[best_match_index]

            # print("np.argmax(face_distance) : ", np.argmax(face_distance))  
            # 비율 값 소수점 2자리 까지 가지오기
            distance = str(np.round(face_distance[np.argmin(face_distance)] * 100, 2))
            name_distance = name + distance
            
            # 화면에 표시될 이름과 비율관련 추가 
            face_names.append(name_distance)
            
            print("name : %s, distance : %s, Matche : %s" %(name, distance, matches[best_match_index]))
    
    process_this_frame = not process_this_frame


    # 화면 표시
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # 화면상 얼굴의 사각 표시
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # 화면상 얼굴의 사각표시 밑에 표시할 문자 위치
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX

        # 사각 표시할 문자 설정 
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # 윈도우창 (Title , 프레임 이미지)
    cv2.imshow('Video', frame)

    # 'q' 문자 로 종료 처리 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vcap.release()           # 메모리 해제 
cv2.destroyAllWindows() # 모든창 제거, 특정 창만듣을 경우 ("VideoFrame")   