import mysql.connector 
import tkinter as tk
from tkinter import *
from functools import partial
from tkinter import messagebox
from doctorAppt import *

db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootroot",
        database="hmsdb"
        )
def validateLogin(username,passwor):

    print(username.get(),passwor.get())
    cursor = db.cursor()
    sql=("SELECT * FROM hmsdb.Doctor where DocUserName=%s and Password=%s")
    val=(username.get(),passwor.get())
    cursor.execute(sql,val)
    data=cursor.fetchall()
    doctorId=str(data[0][0])
    if(len(data)):
        messagebox.showinfo("showinfo","login success")
        doctorAppt([data[0][0]])
        
    else:
        messagebox.showinfo("showinfo","login unsuccess")
    """
    except:
        messagebox.showerror("showerror","error occured login")"""

def doctorLoginForm():
    tkWindow = Tk()  
    tkWindow.geometry('400x150')  
    tkWindow.title('Doctor Login')
    #username label and text entry box
    usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
    username = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

    #password label and password entry box
    passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
    passwor = StringVar()
    passwordEntry = Entry(tkWindow, textvariable=passwor, show='*').grid(row=1, column=1)  

    #login button
    loginButton = Button(tkWindow, text="Login", command=partial(validateLogin,username ,passwor)).grid(row=4, column=0)  

    backButton=Button(tkWindow, text="BACK", command=tkWindow.destroy).grid(row=4, column=2)

    tkWindow.mainloop()
doctorLoginForm()
