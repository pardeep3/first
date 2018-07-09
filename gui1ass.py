#ques 1
import  tkinter as tk
from tkinter import *
top = tk.Tk()
def close():
          sys.exit()
          print("exit")
Label(top,text ="HELLO WORLD").grid(row =0)
Button =tk.Button(top,text ="Exit",width=25,command = close).grid(row =1)
print(top.mainloop())

#ques 2

import tkinter as tk
from tkinter import *
top =tk.Tk()
def close():
    Label(top, text="HELLO WORLD").grid(row=0)
Button =tk.Button(top,text ="Exit",width=25,command = close).grid(row =1)
print(top.mainloop())

#ques 3

import tkinter as tk
from tkinter import  *
top = tk.Tk()
frame = Frame(top)
frame.pack()
bottomframe = Frame(top)
bottomframe.pack(side = BOTTOM)

def exit():
    sys.exit()
redbutton =Button(frame,text="Exit",bg="red",command = exit)
redbutton.pack(side = LEFT)

def label_text():
    l1.config(text = "hfhdfd")
greenbutton = Button(frame,text ="brown",fg="brown",command = label_text)
greenbutton.pack(side = LEFT)
l1=Label(top ,text="HELLO WORLD")
l1.pack(side = BOTTOM)

print(top.mainloop())

#ques 4

from tkinter import *

master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)
#Label(master,text=).grid(row =3)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
def name():
    print("First Name = ",e1.get())
    print("Last Name =  ",e2.get())
but = Button(master,text="Submit",command=name).grid(row=3)
mainloop()
