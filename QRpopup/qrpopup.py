import time
import tkinter
from tkinter import *
from PIL import ImageTk, Image
from apscheduler.schedulers.background import BackgroundScheduler

def QRpopup():
    window = Tk()
    window.wm_attributes("-topmost", 1)
    window.title("입실확인QR")
    window.geometry("450x400")
    window.resizable(width=True, height=True)
    path = "homeQR.jpeg"
    img = ImageTk.PhotoImage(Image.open(path))
    label = tkinter.Label(window, image = img)
    label.pack()

    button = Button(window, text = "창닫기", fg = 'black', command=window.destroy)
    button.pack()

    window.mainloop()

sched = BackgroundScheduler()
sched.start()

sched.add_job(QRpopup, 'cron', minute="01", second="0")

while True:
    time.sleep(1)
    message = str(input("qr입력시 qr코드창 팝업"))

    if message == 'qr':
        QRpopup()