from flask import Flask, request

app = Flask(__name__) 
# __name__의 의미
# 1. 현재 사용하고 있는 프로그램을 main으로 표현된다
# 2. app.py 안에 있는 Flask 클래스를 통해 프로그램 이름(lec_flask0422.py)을 호출한다.

print("app이름 : ", app)
@app.route("/")
def helloworld():
    return "Hello World"

@app.route("/led") #http://localhost:5000/led?state=on(or off)
def led_on():
    state = request.values.get("state", "error")    #동적라우팅<쿼리스트링> /led?state=on
    if state == "on":
        print("GPIO.HIGH")
    elif state == "off":
            print("GPIO.LOW")
    elif state == "error":
        return "쿼리스트링 state가 전달되지 않았습니다."
    else:
        return "잘못된 쿼리스트링이 전달되었습니다."
    return "LED "+ state

@app.route("/gpio/cleanup")
def gpio_cleanup():    
    return "GPIO CLEANUP" 


if __name__ == "__main__":
    app.run(host="localhost")   
# 자신을 표현하는 localhost
# 모든 서버를 나타낼 때 -> 0.0.0.0
# 외부에서 요청할 때 다 반응한다
# localhost -> 내 컴퓨터만 요청시 반응한다.