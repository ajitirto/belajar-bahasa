from tkinter import messagebox,Tk,Button,LabelFrame,Label,Canvas,IntVar,Radiobutton,Entry,Listbox, Scrollbar,END
from time import sleep
from ProgramQueue import *
Pq=Queue()
for i in Lists:
    Pq.enqueue(i)
X=Tk()
X.geometry("640x480+100+100")
X.title("Queue System")
X.resizable(width=False, height=False)
labelframe = LabelFrame(X, cursor="target")
labelframe.pack(fill = "both", expand = "yes")

def dequeue():
    if var.get()==3:
        if len(Pq)==0 and A1.get()!='0':
            messagebox.showinfo("Stop","Queue has been empty")
        else:
            if A1.get()!='0':
                Lb1.delete(0,int(A1.get())-1)
            for i in range(int(A1.get())):
                if len(Pq)==0:
                    messagebox.showinfo("Stop","Queue has been empty")
                    break;
                Lb2.insert(0,Pq.dequeue().name)
    elif var.get()==2:
        if len(Pq)==0:
            messagebox.showinfo("Stop","Queue has been empty")
        else:
            Lb1.delete(0,0)
            Lb2.insert(0,Pq.dequeue().name)
    elif var.get()==1:
        if len(Pq)==0:
            messagebox.showinfo("Stop","Queue has been empty")
        else:
            Lb1.delete(0,END)
            for i in range(len(Pq.qlist)):
                Lb2.insert(0,Pq.dequeue().name)
    
def selectbox():
    if var.get()==3:
        A.config(state="normal")
        A1.config(state='normal')
        A1.delete(0,END)
        A1.insert(0,0)
    elif var.get()==2:
        A.config(state="normal")
        A1.config(state='normal')
        A1.delete(0,END)
        A1.insert(0,1)
        A1.config(text=1,state='disabled')
    elif var.get()==1:
        A.config(state="normal")
        A1.config(state='normal')
        A1.delete(0,END)
        A1.config(state='disabled')

## Making Button on center of interface
var = IntVar()
R1 = Radiobutton(labelframe, font=('algerian',20), text = "All", variable = var, value = 1, command = selectbox)
R1.place(x=270,y=150)
R2 = Radiobutton(labelframe, font=('algerian',20), text = "By 1", variable = var, value = 2, command = selectbox)
R2.place(x=270,y=186)
R3 = Radiobutton(labelframe, font=('algerian',20), text = "By X", variable = var, value = 3, command = selectbox)
R3.place(x=270,y=222)
A1=Entry(labelframe,font=('algerian',20),bd=2,width=4)
A1.place(x=285,y=265)
A1.config(state='disabled')
A=Button(labelframe,font=('algerian',20),text="Queue",command=dequeue)
A.place(x=267, y=315)
B=Button(labelframe,font=('algerian',20),text="Edit",command=None)
B.place(x=280, y=375)
A.config(state="disabled")

## Make left layer
subLF1=LabelFrame(labelframe,width="237",height="410")
subLF1.place(x=10,y=60)
Lb1 = Listbox(subLF1,width="38",height="25")
Lb1.place(x=0,y=0)
for i in range(len(Pq)):
    Lb1.insert(i,Pq.qlist[i].name)

## Make right layer
subLF2=LabelFrame(labelframe,width="237",height="410")
subLF2.place(x=390,y=60)
Lb2 = Listbox(subLF2,width="38",height="25")
Lb2.place(x=0,y=0)

## Looping main
X.mainloop()