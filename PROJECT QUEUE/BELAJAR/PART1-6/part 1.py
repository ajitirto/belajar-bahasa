import tkinter
import random
from tkinter import*

#Create root window
root = tkinter.Tk()


root.configure(bg="white")

tasks=[]
tasks=["call mom", "buy guitar","Eat shusi"]


#Create Function

def update_listbox():
    for task in tasks:
        lb_tasks.insert("end",task)
def clear_ilstbox():
    lb_task.delete(0, "end")

def add_task():
    update_listbox()
def delete():
    pass
def delete_one():
    pass
def sort_desc():
    pass

root.geometry("200x600")
root.title("BGP")

lbl_title=tkinter.Label(root, text="PERCOBAAN 1", bg = "white")
lbl_title.pack()

lbl_title=tkinter.Label(root, text="", bg = "white")
lbl_title.pack()

lbl_input=tkinter.Entry(root, width=15)
lbl_input.pack()

btn_add_task = tkinter.Button(root, text = "Add task", fg="green", bg="white", command=add_task)
btn_add_task.pack()

btn_delete_all = tkinter.Button(root, text = "Delete all", fg="green", bg="white", command=delete)
btn_delete_all.pack()

btn_delete_one = tkinter.Button(root, text = "delete one", fg="green", bg="white", command=delete_one)
btn_delete_one.pack()

btn_sort_desc = tkinter.Button(root, text = "sort_desc", fg="green", bg="white", command=sort_desc)
btn_sort_desc.pack()

lb_tasks= tkinter.Listbox(root)
lb_tasks.pack()



##btn = tkinter.Button(root, text = "", fg="green", bg="white", command=)
##btn.pack()

#Create Main loop
root.mainloop()