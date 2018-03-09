import tkinter as tk        #1
from tkinter import ttk
win=tk.Tk()                  #2
win.title("Python GUI")     #3

#Adding a Label
ttk.Label(win,text="A Lable").grid(column=0,row=0)  #5

#win.resizable(0,0)          #6

#MOdify adding a Label                          #1
aLabel = ttk.Label(win,text="A Label")         #2
aLabel.grid(column=0,row=0)                     #3


#Button click Event callback Function           #4

def clickMe():                                  #5
    #action.configure(text="*** I have Clicked! ***")
    #aLabel.configure(foreground='red')
    action.configure(text="Hello " + name.get()+' '+numberChosen.get())
#Adding a Button                                #6
#Position Button in second row, second column (zero-bassed)
action=ttk.Button(win,text="Click Me!",command=clickMe)
#action.configure(state='disabled')          #setting state
action.grid(column=2,row=1)

#Changing our Label
ttk.Label(win,text="Enter a name:").grid(column=0,row=0)

#Adding a Textbox Entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(win,width=12,textvariable=name)
nameEntered.focus()
nameEntered.grid(column=0,row=1)

ttk.Label(win,text="Choose a number:").grid(column=1,row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(win,width=12,textvariable=number)
numberChosen['values']=(1,24,42,100)
numberChosen.grid(column=1,row=1)
numberChosen.current(0)

#Creating three checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win,text='Disabled',variable=chVarDis,state='disabled')
check1.select()
check1.grid(column=0,row=4,sticky=tk.W)

chVarUn = tk.IntVar()
check2=tk.Checkbutton(win,text="Unchecked",variable=chVarUn)
check2.deselect()
check2.grid(column=1,row=4,sticky=tk.W)

chVarEn =tk.IntVar()
check3=tk.Checkbutton(win,text="Enabled",variable=chVarEn)
check3.select()
check3.grid(column=2,row=4,sticky=tk.W)

   #7
#action.grid(column=1,row=0)

#Creating three checkbutton

#Radiobutton Globals
COLOR1= "Blue"
COLOR2= "Gold"
COLOR3 = "Red"

#Radiobutton Callback
def radCall():
    radSel =radVar.get()
    if radSel == 1: win.configure(background=COLOR1)
    elif radSel == 2: win.configure(background=COLOR2)
    elif radSel == 3:win.configure(background =COLOR3)

#create three Radiobuttons
radVar = tk.IntVar()
rad1 = tk.Radiobutton(win,text=COLOR1,variable=radVar,value=1,command=radCall)
rad1.grid(column=0,row=5,sticky=tk.W)

rad2 = tk.Radiobutton(win,text=COLOR2,variable=radVar,value=2,command=radCall)
rad2.grid(column=1,row=5,sticky=tk.W)

rad3=tk.Radiobutton(win,text=COLOR3,variable=radVar,value=3,command=radCall)
rad3.grid(column=2,row=5,sticky=tk.W)


win.mainloop()               #7