#Import the required libraries
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootroot",
        database="hmsdb"
        )




def main(patientMobile,patientDOB):
    try:
        tkWindow = Tk()  
        tkWindow.geometry('700x700')  
        tkWindow.title(' Details')
        cur = db.cursor()


        tree = ttk.Treeview(tkWindow, column=("PatientID","Name", "Address", "Gender","DOB","Doctor Name","Treatment","Medicines","Doctor Charge","NurseCharge","AmbCharge"), show='headings', height=4)
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
        inner join doctor on doctor.doctorID=patients.Doctor_DoctorID 
        where patients.patientMobile=%s and patients.patientDOB=%s"""
        
        val=(patientMobile.get(),patientDOB.get())
        cur.execute(Select,val)
        result = cur.fetchall()
       
        for i in result:
            tree.insert('', 'end', text="1", values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]))
        

        tkWindow.mainloop()
    except:
        messagebox.showinfo("showinfo","error")

    return

