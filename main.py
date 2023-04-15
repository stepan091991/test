import tkinter as tk
from tkinter import *
from random import randint
from random import choice
from PIL import ImageTk, Image
from tkinter import scrolledtext
# дальше импортируй все что нужно
errors_types = ["System message!","Program error!","Windows problem!","TaskHost error!","VDA error!","SystemHost problem","Explorer error","taskmngr error"]
errors_texts = ["The system has received a critical error and will be rebooted!","The program returned an invalid argument and will be closed!","The host process was unexpectedly terminated!","VDA received a critical error message and was suspended!","The process did not respond for the deferred period Code (23352)","Error code(NoProcessCommand),Please contact the administrator!","The task cannot be displayed. Please check the system settings!","Error code 2353"]
errors_icons = []
button_texts = ["Повторить","Ок","Close","Reply"]
game_codes = ["System message!\nThe error code","Program error!\nError in System32"]
root = tk.Tk()
error_img = ImageTk.PhotoImage(Image.open("error.png"))
warning_img = ImageTk.PhotoImage(Image.open("warning.png"))
errors_icons.append(error_img)
errors_icons.append(warning_img)
index = 0
coins = 10
find = None
def create_window():
    def close():
        window.geometry(f"184x135+{randint(0, 1820)}+{randint(0, 980)}")
    def move():
        window.geometry(f"184x135+{randint(0, 1820)}+{randint(0, 980)}")
        window.after(1500, move)
    def close_question(event):
        root.destroy()
    global index
    window = tk.Toplevel(root)
    window.resizable(width=False, height=False)
    window.config(bg="white")
    window.title(choice(errors_types))
    window.attributes("-toolwindow",1)
    window.protocol('WM_DELETE_WINDOW', close)
    window.geometry(f"184x135+{randint(0,1820)}+{randint(0,980)}")
    window.bind("<space>",close_)
    window.attributes("-topmost",True)
    btn1 = tk.Button(window,text=choice(button_texts),command=close)
    text = scrolledtext.ScrolledText(window, font=("",10),borderwidth=0)
    text.insert(INSERT,choice(errors_texts))
    text.configure(state=tk.DISABLED)
    icon = tk.Label(window,image=choice(errors_icons),bg="white")
    icon.place(x=1,y=10,height=47,width=47)
    btn1.place(x=85,y=100,height=28,width=90)
    text.place(x=50, y=15, height=80, width=150)
    index += 1
    window.after(2000,move)
    if index < 20:
        root.after(50, create_window)
def close_(event):
    root.destroy()
root.geometry(f"0x0+{1900}+{1900}")
root.after(100,create_window)
root.bind("<space>",close_)
root.mainloop()
