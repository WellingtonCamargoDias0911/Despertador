import tkinter as tk
from tkinter import Label, Frame, StringVar, OptionMenu, Button
from datetime import datetime
from time import sleep
from os import system

def alarm():
    while True:
        set_alarm_time = f'{hour.get()}:{minute.get()}:{second.get()}'
        sleep(1)
        current_time = datetime.now().strftime('%H:%M:%S')
        print(current_time, set_alarm_time)

        if current_time == set_alarm_time:
            system('start Alarm.wav')
            break



root = tk.Tk()
root.geometry('400x200')
root.title('Alarme Pythonico | Programador Aventureiro')

Label(root, text='Alarme Pythônico', font=('Helvetica 20 bold')).pack(pady=10)
Label(root, text='Definir alarme').pack(pady=5)

frame = Frame(root)
frame.pack()

def option(value):
    opt = StringVar(root)
    options = [str(i).zfill(2) for i in range(value)]
    opt.set(options[0])
    OptionMenu(frame, opt, *options).pack(side=tk.LEFT)
    return opt

hour = option(24)
minute = option(60)
second = option(60) 

Button(root, text='Definir', font=('Helvetica 15'), command=alarm).pack(pady=20)

root.mainloop()