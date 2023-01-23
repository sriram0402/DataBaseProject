import mysql.connector 
import tkinter as tk
from tkinter import *
from tkinter import ttk
from functools import partial
from tkinter import messagebox 
from tkinter.ttk import *

"""
from PatientLogin import *
from patientRegistration import *
from AdminLogin import *
from doctorLogin import *

, command=partial()
"""

def mainMenu():

    window = Tk()  
    window.geometry('400x400')  
    window.title('Main menu')

    patientLoginButton = tk.Button(window, text="Patient Login").grid(row=1, column=0)
    adminLoginButton = tk.Button(window, text="Admin Login").grid(row=2, column=0)
    doctorLoginButton = tk.Button(window, text="Doctor Login").grid(row=3, column=0)
    patientRegButton = tk.Button(window, text="Patient Registration").grid(row=4, column=0)

mainMenu()
