import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import pyautogui as pag
import threading
import time

root = ttk.Window(themename="minty")

root.title("Spaminator")
root.geometry("400x300")
root.resizable(False, False)
root.wm_attributes("-topmost", True)

# Sections
titleFrame = ttk.Frame(root)
titleFrame.pack()

program = ttk.Frame(root)
program.pack()

options = ttk.Frame(root)
options.pack()

def spam():
    speed = round(float(slider.get()))
    global keepGoing
    keepGoing = True
    input = entry.get() 
    
    def checkboxSelected():
        pag.typewrite(input)
        pag.press("enter")
        
    def checkboxNotSelected():
        pag.typewrite(input)
    
    if checkboxValue.get():
        while keepGoing:
            checkboxSelected()
            time.sleep(1/speed)
    
    else:
        while keepGoing:    
            checkboxNotSelected()
            time.sleep(1/speed)

def startButton():
    global loopThread
    loopThread = threading.Thread(target=spam)
    loopThread.start()
    start.configure(state="DISABLED")

def stopButton():
    global keepGoing
    keepGoing = False
    start.configure(state="NORMAL")

def labelUpdate(speed):
    speed = round(float(speed))
    counter.config(text=speed)

# Widgets
title = ttk.Label(titleFrame, text="Ingrese el texto debajo", font=("Arial", 16, "bold"), padding=(20))
title.pack()

entry = ttk.Entry(program, text="Ingrese el texto", width="40")
entry.pack(pady=(0, 25))

start = ttk.Button(program, text="Start (F1)", bootstyle="SUCCESS", padding=(20, 15), command=startButton)
start.pack(side="left", padx="20")

stop = ttk.Button(program, text="Stop (F2)", bootstyle="SECONDARY", padding=(20, 15), command=stopButton)
stop.pack(side="right", padx="20")

sliderTitle = ttk.Label(options, text="Mensajes por segundo")
sliderTitle.pack(pady="20, 0")

slider = ttk.Scale(options, from_=1, to=20, orient="horizontal", length="250", command=labelUpdate)
slider.pack(pady="0, 0")

counter = ttk.Label(options, text="0")
counter.pack(pady="0, 20")

checkboxValue = ttk.IntVar()
checkbox = ttk.Checkbutton(options, text="Pegar y enviar", variable=checkboxValue)
checkbox.pack()

root.mainloop()