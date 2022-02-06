# Importing modules on which we work
from tkinter import *
import calendar

def date_calendar():
    # making our main window
    root = Tk()
    root.title("Calendar")
    root.geometry("240x200")
    root.resizable(0, 0)
    root.iconbitmap("Computer_icon.ico")

    # defining Function for displaying Calendar
    def show():
        a = int(spin1.get())
        b = int(spin2.get())

        cal = calendar.month(b, a)  # pass here your year and then month values
        # in our case i use b for year and a for month

        txt.delete(0.0, END)
        txt.insert(INSERT, cal)

    # Creating Label
    lbl1 = Label(root, text="Month", font=("arial", 9, "bold")).place(x=15, y=0)
    lbl2 = Label(root, text="Year", font=("arial", 9, "bold")).place(x=115, y=0)

    # Creating Spinbox
    spin1 = Spinbox(root, values=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), width=4)
    spin1.place(x=60, y=0)

    spin2 = Spinbox(root, from_=1999, to=2100, width=4)
    spin2.place(x=150, y=0)

    # Creating Button
    btn = Button(root, text="Show", font=("arial", 9, "bold"), command=show).place(x=100, y=30)

    # Creating textbox to display calendar

    txt = Text(root, width=23, height=8)
    txt.place(x=20, y=57)

    root.mainloop()

