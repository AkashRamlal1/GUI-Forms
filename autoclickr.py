
from calendar import c
from cgitb import text
from distutils import bcppcompiler
import tkinter as tk
import time
from tkinter.ttk import Checkbutton
from tkinter import *
from pygame import event

checked_up =  False
checked_down = False

counter = 0
window = tk.Tk()

window.geometry("500x500")



button_up = tk.Button(text= 'up')

counter_label = tk.Label(
    window,
    text= counter
)

button_down = tk.Button(text= 'down')

button_reset = tk.Button(text='reset')

reset_label = tk.Label(text= '')




    
   
def color(counter):
    
    if counter < 0:
        color_choice = "red"
        

    elif counter > 0:
     color_choice = "green"

    else:
        color_choice = "grey"
    return color_choice


def upB():
    global counter, counter_label,window,up

    print('hallo')
    counter = counter + 1
    counter_label.config(text= counter, bg=color(counter))
    up = True

def up_button(event):
    upB()
    
    
def downB():
    global counter, counter_label,window, color, up
    counter = counter - 1
    counter_label.config(text= counter, bg=color(counter))
    up = False
    

def down_button(event):
    downB()
    
def resetB():
    global counter, counter_label, reset_label

    if counter > 0 or counter < 0 :
        counter = 0
        counter_label.config(text= counter)

def reset(event ):
    resetB()
    
    
def pluscheck():
    global counter,counter_label,cbplus

    if cbplus.get() == 5:
        counter = counter + 1
        print(counter)
        counter_label.config(text=counter)
        counter_label.after( 1,pluscheck)

def minusCheck():
    global counter,counter_label,cbminus

    if cbminus.get() == 5:
        counter = counter - 1
        print(counter)
        counter_label.config(text=counter)
        counter_label.after( 1,minusCheck)



window.config(

 bg = color(counter)   
)

def TempColor(event):
    counter_label.config(bg='yellow')
def TempcolorEnd(event):
    counter_label.config(bg=color(counter))
def DoubleClick(event):
    global  counter, counter_label

    if up == True:
        counter = counter * 3
        counter_label.config(text= counter)
    elif up == False:
        counter = counter / 3
        counter_label.config(text= counter)
  

cbplus = IntVar(value=1)
cbminus = IntVar(value=1)
button_up.config(command= upB)
button_down.config(command= downB)
button_reset.config(command= resetB)
checkUP = tk.Checkbutton(text="+", onvalue=5, offvalue=6,variable=cbplus ,command=pluscheck)
checkDown = tk.Checkbutton(text="-",onvalue=5, offvalue=6,variable=cbminus, command= minusCheck)





button_up.pack(
    ipady=25,
    ipadx=100,
    
    
)

counter_label.pack(ipady=25,
    ipadx=100)

button_down.pack(ipady=25,
    ipadx=100,)

button_reset.pack(ipady=25,
    ipadx=100,)

checkUP.pack()
checkDown.pack()

counter_label.bind("<Enter>",TempColor)
counter_label.bind("<Leave>",TempcolorEnd)
counter_label.bind("<Double-Button-1>", DoubleClick)
window.bind('<Up>', up_button)
window.bind('<Down>', down_button)
window.bind('<space>', DoubleClick)
window.bind('<Return>', reset)


window.mainloop()