from tkinter import *
import mysql.connector
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




# database connection
cnx = mysql.connector.connect(user='root', password='',host='localhost')
cursor = cnx.cursor()



# create database and table
cursor.execute("create DATABASE IF NOT EXISTS budgeterist;")
cursor.execute("USE budgeterist")
cursor.execute("CREATE TABLE IF NOT EXISTS expenses  ( id INT AUTO_INCREMENT PRIMARY KEY, expenses VARCHAR(255), amount INT);")



def add():
    os.system('py addExpenses.py')


# Background
bg = PhotoImage(file='img/dashboard.png')
bgf = Label(root,image=bg ,bg="#292626")
bgf.place(x=0,y=0)


# Container for contents
container = Frame(root, height=800, width=1320,bg="#292626")
container.place(x=65,y=180)


# Past expenses
bg_past = PhotoImage(file='img/Past Expenses.png')
bgf_past = Label(container,image=bg_past ,bg="#292626")
bgf_past.grid(row=1, column=1)

# Adding space 
space_frame = Frame(container, width=80, height=100, bg="#292626")
space_frame.grid(row=1, column=2)

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


# Total
total = PhotoImage(file='img/total.png')
totalF = Label(te_frame,image=total, bd=0, bg="#292626")
totalF.grid(column=1, row=3)


# Spacing
space3 = Frame(te_frame, height=27, bg="#292626")
space3.grid(column=1, row=4)

# Add expenses
addbtn = PhotoImage(file='img/Add.png')
addbtnf = Button(te_frame,image=addbtn,bd=0, bg="#292626", command=add)
addbtnf.grid(column=1, row=5)

# Spacing
space4 = Frame(te_frame, height=27, bg="#292626")
space4.grid(column=1, row=6)

card = PhotoImage(file='img/addExp.png')
delete = PhotoImage(file='img/delete.png')
edit = PhotoImage(file='img/edit.png')


cursor = [("shhesh"), ("lalala"), ("sasa")]
i = 0
for data in cursor:
    cardf = Label(te_frame,image=card,bd=0,bg="#292626")
    # deltf = Button(cardf,image=delete,bd=0,bg="#292626",cursor="hand2")
    # editf= Button(cardf,image=edit,bd=0,bg="#292626",cursor="hand2")
    # editf.place(x=20,y=10)
    # deltf.place(x=120,y=10)
    expenses = Label(cardf,font=("Arial ", 18),fg="#000000",bg="#292626")
    expenses.place(x=0, y=0)
    cardf.grid(row=7+i+1, column=1)
    i = i + 1





root.mainloop() 