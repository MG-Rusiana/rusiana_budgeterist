from tkinter import *
import mysql.connector




root = Tk()
root.title('Budgeterist')
root.iconbitmap('./img/icon.ico')
height = 495
width = 671
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(False, True)
root.configure(bg="#292626")


# Background
bg = PhotoImage(file='img/addWin.png')
bgf = Label(root,image=bg ,bg="#292626")
bgf.place(x=0,y=0)


def add():
    root.destroy()

# Get started button
addbtn =   PhotoImage(file='img/addBtn.png')
addbtnf = Button(root,image=addbtn,bd=0, bg="#292626", command=add)
addbtnf.place(x=250,y=400)


root.mainloop() 