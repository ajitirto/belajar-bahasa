import tkinter
import random
from tkinter import*

from ProgramQueue import *

pq=Queue()

root = Tk()
root.geometry("640x480+200+100")
root.title("Enqueue Layer")

#----------function-------------

##root.resizable(width=False, height=False)
##labelframe = LabelFrame(root, cursor="target")
##labelframe.pack(fill = "both", expand = "yes")

#--------------------background------------------
bg= tkinter.Frame(root, width = 640,height=480)
bg.pack()

#----------------------------Label-------------------------
lbl_judul=tkinter.Label(root, font=('calibri', 25,'bold'),text="Enqueue",fg="green", bg = "white")
lbl_judul.pack()
#----------------------------------------------------------------
lbl_input=tkinter.Label(root, font=('calibri', 10,'bold'),text="List",fg="black", bg = "white")
lbl_input.pack()

lbl_edit=tkinter.Label(root, font=('calibri', 10,'bold'),text="Edit",fg="black", bg = "white")
lbl_edit.pack()
#-----------Button-------------------------------------
btn_input=tkinter.Button(root,text="Input",width=10)
btn_input.pack()

btn_remove=tkinter.Button(root,text="remove",width=10,bg="red",fg="white")
btn_remove.pack()

btn_edit=tkinter.Button(root,text="edit",width=10,bg="blue",fg="white")
btn_edit.pack()

btn_deq=tkinter.Button(root,text="Dequeue",font = ("calibri",20,"bold"),width=10)
btn_deq.pack()


btn_back=tkinter.Button(root,text="back",width=10,)
btn_back.pack()
#----------------kotak isi------------------
subLF1=tkinter.LabelFrame(width="280",height="130")

#----------------Kotaknya kotak-------------
Lb1 = tkinter.Listbox(width="43",height="7")


#-------function---------------------------------------------------------
def input():
    pq.enqueue()
                
            
def edit():
    pass

def back():
    pass
def remove():
    pass

def dequeue():
    pass
#----------text field ATAS------------
txt_input=tkinter.Entry(root, width=3)
txt_input.pack()

txt_input1=tkinter.Entry(root, width=10)
txt_input1.pack()

txt_input2=tkinter.Entry(root, width=10)
txt_input2.pack()

txt_input3=tkinter.Entry(root, width=10)
txt_input3.pack()
#----------text field BAWAH--------------
txt_input4=tkinter.Entry(root, width=3)
txt_input4.pack()

txt_input5=tkinter.Entry(root, width=10)
txt_input5.pack()

txt_input6=tkinter.Entry(root, width=10)
txt_input6.pack()

txt_input7=tkinter.Entry(root, width=10)
txt_input7.pack()


#-----------------------Tempat-------------------
lbl_judul.place(x= 250, y=50)

#--------------text input-----------------
txt_input.place(x=150,y=150);txt_input1.place(x=200,y=150);txt_input2.place(x=300,y=150);txt_input3.place(x=400,y=150)
txt_input4.place(x=150,y=320);txt_input5.place(x=200,y=320);txt_input6.place(x=300,y=320);txt_input7.place(x=400,y=320)

#---------------tombol-------------------
btn_input.place(x=480,y=149);btn_remove.place(x=480,y=230);btn_edit.place(x=480,y=320)
btn_deq.place(x=230,y=380),btn_back.place(x=10,y=10)
#---------kotak--------------

subLF1.place(x=193,y=175);Lb1.place(x=200,y=180)

#---------Label----------------------
lbl_input.place(x=100,y=150);lbl_edit.place(x=100,y=320)



root.mainloop()




















