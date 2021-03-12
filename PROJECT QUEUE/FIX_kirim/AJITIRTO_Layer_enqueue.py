import tkinter
import random
from tkinter import*

root = Tk()
##root.geometry("640x480")
root.geometry("560x350")
root.title("Enqueue Layer")

#----------function-------------


#--------------------background------------------
bg= tkinter.Frame(root, width = 640,height=480, bg = "#EE4065")
bg.pack()

#----------------------------Label-------------------------
lbl_judul=tkinter.Label(root, font=('11S01 Black Tuesday', 25),text="Enqueue",fg="green", bg = "white")
lbl_judul.pack()
#----------------------------------------------------------------
lbl_input=tkinter.Label(root, font=('11S01 Black Tuesday', 12,'bold'),text="Masukan Data",fg="blue", bg = "white")
lbl_input.pack()

lbl_notlisted=tkinter.Label(root, font=('11S01 Black Tuesday', 12,'bold'),text="Not Listed",fg="blue", bg = "white")
lbl_notlisted.pack()

lbl_enqL=tkinter.Label(root, font=('11S01 Black Tuesday', 12,'bold'),text="Enqueue list",fg="blue", bg = "white")
lbl_enqL.pack()

#----------------------------Button-------------------------
btn = Button( font= ('11S01 Black Tuesday',8,'bold'), text='Satu ', bg='white')
btn.pack()

btn2 = Button( font= ('11S01 Black Tuesday',8,'bold'), text='Dua  ', bg='white')
btn2.pack()

btn3 = Button( font= ('11S01 Black Tuesday',8,'bold'), text='Tiga ', bg='white')
btn3.pack()

btn4 = Button( font= ('11S01 Black Tuesday',8,'bold'), text='Empat', bg='white')
btn4.pack()

btn5 = Button( font= ('11S01 Black Tuesday',8,'bold'), text='Lima', bg='white')
btn5.pack()

btn6 = Button( font= ('11S01 Black Tuesday',8,'bold'), text='Enam', bg='white')
btn6.pack()

btn7 = Button( font= ('11S01 Black Tuesday',8,'bold'), text='Tujuh', bg='white')
btn7.pack()

btn8 = Button( font= ('11S01 Black Tuesday',26,'bold'), text='Dequeue',fg='blue', bg='white')
btn8.pack()
#-----------------------Tempat-------------------
lbl_judul.place(x= 220, y=10)
lbl_input.place(x= 250, y=60)
lbl_notlisted.place(x=250, y = 88)
lbl_enqL.place(x=250, y = 115)

btn.place(x= 360, y=60)
btn2.place(x= 400, y=60)
btn3.place(x= 360, y=90)
btn4.place(x= 400, y=90)
btn5.place(x= 450, y=90)
btn6.place(x= 494, y=90)
btn7.place(x= 360, y=120)
btn8.place(x= 220, y=170)

root.mainloop()