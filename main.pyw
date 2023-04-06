import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="minty")

root.title("Spaminator")
root.geometry("400x220")


titleFrame = ttk.Frame(root)
titleFrame.pack()

program = ttk.Frame(root)
program.pack()

speedSelector = ttk.Frame(root)
speedSelector.pack()

title = ttk.Label(titleFrame, text="Ingrese el texto debajo", font=("Arial", 16, "bold"), padding=(20))
title.pack()

entry = ttk.Entry(program, text="Ingrese el texto", width="40")
entry.pack(pady=(0, 25))

start = ttk.Button(program, text="Start (F1)", bootstyle="SUCCESS", padding=(20, 15))
start.pack(side="left", padx="20")

stop = ttk.Button(program, text="Stop (F2)", bootstyle="SECONDARY", padding=(20, 15))
stop.pack(side="right", padx="20")

slider = ttk.Scale(speedSelector, from_=0, to=100, orient="horizontal")
slider.pack(pady="10")

root.resizable(False, False)
root.mainloop()