"""
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

def editPatient(patientID):
    print(patientID.get())

def editPatientForm():
    tkWindow = Tk()  
    tkWindow.geometry('400x400')  
    tkWindow.title('Update Patient Details')


    patientIDLabel = Label(tkWindow, text="Patient ID").grid(row=0, column=0)
    patientID = IntVar()
    patientIDEntry = Entry(tkWindow, textvariable=patientID).grid(row=0, column=1)


    nextButton = Button(tkWindow, text="NEXT", command=lambda:editPatient(patientID)).grid(row=4, column=0)
    if(nextButton):
        print("If",patientID.get())


"""




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
def editPatient(patID):
    print("222",patID)
def editPatientForm():

    tkWindow = Tk()  
    tkWindow.geometry('400x150')  
    tkWindow.title('Update Patient')

    
    patientIDLabel = Label(tkWindow, text="Patient ID").grid(row=0, column=0)
    patientID = StringVar()
    patientIDEntry = tk.Entry(tkWindow, textvariable=patientID).grid(row=0, column=1)
    print("inside function:",patientID.get())

    nextButton = Button(tkWindow, text="NEXT", command=partial(editPatient,patientID.get())).grid(row=4, column=0)
    
    backButton=Button(tkWindow, text="BACK", command=tkWindow.destroy).grid(row=4, column=2)

    tkWindow.mainloop()
