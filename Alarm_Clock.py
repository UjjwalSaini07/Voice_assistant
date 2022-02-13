# from tkinter import *
# import datetime
# import time
# import winsound
#
#
# def Alarm(set_alarm_timer):
# 	while True:
# 		time.sleep(1)
# 		actual_time = datetime.datetime.now()
# 		cur_time = actual_time.strftime("%H:%M:%S")
# 		cur_date = actual_time.strftime("%d/%m/%Y")
# 		msg = "Current Time: " + str(cur_time)
# 		print(msg)
# 		if cur_time == set_alarm_timer:
# 			winsound.PlaySound("Music.wav", winsound.SND_ASYNC)
# 			break
#
#
# def get_alarm_time():
# 	alarm_set_time = f"{hour.get()}:{min.get()}:{sec.get()}"
# 	Alarm(alarm_set_time)
#
#
# window = Tk()
# window.title("Alarm Clock")
# window.geometry("400x160")
# window.config(bg="#922B21")
# window.resizable(width=False, height=False)
#
# time_format = Label(window, text="Remember to set time in 24 hour format!", fg="white", bg="#922B21",
# 					font=("Arial", 15)).place(x=20, y=120)
# addTime = Label(window, text="Hour     Min     Sec", font=60, fg="white", bg="black").place(x=210)
# setYourAlarm = Label(window, text="Set Time for Alarm: ", fg="white", bg="#922B21", relief="solid",
# 					 font=("Helevetica", 15, "bold")).place(x=10, y=40)
#
# hour = StringVar()
# min = StringVar()
# sec = StringVar()
#
# hourTime = Entry(window, textvariable=hour, bg="#48C9B0", width=4, font=(20)).place(x=210, y=40)
# minTime = Entry(window, textvariable=min, bg="#48C9B0", width=4, font=(20)).place(x=270, y=40)
# secTime = Entry(window, textvariable=sec, bg="#48C9B0", width=4, font=(20)).place(x=330, y=40)
#
# submit = Button(window, text="Set Your Alarm", fg="Black", bg="#D4AC0D", width=15, command=get_alarm_time,
# 				font=(20)).place(x=100, y=80)
#
# window.mainloop()
#
#
# exit()
# Import Required Library
from tkinter import *
import datetime
import time
import winsound
from threading import *
import os

# Create Object
root = Tk()

# Set geometry
root.geometry("400x200")

# Use Threading
def Threading():
    t1=Thread(target=alarm)
    t1.start()

def alarm():
	# Infinite Loop
	while True:
		# Set Alarm
		set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
		# Wait for one seconds
		time.sleep(1)
		# Get current time
		current_time = datetime.datetime.now().strftime("%H:%M:%S")
		print(current_time,set_alarm_time)

		# Check whether set alarm is equal to current time or not
		if current_time == set_alarm_time:
			print("Time to Wake up")
			# Playing sound
			# winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
os.startfile("E:\Python\Voice_assistant-main\SoftAlarmTone.mp3")


# Add Labels, Frame, Button, Optionmenus
Label(root,text="Alarm Clock",font=("Helvetica 20 bold"),fg="red").pack(pady=10)
Label(root,text="Set Time",font=("Helvetica 15 bold")).pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07','08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24')
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07','08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23','24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39','40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55','56', '57', '58', '59', '60')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07','08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23','24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39','40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55','56', '57', '58', '59', '60')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(root,text="Set Alarm",font=("Helvetica 15"),command=Threading).pack(pady=20)
# Execute Tkinter
#root.mainloop()
root.mainloop()
