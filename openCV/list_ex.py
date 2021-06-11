import get_data

kosta_student = {'minji':'박민지', 'chaeryeong':'이채령','iu':'이지은'}

class a():
    def func_a():
        print("func_a() in class a")
class b():
    def func_b(self):
        print("func_b() in class b")
        self.x = a()
        self.x.func_a()
        
def func1():
    func2()
    print("func1() activate and call func2() !!")

def func2():
    print("func2() activate !!")

if __name__ == '__main__':
    today = get_data.GetTime()
    #test_data = get_data.GetData()
    #print("today.today_object", today.today_object)
    
    today_hour = today.get_now().hour
    today_minute = today.get_now().minute
    today_time = str(today_hour)+":"+str(today_minute)
    
    print("time is ...",today_time)
    #print(today.get_now().second)
    
    a = a()
    b = b()
    
    print(b.func_b())
    count = 0
    num = 1
    
    if count == 0  and num == 0:
        print("if문에서는 or나 and 연산자를 사용합니다")
    
    '''
    while True:
        n = 0
        while n < 20:
            print("n = %d"%(n))
            if n == 10:
                break # while n<20 루프 탈출
            n += 1
        break # while True 루프 탈출

   
    
    print(str(today.today_object))
    #date 값을 뽑아올 때는 str() 처리를 해야한다.
    print(type(today.today_object))
    print(kosta_student['minji'])
    print(kosta_student)
    '''
    #name = ['minji']
    #print(name)
    #print(kosta_student[name[0]])
    
    #print(kosta_student['minji'])
    #print(kosta_student.keys())
    #print(kosta_student.values())