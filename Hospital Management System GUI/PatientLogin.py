import mysql.connector 
import tkinter as tk
from functools import partial
from tkinter import *
from tkinter import messagebox
from patientDetailsDisplay import main

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootroot",
    database="hmsdb"
    )


def validateLogin(Mobile,DOB):
    try:

        print("hello",Mobile.get(),DOB.get())
        cursor = db.cursor()
        sql="SELECT * FROM hmsdb.patients where PatientMobile=%s and patientDOB=%s"
        values=(Mobile.get(),DOB.get())
        cursor.execute(sql,values)
        data=cursor.fetchall()

        if(len(data)):
            messagebox.showinfo("showinfo","login success")
            main(Mobile,DOB)
            
        else:

            messagebox.showinfo("showinfo","Invalid login")
        
    
    except:
        messagebox.showerror('error',"enter valid information ")
    

def patientLoginForm():
    

    tkWindow = Tk()  
    tkWindow.geometry('400x150')  
    tkWindow.title('Patient Login Form')


    MobileLabel = Label(tkWindow, text="Mobile").grid(row=0, column=0)
    Mobile = StringVar()
    MobileEntry = Entry(tkWindow, textvariable=Mobile).grid(row=0, column=1) 

    DOBLabel = Label(tkWindow,text="Date Of Birth").grid(row=1, column=0)  
    DOB = StringVar()
    DOBEntry = Entry(tkWindow, textvariable=DOB).grid(row=1, column=1)  

    loginButton = tk.Button(tkWindow, text="Login", command=partial(validateLogin,Mobile,DOB)).grid(row=4, column=0)
    backButton = Button(tkWindow, text="BACK", command=tkWindow.destroy).grid(row=4, column=2)
    
    tkWindow.mainloop()
    

"""
patientLoginForm()
"""
