import os
from tkinter import *

### global 변수 ###
window = None
canvas = None
X, Y = 256, 256
inImage = []
inFp = None 
fName, inList, inStr = "", [ ], ""   

### 함수 ###
def read_file():
    global fName, inFp, inStr, inList
    if os.path.exists(fName):
        inFp = open(fName, "r", encoding='utf-8')
        inList = inFp.readlines()
        for inStr in inList :
            print(inStr, end = "")
        
        inFp.close()
    else :
        print("%s 파일이 없습니다" %fName)

def tkinter_window():
    global X, Y, window, canvas 
    window = Tk()
    canvas = Canvas(window, height = X, width = Y)
    paper = PhotoImage(width = X, height = Y)
    canvas.create_image((X/2, Y/2), image=paper, state='normal')
    canvas.pack()
    window.mainloop()

#def write_file():
    


 
## main 함수(?) ###

tkinter_window()
fName = input("파일명을 입력하세요 : ")
read_file()

    
