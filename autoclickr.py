import tkinter as tk
from tkinter.ttk import Checkbutton
from tkinter import *
window = tk.Tk()
window.geometry("500x500")
window.teller = 0
window.inspect = True
#telt op en af
def optellen():
    window.teller += 1
    update_window()

def Optellen(event):
    optellen()
    update_window()

def aftellen():
    window.teller -= 1
    update_window()

def Aftellen(event):
    aftellen()

def verdubbel_delen(event):
    print(window.inspect)
    if window.inspect == True:
        window.teller *= 2
        
    elif window.inspect == False:
        window.teller /= 3
    update_window()

def herstart_teller(event):
    window.teller = 0
    update_window()
def Herstart_timer(event):
    herstart_teller()

def highlight_Tbox(event):
    teller_box.config(bg='yellow')

opteler = tk.Button(text= "+", command=optellen)
teller_box = tk.Label(text= window.teller)
afteler = tk.Button(text="-",command= aftellen)
herstart = tk.Button(text="herstart", command=herstart_teller) 

Checkplus = IntVar(value=1)
Checkmin = IntVar(value=1)

def pluscheck():
    if Checkplus.get() == 5:
        window.teller += 1
        update_window()
        teller_box.after(10,pluscheck)

def minusCheck():
    if Checkmin.get() == 5:
        window.teller -= 1
        update_window()
        teller_box.after(10,minusCheck)
        
checkUP = tk.Checkbutton(text="+", onvalue=5, offvalue=6,variable=Checkplus ,command=pluscheck)
checkDown = tk.Checkbutton(text="-",onvalue=5, offvalue=6,variable=Checkmin, command= minusCheck)

#controleert de kleur
def Kleur_waarde(event):
    kleur_waarde() 
def kleur_waarde():
    if window.teller>0:
        teller_box.config(text= window.teller,bg="green")
    elif window.teller<0:
        teller_box.config(text= window.teller,bg="red")
    else:
        teller_box.config(text= window.teller,bg="grey")
#deze functie update de window constant 
def update_window():
    print(window.teller)
    kleur_waarde()
    
opteler.pack(ipady=35,ipadx=110)
teller_box.pack(ipady=35,ipadx=110)
afteler.pack(ipady=35, ipadx=110)
herstart.pack(ipady=35,ipadx=110)
checkUP.pack()
checkDown.pack()

teller_box.bind("<Double-Button-1>",verdubbel_delen)
teller_box.bind("<Enter>", highlight_Tbox)
teller_box.bind("<Leave>",Kleur_waarde)
window.bind("<Up>",Optellen)
window.bind("<Down>",Aftellen)
window.bind("<space>",verdubbel_delen)
window.bind("<Return>",herstart_teller)

window.mainloop()