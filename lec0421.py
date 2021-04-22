class  Car :
    color = ""  #클래스 내부에 있는 변수를 필드라고 한다
    speed = 0   #필드: 인스턴스 변수

    def __init__(self, value1, value2):
        self.color = value1
        self.speed = value2
        
    def  upSpeed(self, value) : #self: 클래스 내 필드(color, speed)를 접근하는 인스턴스
        self.speed += value     #C++나 C#에서는 this 인스턴스를 사용한다.
        if self.speed > 150:
            self.speed = 150
    
    def  downSpeed(self, value) :
        self.speed -= value     

class Sedan(Car):   #상속받은 자식 클래스(부모클래스) <- 클래스 선언방법
    def upSpeed(self, value):   # 부모 클래스 상속받은 메소드를 재정의해서 코드를 재작성한다.
        self.speed += value
        if self.speed == 0:
            self.speed = 20
            
class myClass:
    name = ''
    age = 0
    count = 0
    
    def __init__(self):
        myClass.count = 1       #클래스.필드 = 클래스 변수
        self.age += 20          #self.필드 = 인스턴스 변수
        self.name = '홍길동'
    def print_myClass(self):
        print("1학년 1반 %s, %d세" % (self.name, self.age))

name1 = myClass()
name1.name = '안희연'
name1.age = 30

name2 = myClass()
name2.name = '이지은'
name2.age = 29

name3 = myClass()
name3.name = '이채령'
name3.age = 21

#클래스를 배열처럼 넣을 수 없을까?

'''
myCar1 = Car('', 0)
myCar1.color = "빨강"
myCar1.speed = 0

myCar2 = Car('', 0)
myCar2.color = "파랑"
myCar2.speed = 0

myCar3 = Car('', 0)
myCar3.color = "노랑"
myCar3.speed = 0

myCar4 = Car("블랙", 70)

myCar1.upSpeed(30)
print("자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다." % (myCar1.color, myCar1.speed))

myCar2.upSpeed(60)
print("자동차2의 색상은 %s이며, 현재 속도는 %dkm입니다." % (myCar2.color, myCar2.speed))

myCar3.upSpeed(200)
print("자동차3의 색상은 %s이며, 현재 속도는 %dkm입니다." % (myCar3.color, myCar3.speed))

print("자동차4의 색상은 %s이며, 현재 속도는 %dkm입니다." % (myCar4.color, myCar4.speed))
'''
# %%
1606+158+149+110+107+99+77+60+47+40+32+31+31+31+28+18+18
# %%
