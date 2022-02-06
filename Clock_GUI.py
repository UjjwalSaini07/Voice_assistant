from tkinter import *
from tkinter.ttk import *
from time import strftime

def tkinter_clock():
    root = Tk()
    root.title("Clock")
    root.geometry("300x62")
    root.minsize(296, 60)
    root.maxsize(302, 63)
    root.iconbitmap("Computer_icon.ico")

    def time():
        string = strftime("%H:%M:%S %p")
        label.config(text=string)
        label.after(1000, time)

    label = Label(root, font=("lucida", 40), background="black", foreground="cyan")
    label.pack(anchor="center")
    time()
    mainloop()

# tkinter_clock()
