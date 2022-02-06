import speedtest
import pyspeedtest
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk

def internet_speedtest():
    result_download = []
    result_upload = []

    def down():
        st = speedtest.Speedtest()
        sp_down = str(st.download())
        msg = messagebox.showinfo("Download Speed", sp_down[:2] + "mbps")
        result_download.append(sp_down[:2])

    def up():
        st = speedtest.Speedtest()
        sp_up = str(st.upload())
        msg = messagebox.showinfo("Upload Speed", sp_up[:2] + "mbps")
        result_upload.append(sp_up[:2])

    def speed_test():
        # For Download Speed
        st = speedtest.Speedtest()
        sp_down = str(st.download())
        result_download.append(sp_down[:2])

        # For Upload Speed
        st = speedtest.Speedtest()
        sp_up = str(st.upload())
        result_upload.append(sp_up[:2])

        messagebox.askokcancel("SpeedTest", f"Download Speed {sp_down[:2]} mbps\nUpload Speed {sp_up[:2]} mbps")

    def ping():
        def Speed_test():
            t = pyspeedtest.SpeedTest(e1.get())
            myping.set(t.ping())

        master = Tk()
        master.iconbitmap("Computer_icon.ico")
        master.title("Ping Calculate")
        myping = StringVar()
        Label(master, text="Website URL").grid(row=0, sticky=W)
        Label(master, text="Ping Result:").grid(row=2, sticky=W)
        result = Label(master, text="", textvariable=myping).grid(row=3, column=1, sticky=W)
        e1 = Entry(master)
        e1.grid(row=0, column=1)
        b = Button(master, text="Check", command=Speed_test)
        b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

        mainloop()

    root = Tk()
    root.iconbitmap("Computer_icon.ico")
    root.title("SpeedTest")
    # root.geometry("224x300") # todo : This is the default size of window
    root.minsize(220, 230)
    root.maxsize(230, 245)
    framehome = Frame(root, bg="orange")
    framehome.pack(fill=BOTH, expand=True)
    imagehome = PhotoImage(file="Speedtest1.png")
    label1 = ttk.Label(framehome, image=imagehome)
    label1.grid(columnspan=2)

    create_button_1 = Button(framehome, text="Download Speed", command=down, fg="white", bg="black", padx=10, pady=8)
    create_button_1.grid(row=1, column=0)
    create_button_2 = Button(framehome, text="Upload Speed", command=up, fg="white", bg="black", padx=18, pady=8)
    create_button_2.grid(row=2, column=0)
    create_button_3 = Button(framehome, text="Speed Test", command=speed_test, fg="white", bg="black", padx=23, pady=8)
    create_button_3.grid(row=1, column=1)
    create_button_4 = Button(framehome, text="Ping Speed", command=ping, fg="white", bg="black", padx=22, pady=8)
    create_button_4.grid(row=2, column=1)

    root.mainloop()

    """
    down(st)
    up(st)
    """

internet_speedtest()

