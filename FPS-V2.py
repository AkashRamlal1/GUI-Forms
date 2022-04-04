
import tkinter as tk
from tkinter import ttk
from tkinter import *
import random
from tkinter.tix import Tree


window = tk.Tk()
window.geometry("1000x1000")
punten = 0
timer = ttk.Entry()
bind_list = ['<w>','<s>','<r>','<a>','<space>','<Button>','<Double-Button>','<Triple-Button>']
onhold = True
keuze = random.choice(bind_list)


def TrainerStart():
    global startknop, custom_time_container, punten_label, timer, onhold
    
    onhold = False
    startknop.place_forget()
    startknop = tk.Button(window,bg="grey",text= "start trainer", command=TrainerStart)
    custom_timer = int(timer.get())
    chosen_time = int(timer.get())
    timer.place_forget()
    timer = ttk.Entry()
    print("je wilt een tijd van ",custom_timer)
    custom_time_container.config(text=custom_timer)
    custom_time_container.place(x=950,y=30,)
    punten_label.place(x=951,y=50)
    opdrachtlabel.place(x=(random.randrange(1000)),y=(random.randrange(1000)))
    custom_time_container.after(1000, lambda: stopwatch(custom_timer))

def restartTrainer():
    global timer, vervolglabel,vervolglabel_no,vervolglabel_yes, punten,custom_time_container,startknop,punten_label
    
    
    startknop.place(x=480,y=550)
    timer.place(x=480,y=420)
   
    scorelabel.place_forget()
    vervolglabel.place_forget()
    vervolglabel_yes.place_forget()
    vervolglabel_no.place_forget()
    punten = 0
    punten_label.config(text=punten)
    
    

def stopit():
    window.destroy()

def stopwatch(custom_timer):
    global custom_time_container ,punten,scorelabel,vervolglabel_yes,vervolglabel,vervolglabel_no,punten_label,opdrachtlabel,onhold
    print(custom_timer)
    custom_timer = int(custom_timer) - 1
    scorelabel.config(text="je score was {}".format(punten))
    custom_time_container.config(text=custom_timer)
    if custom_timer != 0:
        custom_time_container.after(1000, lambda: stopwatch(custom_timer))

    elif custom_timer == 0:
        
        scorelabel.place(x=480,y=320)
        vervolglabel.place(x=480,y=360)
        vervolglabel_yes.place(x=500,y=500)
        vervolglabel_no.place(x=520,y=500)
        opdrachtlabel.place_forget()
        onhold = True
        opdrachtlabel = tk.Label(text = "klik op {}".format(keuze))
        




    



custom_time_container = tk.Label()
punten_label = tk.Label(text= punten)
opdrachtlabel = tk.Label(text = "klik op {}".format(keuze))
scorelabel = tk.Label(text="je score was {}".format(punten))
vervolglabel = tk.Label(text= "wil je verder spelen")
vervolglabel_yes = tk.Button(text ="ja", command=restartTrainer)
vervolglabel_no = tk.Button(text ="nee",command=stopit)

def opdracht(event):
    
    global punten,opdrachtlabel,bind_list,timer,keuze, punten_label, onhold


    if onhold == True:
        print('start eerst een spel')


    elif onhold == False:
        punten = punten+ 1
        punten_label.config(text=punten)
        opdrachtlabel.place(x=(random.randrange(1000)),y=(random.randrange(1000)))
        window.unbind(keuze)
        keuze = random.choice(bind_list)
        
        opdrachtlabel.config(text="klik op {}".format(keuze))
        window.bind(keuze,opdracht)


startknop = tk.Button(window,bg="grey",text= "start trainer", command=TrainerStart)
window.bind(keuze, opdracht)
timer.place(x=480,y=420)
timer.insert(0,20)
startknop.place(x=480,y=450)

window.mainloop()