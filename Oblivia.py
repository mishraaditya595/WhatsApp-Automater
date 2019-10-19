import time
from tkinter import messagebox
import tkinter as tk
import requests
import os
import pyautogui as p
 
def send_message():
    h = e3.get()
    m = e4.get()
    rec = e1.get()
    msg = e2.get()
    
    while True:
        l = time.localtime(time.time()) 
        if(l.tm_hour == int(h) and l.tm_min == int (m)-1):
            p.press("win")
            time.sleep(0.5)
            p.typewrite("Whatsapp")
            time.sleep(0.5)
            p.press("enter")
            time.sleep(10)
            p.keyDown('alt')
            p.press(' ')
            p.press('x')
            p.keyUp('alt')
            time.sleep(10)
            p.moveTo(x=400, y=200, duration=0.7)
            p.click()
            p.typewrite(rec, interval=0.04)
            time.sleep(2)
            p.press('enter')
            time.sleep(2)
            p.typewrite(msg, interval=0.04)
            time.sleep(2)
            p.press('enter')
            break

    
master = tk.Tk()
master.title("Oblivia")
master.geometry("350x150")
tk.Label(master, text="Receiver's name : ").grid(row=0)
tk.Label(master, text="Message : ").grid(row=1)
tk.Label(master, text="Hour : ").grid(row=2,column=0)
tk.Label(master, text="Minutes : ").grid(row=3,column=0)
 
e1 = tk.Entry(master)
e2 = tk.Entry(master,width=30)
e3 = tk.Spinbox(master, from_=00, to=23, width=5)
e4 = tk.Spinbox(master, from_=00, to=59, width=5)
 
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
 
tk.Button(master,text='SEND MESSAGE', command=send_message).grid(row=4,column=1)#,sticky=tk.W,pady=1)
master.mainloop()