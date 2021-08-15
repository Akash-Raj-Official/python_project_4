from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")
icon = PhotoImage(file="D:/Python Project/Clock.png")
root.iconphoto(root, icon)
root.resizable(False, False)


def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=("ds-digital", 80),
              background="green", foreground="black")
label.pack(anchor='center')
time()

mainloop()
