from tkinter import *
from PIL import Image



## 변수 선언 부분 ##
btnList = [""] * 9
fnameList = ["building.png", "flower.png", "jc-gellidon.png", "landscape.png",
             "laptop.png", "Milky Way.png", "romantic.png", "stars.png", "wow light.png"]
photoList=[None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

## 함수 선언 부분 ## 
def clickNext() :
    global num
    num += 1
    if num > 8 :
        num = 0
    photo = PhotoImage(file = "PNG/" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo
    
def clickPrev() :
    global num
    num -= 1
    if num < 0 :
        num = 8
    photo = PhotoImage(file = "PNG/" + fnameList[num]).zoom(1,1)
    pLabel.configure(image = photo)
    pLabel.image=photo
    
## 메인 코드 부분
window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text = "<< 이전", command = clickPrev)
btnNext = Button(window, text = "다음 >>", command = clickNext)

photo = PhotoImage(file = "PNG/" + fnameList[0]).zoom(1,1)
pLabel = Label(window, image = photo)  

btnPrev.place(x = 250, y = 10)
btnNext.place(x = 400, y = 10)
pLabel.place(x = 15, y = 50)

window.mainloop()

