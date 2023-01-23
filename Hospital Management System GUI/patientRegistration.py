import mysql.connector 
import tkinter as tk
from tkinter import *
from functools import partial
from PatientLogin import *
from tkinter import messagebox
from tkcalendar import DateEntry


db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootroot",
        database="hmsdb"
        )

"""
select='select DISTINCT(Treatment) from doctor';
cursorSelect=db.cursor()
cursorSelect.execute(select)
records=cursorSelect.fetchall()
"""

def validateLogin(Name,Mobile,Address,Gender,patientDOB,age,Status,Treatment,dtOfAppt):
    
    data=Treatment.get()
    treatmentName=[0]*1
    treatmentName[0]=(data.strip("()',"))
    
    cursor = db.cursor()
    sqlDoctorName="select DocName,DoctorID from doctor where treatment=%s order by rand() limit 1";
    valDoc=(treatmentName)
    cursor.execute(sqlDoctorName,valDoc)

    for i in cursor:
        docName=i
    print(docName)
    
    sql='insert into patients(PatientName, PatientMobile, Address, PatientDOB, age, Gender, DoctorName, status,Doctor_DoctorID) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)';
    val=(Name.get(),Mobile.get(),Address.get(),patientDOB.get(),age.get(),Gender.get(),docName[0],Status.get(),docName[1])
    cursor.execute(sql,val)
    db.commit()

    print(cursor.rowcount)

    if (cursor.rowcount == 1):
        
        msg=messagebox.showinfo("showinfo","Successfully Registered,Please Login")

    
        sqlMedicines="""insert into medicines(Medicines,Patients_PatientID,Doctor_DoctorID)
        values(NULL,(select PatientId from patients where patientmobile=%s and patientDOB=%s),(select Doctor_DoctorID from patients where patientmobile=%s and patientDOB=%s))"""
        valMedicines=(Mobile.get(),patientDOB.get(),Mobile.get(),patientDOB.get())
        
        """
        sqlRoom="insert into room(RoomNumber,RoomType,DoctorID,NurseID,PatientID)
        values(NULL,NULL,(select Doctor_DoctorID from patients where patientmobile=%s and patientDOB=%s),(select NurseID from nurse order by rand() limit 1),(select PatientID from patients where patientmobile=%s and patientDOB=%s))""
        valRoom=(Mobile.get(),patientDOB.get(),Mobile.get(),patientDOB.get())
        """
        sqlBill="""insert into bill(PatientID,DocCharge,NurseCharge,AmbCharge)
        values((select PatientId from patients where patientmobile=%s and patientDOB=%s),NULL,NULL,NULL)"""
        valBill=(Mobile.get(),patientDOB.get())

        cursor.execute(sqlMedicines,valMedicines)
        cursor.execute(sqlBill,valBill)
        db.commit()
        if(msg):
            patientLoginForm()
            
    
    
def validate(hello):
    print(hello)

def registraionForm():


    tkWindow = Tk()  
    tkWindow.geometry('400x400')  
    tkWindow.title('Patient Registration Form ')
    
    gender=['M','F']
    statusList=['in_patients','out_patients']
    
    
    select='select DISTINCT(Treatment) from doctor';
    cursorSelect=db.cursor()
    cursorSelect.execute(select)
    records=cursorSelect.fetchall()

    NameLabel = Label(tkWindow, text="Patient Name").grid(row=0, column=0)
    Name = StringVar()
    NameEntry = Entry(tkWindow, textvariable=Name).grid(row=0, column=1)

    AddressLabel = Label(tkWindow, text="Patient Address").grid(row=1, column=0)
    Address = StringVar()
    AddressEntry = Entry(tkWindow, textvariable=Address).grid(row=1, column=1)


    MobileLabel = Label(tkWindow, text="Mobile").grid(row=2, column=0)
    Mobile = StringVar()
    MobileEntry = Entry(tkWindow, textvariable=Mobile).grid(row=2, column=1)

    GenderLabel = Label(tkWindow, text="Patient Gender").grid(row=3, column=0)
    Gender = StringVar()
    GenderEntry = OptionMenu(tkWindow,Gender,*gender).grid(row=3, column=1)


    patientDOBLabel = Label(tkWindow,text="Date Of Birth").grid(row=4, column=0)  
    patientDOB = StringVar()
    patientDOBEntry = Entry(tkWindow, textvariable=patientDOB,).grid(row=4, column=1)

    ageLabel = Label(tkWindow, text="Patient age").grid(row=5, column=0)
    age = StringVar()
    ageEntry = Entry(tkWindow, textvariable=age).grid(row=5, column=1)

    StatusLabel = Label(tkWindow, text="Patient Status").grid(row=6, column=0)
    Status = StringVar()
    StatusEntry = OptionMenu(tkWindow,Status,*statusList).grid(row=6, column=1)

    TreatmentLabel= Label(tkWindow, text="Treatment").grid(row=7, column=0)
    Treatment=StringVar(tkWindow)
    TreatmentEntry=OptionMenu(tkWindow, Treatment, *records).grid(row=7, column=1)

    dtOfApptLabel= Label(tkWindow, text="Date of Appointment").grid(row=8, column=0)
    dtOfAppt=StringVar(tkWindow)
    dtOfApptEntry=DateEntry(tkWindow,selectmode='day').grid(row=8, column=1,padx=15)


  
    loginButton = tk.Button(tkWindow, text="Register", command=partial(validateLogin,Name,Mobile,Address,Gender,patientDOB,age,Status,Treatment,dtOfAppt)).grid(row=9, column=0)

    backButton=Button(tkWindow, text="BACK", command=tkWindow.destroy).grid(row=9, column=2)

    tkWindow.mainloop()


registraionForm()
