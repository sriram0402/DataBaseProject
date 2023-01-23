import mysql.connector 
import tkinter as tk
from tkinter import *
from tkinter import ttk
from functools import partial
from tkinter import messagebox 
from tkinter.ttk import *

db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootroot",
        database="hmsdb"
        )
def deletePatientRecord(patID):
    cursor = db.cursor()
    sql="Delete from patients where patientID = '%s'" % patID.get()
    val=(patID)
    cursor.execute(sql)
    db.commit()
    messagebox.showinfo("showinfo",'Patient Record Deleted')
def deleteForm():

    tkWindow = Tk()  
    tkWindow.geometry('400x150')  
    tkWindow.title('Delete Patient')

    
    patientIDLabel = Label(tkWindow, text="Patient ID").grid(row=0, column=0)
    patientID = IntVar()
    patientIDEntry = tk.Entry(tkWindow, textvariable=patientID).grid(row=0, column=1) 

    deleteButton = Button(tkWindow, text="DELETE", command=partial(deletePatientRecord,patientID)).grid(row=4, column=0)
    
    backButton=Button(tkWindow, text="BACK", command=tkWindow.destroy).grid(row=4, column=2)
    
