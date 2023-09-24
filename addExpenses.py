from tkinter import *
import mysql.connector
import os
from tkinter import messagebox



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




# database connection
cnx = mysql.connector.connect(user='root', password='',host='localhost')
cursor = cnx.cursor()


# create database and table
cursor.execute("create DATABASE IF NOT EXISTS budgeterist;")
cursor.execute("USE budgeterist")
cursor.execute("CREATE TABLE IF NOT EXISTS expenses  ( id INT AUTO_INCREMENT PRIMARY KEY, expenses VARCHAR(255), amount INT);")


# Variables
EXPENSES = StringVar()
AMOUNT = IntVar()



# Background
bg = PhotoImage(file='img/addWin.png')
bgf = Label(root,image=bg ,bg="#292626")
bgf.place(x=0,y=0)


# functions

def add():
    if EXPENSES.get() == "" or AMOUNT.get() == 0:
        messagebox.showwarning("INCOMPLETE FIELDS!", "Please complete the missing fields!")
    else:          
        cursor.execute(f"INSERT INTO expenses (expenses, amount) VALUES ('{EXPENSES.get()}', {AMOUNT.get()});")
        cnx.commit()
        root.destroy()
        os.system('py dashboard.py')
      

def cancel():
    root.withdraw()
    os.system('py dashboard.py')

# inputs
expenses = Entry(root, textvariable=EXPENSES,font=("Tibetan Machine Uni", 21),fg="#292626",bg="#FFF4F4",width=29,bd=0)
expenses.place(x=100, y=180)
amount = Entry(root, textvariable=AMOUNT,font=("Tibetan Machine Uni", 21),fg="#292626",bg="#FFF4F4",width=29,bd=0)
amount.place(x=100, y=310)


# Cancel Button
cancelbtn =   PhotoImage(file='img/cancel.png')
cancelbtnf = Button(root,image=cancelbtn,bd=0, bg="#292626", command=cancel, activebackground="#292626")
cancelbtnf.place(x=135,y=400)

# Add button
addbtn =   PhotoImage(file='img/addBtn.png')
addbtnf = Button(root,image=addbtn,bd=0, bg="#292626", command=add, activebackground="#292626")
addbtnf.place(x=370,y=400)


root.mainloop() 