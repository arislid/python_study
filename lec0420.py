'''
import random

lotto = []
def get_number():
    return random.randrange(1,46)

def get_lotto(lotto):
    while len(lotto) < 6:
        num = get_number()
        lotto.append(num)
        if lotto.count(num) > 1:
            lotto.pop()                              
    return lotto

print("** 로또 추첨을 시작합니다 **")
print()
print("추첨된 로또번호 ==>", get_lotto(lotto))
'''
from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("윈도 창 연습")
window.geometry("400x400")
window.resizable(width = TRUE, height = TRUE) # 사이즈 조절 못하게 false 처리
                                             # true시 사이즈 조절 가능
                                             
label1 = Label(window, text = "COOKBOOK~~ Python을")
label2 = Label(window, text = "열심히", font = ("궁서체", 30), fg = "blue")
label3 = Label(window, text = "공부 중입니다.", bg = "magenta", width = 20, height = 5, anchor = SE)

label1.pack()
label2.pack()
label3.pack()

button1 = Button(window, text = "파이썬 종료", fg = "red", command = quit)

button1.pack()

def clickleft(event):
    messagebox.showinfo("마우스", "마우스 왼쪽 클릭됨")

window.bind("<Button-1>", clickleft)

window.mainloop()