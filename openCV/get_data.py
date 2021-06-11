#import time
#import face_recognition
#import camera
import face_recog
import sqlite3
import datetime
import cv2




##날짜와 시간을 나타내는 클래스
##시, 분을 뽑아내는 것이 중요.
class GetTime():
    def __init__(self):
        print("GetTime execute...")
        self.today_object = datetime.date.today()
        print("Today is ...", self.today_object)
    
    def get_now(self):
        self.date_now = datetime.datetime.now()
        return self.date_now
    
    def print_time(self): #이 메소드 구현 전에 get_now() 메소드가 구현되어야 함.
        self.now_time = self.date_now.strftime("%H:%M:%S")
        print("Time is ...", self.now_time)
 
 
# sqlite에서 minjiTABLE 세팅함
# id(사진이름), userName(이름), date(날짜), time(시간), message(입실체크 여부)
# GetData() 과정을 거쳐 checkDB.db에 minjiTABLE에 저장한다.  -> insert_data()       
class GetData():   
    #cur과 con 변수를 다른 곳에서도 사용하고 싶다면 어떻게 해야 하는가...!
    def __init__(self):
        print("GetData execute...")
        self.con = sqlite3.connect("./checkDB.db")
        #print(con) # <sqlite3.Connection object at 0x000001ADAF7E5A80>
        if self.con:
            print("checkDB.db connected !")
        self.cur = self.con.cursor()
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='minjiTABLE';")
        #self.cur.execute("SELECT * FROM minjiTABLE;")
        self.data = self.cur.fetchall()
        if len(self.data):
            print("minjiTABLE exists")
        else:
            self.cur.execute("CREATE TABLE minjiTABLE (id char(4), name char(7), date char(10), time char(10), message char(30));")
        
        self.con.commit()
        #self.con.close() # 요 녀석을 넣어야 할지, 말아야 할지 ...;;
        # 넣지 말아야 한다 -> GetData() 생성할 때 checkDB.db 를 연결하고, 그 다음을 동작하도록 대기해야한다.......
           
    def insert_data(self, id, name, date, time, message):
        self.id = id
        self.name = name
        self.date = date
        self.time = time
        self.message = message
        
        self.cur.execute("INSERT INTO minjiTABLE VALUES('"+self.id+"', '"+self.name+"', '"+self.date+"', '"+self.time+"', '"+self.message+"'); ")
        self.con.commit()
        self.con.close()
        

if __name__ == '__main__':
    print("get_data.py execute...")
    #my_face = face_recog.FaceRecog()
    kosta_student = {'minji':'박민지', 'chaeryeong':'이채령','iu':'이지은', 'Chris':'크리스 햄스워스',
                     'Liam': '리암 햄스워스'}
    open_message = "출석확인 완료"
    state_message = "입실확인 완료"
    close_messate = "퇴칠확인 완료"
    
    today = GetTime()
    today_data = GetData()
    face_cam = face_recog.FaceRecog()
    
    while True:
        get_date = str(today.today_object)
        #print("get_date", get_date, type(get_date)) # get_date 2021-04-28 <class 'str'>
        get_hour = today.get_now().hour
        get_minute = today.get_now().minute
        get_time = str(get_hour)+":"+str(get_minute)
        #print("get_time", get_time, type(get_time)) #get_time 16:44 <class 'str'>
        #print(get_hour,"시 ", get_minute,"분") # 16 시  44 분
        
        face_frame = face_cam.get_frame()
        cv2.imshow("Frame", face_frame)
        count = []
        if face_cam.face_names :
           name = face_cam.face_names
           #print(name)  # ['minji']
           #print(name[0]) # minji
           #print(kosta_student[name[0]]) #박민지
           if(kosta_student[name[0]]) :
                today_data.insert_data(name[0], kosta_student[name[0]], get_date, get_time, state_message)
                print(name[0], kosta_student[name[0]], get_date, get_time, state_message, "입력 완료")
                break 
        #if get_minute == 10    : ## 일단 10분 단위로 체크함.
            ## face_recog.FaceRecog() 수행해서
            ## 얼굴 인식 후 입실체크 수행하기
            #today_data.insert_data('minji', kosta_student['minji'], get_date, get_time, state_message)
        '''
        if get_hour == 8:
            face_frame = face_cam.get_frame()
            cv2.imshow("Frame", face_frame)
            if face_cam.face_names :
                name = face_cam.face_names

                if(kosta_student[name[0]]) :
                    today_data.insert_data(name[0], kosta_student[name[0]], get_date, get_time, open_message)
                    print(name[0], kosta_student[name[0]], get_date, get_time, open_message, "입력 완료")
            break
                    
        if get_minute == 36 :
            face_frame = face_cam.get_frame()
            cv2.imshow("Frame", face_frame)
            if face_cam.face_names :
                name = face_cam.face_names

                if(kosta_student[name[0]]) :
                    if count == 0:
                    # 한번만 데이터 입력하고
                    # 나오고 싶다면
                    # pass 하도록...
                        today_data.insert_data(name[0], kosta_student[name[0]], get_date, get_time, state_message)
                        print(name[0], kosta_student[name[0]], get_date, get_time, state_message, "입력 완료")
                        count = 1
            break
        
        if get_hour == 17 & get_minute == 55:
            face_frame = face_cam.get_frame()
            cv2.imshow("Frame", face_frame)
            if face_cam.face_names :
                name = face_cam.face_names

                if(kosta_student[name[0]]) :
                    if count == 0:
                        today_data.insert_data(name[0], kosta_student[name[0]], get_date, get_time, close_message)
                        print(name[0], kosta_student[name[0]], get_date, get_time, close_message, "입력 완료")               
                        count = 1
            break
        '''
        
        
        cv2.waitKey(1)
            
        #today.print_time()
        #time.sleep()
    
    cv2.destroyAllWindows()
    print('finish')
    
    
    
    
    ##### while문에 넣을 블록 #####
    '''
    get_date = str(today.today_object)
    
    get_hour = today.get_now().hour
    get_minute = today.get_now().minute
    get_time = str(get_hour)+":"+str(get_minute)
    
    today_data.insert_data('minji', kosta_student['minji'], get_date, get_time, state_message)
    print("DB에 입실확인 저장완료")
    '''
    ##############################