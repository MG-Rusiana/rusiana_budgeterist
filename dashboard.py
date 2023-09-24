from tkinter import *
import mysql.connector
import os
import json
from tkinter import messagebox




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




# database connection
cnx = mysql.connector.connect(user='root', password='',host='localhost')
cursor = cnx.cursor()

# create database and table
cursor.execute("create DATABASE IF NOT EXISTS budgeterist;")
cursor.execute("USE budgeterist")
cursor.execute("CREATE TABLE IF NOT EXISTS expenses  ( id INT AUTO_INCREMENT PRIMARY KEY, expenses VARCHAR(255), amount INT);")

# Variables
ID = IntVar()
EXPENSES = StringVar()
AMOUNT = IntVar()
TOTAL = IntVar()


# adding expenses
def add():
    root.withdraw()
    os.system('py addExpenses.py')

# updating expenses
def edit(id, expenses, amount):
    root.withdraw()
    data = {
        'id': id,
        'expenses': expenses,
        'amount': amount,
    }
    with open('data.json', 'w') as f:
        json.dump(data, f)
    os.system('py editExpenses.py')

# deleting expenses
def delete(id):
    result = messagebox.askquestion("Confirmation", "Do you want to delete this item?")
    if result == "yes":
        cursor.execute(f"DELETE FROM expenses WHERE id = {id};")
        cnx.commit()
        print("ITEM ", id, " is deleted")
        for widget in expF.winfo_children():
            widget.destroy()
            totalAmount()
        display()
        print("Action confirmed.")
    else:
        print("Action canceled.")

    

# Background
bg = PhotoImage(file='img/dashboard.png')
bgf = Label(root,image=bg ,bg="#292626")
bgf.place(x=0,y=0)


# Container for contents
container = Frame(root, height=800, width=1320,bg="#292626")
container.place(x=80,y=180)


# Past expenses
bg_past = PhotoImage(file='img/Past Expenses.png')
bgf_past = Label(container,image=bg_past ,bg="#292626")
bgf_past.grid(row=1, column=1)

# Adding space 
space1 = Frame(container, width=130, bg="#292626")
space1.grid(row=1, column=2)

# Frame for today's expenses
te_frame = Frame(container, width=550, height=100, bg="#292626")
te_frame.grid(row=1, column=3)

# Expenses today text
bg_te = PhotoImage(file='img/Expenses Today.png')
bgf_te = Label(te_frame,image=bg_te ,bg="#292626")
bgf_te.grid(column=1, row=1)

# Spacing
space2 = Frame(te_frame, height=27, bg="#292626")
space2.grid(column=1, row=2)


# Displaying the Total amount
totalbg = PhotoImage(file='img/total.png')
totalF = Label(te_frame,image=totalbg, bd=0, bg="#292626")
totalF.grid(column=1, row=3)

def totalAmount():
    cursor.execute("SELECT * FROM expenses;")

    i = 0
    total = 0
    for data in cursor: 
        total = total + data[2]

        i = i + 1

    print(total, TOTAL)
    TOTAL.set(total)

total_lbl = Label(totalF, textvariable=TOTAL, font=("Tibetan Machine Uni", 21),fg="#292626",bg="#EDE2E2")
total_lbl.place(x=220, y=13)

totalAmount()



# Spacing
space3 = Frame(te_frame, height=27, bg="#292626")
space3.grid(column=1, row=4)

# Add expenses
addbtn = PhotoImage(file='img/Add.png')
addbtnf = Button(te_frame,image=addbtn,bd=0, bg="#292626", command=add, activebackground="#292626")
addbtnf.grid(column=1, row=5)

# Spacing
space4 = Frame(te_frame, height=27, bg="#292626")
space4.grid(column=1, row=6)

# Expenses Frame
expF = Frame(te_frame, bg="#292626")
expF.grid(column=1, row=7)


# Display the added expenses for the day
card = PhotoImage(file='img/addExp.png')
deletebtn = PhotoImage(file='img/delete.png')
editbtn = PhotoImage(file='img/edit.png')

def display():

    cursor.execute("SELECT * FROM expenses;")
    
    i = 0
    for data in cursor:

        cardf = Label(expF,image=card,bd=0,bg="#292626")

        editExp = Button(cardf,image=editbtn, bd=0,bg="#292626",activebackground="#292626",cursor="hand2", command=lambda id=data[0], expenses=data[1] , amount=data[2]: edit(id,expenses,amount))
        editExp.grid(row=1, column=1)

        space5 = Frame(cardf, width=10, bg="#292626")
        space5.grid(row=1, column=2)     

        deleteExp = Button(cardf,image=deletebtn, bd=0,bg="#292626",activebackground="#292626",cursor="hand2", command=lambda id=data[0]: delete(id))
        deleteExp.grid(row=1, column=3)

        space6 = Frame(cardf, width=20, bg="#292626")
        space6.grid(row=1, column=4)   

        expenses = Label(cardf, text=data[1], padx=0, font=("Tibetan Machine Uni", 21),fg="#ffffff",bg="#292626")
        expenses.grid(row=1, column=5)

        equals = Label(cardf, text="  =  ", font=("Tibetan Machine Uni", 21),fg="#ffffff",bg="#292626")
        equals.grid(row=1, column=6)

        amount = Label(cardf, text=data[2], font=("Tibetan Machine Uni", 21),fg="#ffffff",bg="#292626")
        amount.grid(row=1, column=7)

        cardf.grid(row=7+i+1, column=1, sticky="w")

        i = i + 1

display()




root.mainloop() 