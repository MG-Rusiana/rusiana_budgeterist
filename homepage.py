from tkinter import *
import os




root = Tk()
root.title('Budgeterist')
root.iconbitmap('./img/icon.ico')
height = 1024
width = 1440
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(False, True)
root.configure(bg="#292626")



# Functions

def getStarted():
    root.withdraw()
    os.system('py dashboard.py')



# Background
bg = PhotoImage(file='img/Homepage.png')
bgf = Label(root,image=bg ,bg="#292626")
bgf.place(x=0,y=0)



# Get started button
btn =   PhotoImage(file='img/Get Started.png')
btnf = Button(root,image=btn,bd=0, bg="#292626", command=getStarted)
btnf.place(x=600,y=600)



root.mainloop()