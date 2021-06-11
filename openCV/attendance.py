#attendance.py

import face_recog
import sqlite3
import datetime
import cv2

##날짜와 시간을 나타내는 클래스
##시, 분을 뽑아내는 것이 중요.
class GetTime():
    def __init__(self):
        print("GetTime class execute...")
        self.today_object = datetime.date.today()
        print("Today is ...{0}\n".format(self.today_object) )
    
    def get_now(self):
        self.date_now = datetime.datetime.now()
        return self.date_now
    
    def print_time(self): #이 메소드 구현 전에 get_now() 메소드가 구현되어야 함.
        self.now_time = self.date_now.strftime("%H:%M:%S")
        print("Time is ...{0}".format(self.now_time))


# sqlite에서 minjiTABLE 세팅함
# id(사진이름), userName(이름), date(날짜), time(시간), message(입실체크 여부)
# GetData() 과정을 거쳐 checkDB.db에 minjiTABLE에 저장한다.  -> insert_data()       
class GetData():   
    #cur과 con 변수를 다른 곳에서도 사용하고 싶다면 어떻게 해야 하는가...!
    def __init__(self):
        print("GetData class execute...")
        self.con = sqlite3.connect("./checkDB.db")
        if self.con:
            print("checkDB.db connected !")
            
        self.cur = self.con.cursor()
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='minjiTABLE';")
        #self.cur.execute("SELECT * FROM minjiTABLE;")
        self.data = self.cur.fetchall()
        if len(self.data):
            print("minjiTABLE exists\n")
        else:
            self.cur.execute("CREATE TABLE minjiTABLE (id char(4), name char(7), date char(10), time char(10), message char(30));")
        
        self.con.commit()
         
    def insert_data(self, id, name, date, time, message):
        self.id = id
        self.name = name
        self.date = date
        self.time = time
        self.message = message
        
        self.cur.execute("INSERT INTO minjiTABLE VALUES('"+self.id+"', '"+self.name+"', '"+self.date+"', '"+self.time+"', '"+self.message+"'); ")
        self.con.commit()
        #self.con.close()
    
    def close_db(self):
        self.con.close()

def face_attendance(def_date, def_time, msg):
    frame_show(face_cam.get_frame())
    if face_cam.face_names :
        name = face_cam.face_names
        count.append(1)
        if kosta_student[name[0]] and len(count) == 5:
            today_data.insert_data(name[0], kosta_student[name[0]], def_date, def_time, msg)
            print(name[0], kosta_student[name[0]], def_date, def_time, msg, "입력 완료")

def frame_show(face_frame):
    face_frame = face_cam.get_frame()
    cv2.imshow("Frame", face_frame)
    
if __name__ == '__main__':
    print("attendance.py execute...\n")

    kosta_student = {'minji':'박민지', 'chaeryeong':'이채령','iu':'이지은', 'Chris':'크리스 햄스워스',
                     'Liam': '리암 햄스워스'}
    open_message = "출석확인 완료"
    state_message = "입실확인 완료"
    close_message = "퇴실확인 완료"
    
    count = []
    exit_loop = 0
    
    today = GetTime()
    today_data = GetData()
    face_cam = face_recog.FaceRecog()


    while True:
        get_date = str(today.today_object)

        get_hour = today.get_now().hour
        get_minute = today.get_now().minute
        get_time = str(get_hour)+":"+str(get_minute)
        
        while True:
        #while get_hour < 18:
            if get_hour == 8 and get_minute < 59 :
                face_attendance(get_date, get_time, open_message)
                break
            elif get_minute : # == 5 :
                if get_hour == 13:
                    pass
                else:
                    face_attendance(get_date, get_time, state_message)
                break
            elif get_hour == 17 and get_minute == 55:
                face_attendance(get_date, get_time, close_message) 
                break
            else:
                print("no condition match! (체크 안됐음 다시 확인바람!!!)")
                exit_loop = 1
                break     
        
        cv2.waitKey(1000)
        if len(count) == 5 or get_hour >= 18 or exit_loop:
            print("\nattendance.py Termination")
            today_data.con.close()
            #print("\ncount = {0}, get_hour = {1}, exit_loop = {2}".format(count, get_hour, exit_loop))
            break
        
    cv2.destroyAllWindows()
    print('\nfinish')