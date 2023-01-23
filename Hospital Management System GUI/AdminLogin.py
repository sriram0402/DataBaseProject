import mysql.connector 
import tkinter as tk
from tkinter import *
from tkinter import ttk
from functools import partial
from tkinter import messagebox 
from tkinter.ttk import *
from adminDeletePatient import *
from editPatientDetails import *
from PIL import ImageTk,Image

db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootroot",
        database="hmsdb"
        )



def validateLogin(username,passwor):
    print(username.get(),passwor.get())
    cursor = db.cursor()
    sql=("SELECT * FROM hmsdb.admin where username=%s and admin_password=%s")
    val=(username.get(),passwor.get())
    cursor.execute(sql,val)
    data=cursor.fetchall()
    if(len(data)):
        messagebox.showinfo("showinfo","login success")
        adminMenu()
        
    else:
        messagebox.showinfo("showinfo","login unsuccess")

def adminLoginForm():

    tkWindow = Tk()  
    tkWindow.geometry('400x150')  
    tkWindow.title('Admin Login')
     


    #username label and text entry box
    usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
    username = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

    #password label and password entry box
    passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
    passwor = StringVar()
    passwordEntry = Entry(tkWindow, textvariable=passwor, show='*').grid(row=1, column=1)  



    loginButton = Button(tkWindow, text="Login", command=partial(validateLogin,username ,passwor)).grid(row=4, column=0)  

    backButton=Button(tkWindow, text="BACK", command=tkWindow.destroy).grid(row=4, column=2)

    tkWindow.mainloop()



def adminMenu():

    window = Tk()  
    window.geometry('400x150')  
    window.title('Admin Menu')

    
    patientDetails = Button(window, text="Patient Details",command=partial(adminPatientDetails)).grid(row=0, column=0)  
    

    doctorDetails = Button(window, text="Doctor Details",command=partial(doctorData)).grid(row=1, column=0)  


    adminProfile = Button(window, text="Admin Details", command=partial(adminDetails)).grid(row=2, column=0)

    deletePatient=Button(window, text="Delete Patient", command=partial(deleteForm)).grid(row=3, column=0)

    """
    editButton=Button(window, text="EDIT Patient Details", command=partial(editPatientForm)).grid(row=4,column=0 )
    """
    
def adminPatientDetails():
    
    window = Tk()  
    window.geometry('700x700')  
    window.title(' Patient Details')
    cur = db.cursor()


    tree = ttk.Treeview(window, column=("PatientID","Name", "Address", "Gender","DOB","Doctor Name","Treatment","Medicines","Doctor Charge","NurseCharge","AmbCharge"), show='headings', height=11)
    tree.column("# 1", anchor=CENTER ,width=50)
    tree.heading("# 1", text="PatientID")
    tree.column("# 2", anchor=CENTER,width=75)
    tree.heading("# 2", text="Name")
    tree.column("# 3", anchor=CENTER,width=75)
    tree.heading("# 3", text="Address")
    tree.column("# 4", anchor=CENTER,width=50)
    tree.heading("# 4", text="Gender")
    tree.column("# 5", anchor=CENTER,width=50)
    tree.heading("# 5", text="DOB")
    tree.column("# 6", anchor=CENTER,width=75)
    tree.heading("# 6", text="Doctor Name")
    tree.column("# 7", anchor=CENTER,width=75)
    tree.heading("# 7", text="Treatment")
    tree.column("# 8", anchor=CENTER,width=85)
    tree.heading("# 8", text="Medicines")
    tree.column("# 9", anchor=CENTER,width=75)
    tree.heading("# 9", text="Doctor Charge")
    tree.column("# 10", anchor=CENTER,width=85)
    tree.heading("# 10", text="Nurse Charge")
    tree.column("# 11", anchor=CENTER,width=85)
    tree.heading("# 11", text="Ambulance Charge")
    tree.pack()

    
    Select = """select patients.patientID,PatientName,patients.Address,Patients.Gender,Patients.patientDOB,Patients.DoctorName,doctor.Treatment,medicines.medicines,bill.DocCharge,bill.NurseCharge,bill.AmbCharge from patients inner join bill on patients.patientID=bill.patientID
    inner join medicines on medicines.Patients_PatientID = patients.patientID
    inner join doctor on doctor.doctorID=patients.Doctor_DoctorID"""
    
    
    cur.execute(Select)
    result = cur.fetchall()
   
    for i in result:
        tree.insert('', 'end', text="1", values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]))

    window.mainloop()

    

        
    """
    except:
        messagebox.showinfo("showinfo","error")
        window.withdraw()
        """

    return



def doctorData():


    window = Tk()  
    window.geometry('700x700')  
    window.title(' Doctor Details')
    cur = db.cursor()


    tree = ttk.Treeview(window, column=("DoctorID","Name", "Mobile", "Address","Speciality","LoginTime","LogoutTime","Gender","Age"), show='headings', height=11)
    tree.column("# 1", anchor=CENTER ,width=50)
    tree.heading("# 1", text="DoctorID")
    tree.column("# 2", anchor=CENTER,width=75)
    tree.heading("# 2", text="Name")
    tree.column("# 3", anchor=CENTER,width=75)
    tree.heading("# 3", text="Mobile")
    tree.column("# 4", anchor=CENTER,width=50)
    tree.heading("# 4", text="Address")
    tree.column("# 5", anchor=CENTER,width=50)
    tree.heading("# 5", text="Speciality")
    tree.column("# 6", anchor=CENTER,width=75)
    tree.heading("# 6", text="LoginTime")
    tree.column("# 7", anchor=CENTER,width=75)
    tree.heading("# 7", text="LogoutTime")
    tree.column("# 8", anchor=CENTER,width=85)
    tree.heading("# 8", text="Gender")
    tree.column("# 9", anchor=CENTER,width=75)
    tree.heading("# 9", text="Age")

    tree.pack()

    
    Select = """select DoctorID,DocName,Mobile,Address,Treatment, LoginTime, LogoutTime,Gender,DocAge from doctor"""
    
    
    cur.execute(Select)
    result = cur.fetchall()
   
    for i in result:
        tree.insert('', 'end', text="1", values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))
           

    window.mainloop()


        
    """
    except:
        messagebox.showinfo("showinfo","error")
        window.withdraw()
        """

    return
    


def adminDetails():
    
    window = Tk()  
    window.geometry('700x700')  
    window.title(' Admin Details')
    cur = db.cursor()


    tree = ttk.Treeview(window, column=("Name","Phone", "Username", "Password"), show='headings', height=11)
    tree.column("# 1", anchor=CENTER ,width=75)
    tree.heading("# 1", text="Name")
    tree.column("# 2", anchor=CENTER,width=75)
    tree.heading("# 2", text="Phone")
    tree.column("# 3", anchor=CENTER,width=75)
    tree.heading("# 3", text="Username")
    tree.column("# 4", anchor=CENTER,width=75)
    tree.heading("# 4", text="Password")
    tree.pack()

    
    Select = """select * from admin"""
    
    
    cur.execute(Select)
    result = cur.fetchall()
   
    for i in result:
        tree.insert('', 'end', text="1", values=(i[2],i[3],i[0],i[1]))       

    window.mainloop()


        
    """
    except:
        messagebox.showinfo("showinfo","error")
        window.withdraw()
        """

    return

adminLoginForm()

