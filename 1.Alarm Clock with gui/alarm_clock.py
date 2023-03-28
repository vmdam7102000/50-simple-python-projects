from datetime import datetime, date
import winsound
import time
from tkinter import *


def alarm(time_get_up):
    while True:
        time.sleep(1)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        today = date.today()
        print(today, "\t")
        print(current_time, "\n")
        if current_time == time_get_up:
            print("WAKEEE UPPPP \n")
            winsound.Beep(1000, 440)
            break

def actual_time():
    time_get_up = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(time_get_up)

clock = Tk()
clock.title("DataFlair Alarm Clock")
clock.geometry("400x200")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=120)
addTime = Label(clock,text = "Hour  Min     Sec",font=60).place(x = 110)
setYourAlarm = Label(clock,text = "Set your alarm clock",fg="blue",font=("Helevetica",12)).place(x=3, y=29)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=30)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =110,y=70)

clock.mainloop()
#Execution of the window.