from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import time
from time import strftime
window=Tk()#creates window
window.geometry("500x500")#the measureemnts of the window
window.title("countdown")
window.config(background="pink")

hour=StringVar()# stringvar so the number will not be considered as an integer for the time format purposes
minute=StringVar()
second=StringVar()
hour.set("00")
minute.set("00")
second.set("00")

def startcountdown():
    global hour,minute,second
    time_in_secs=int(hourentry.get()) * 3600 + int(minsentry.get())*60+ int(secentry.get())#adds up the time together in seconds
    while time_in_secs >-1:#till the time is larger thsn -1 it will run
        mins,seconds=divmod(time_in_secs,60)#when the hour is less than 60 minutes it will come to minute.when minutes is less than 60 second it will move to seccs etc
        hours=00
        if mins>60:
            hour,minute=divmod(minute,60)
    
        hour.set(hours)#everytime variable is getting update and sets into the main variables
        minute.set(mins)
        second.set(seconds)
        window.update()
        time.sleep(1)
        time_in_secs=time_in_secs-1
        if time_in_secs==0:
          messagebox.showinfo("TIMES UP","Your timer is over")


          
    




heading=Label(window,text="countdown",font=("Arial",20),background="pink",foreground="black")
heading.place(x=150,y=140)
henter=Label(window,text="hour",font=("Arial",15),background="pink",foreground="black")
henter.place(x=75,y=175)
menter=Label(window,text="mins",font=("Arial",15),background="pink",foreground="black")
menter.place(x=170,y=175)
menter=Label(window,text="secs",font=("Arial",15),background="pink",foreground="black")
menter.place(x=265,y=175)
hourentry=Entry(window,foreground="black",width=5,textvariable=hour)
hourentry.place(x=75,y=215)
minsentry=Entry(window,foreground="black",width=5,textvariable=minute)
minsentry.place(x=170,y=215)
secentry=Entry(window,foreground="black",width=5,textvariable=second)
secentry.place(x=265,y=215)
start_button=Button(window,text="START",command=startcountdown)
start_button.place(x=225,y=265)


window.mainloop()




