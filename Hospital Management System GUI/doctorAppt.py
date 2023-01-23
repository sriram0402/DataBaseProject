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

def doctorAppt(doctorId):
    
    print(doctorId)


    tkWindow = Tk()  
    tkWindow.geometry('700x400')  
    tkWindow.title(' Appointments')
    cur = db.cursor()

    tree = ttk.Treeview(tkWindow, column=("patientID","Name", "Gender","DOB","Status"), show='headings', height=4)
    tree.column("# 1", anchor=CENTER ,width=50)
    tree.heading("# 1", text="PatientID")
    tree.column("# 2", anchor=CENTER,width=75)
    tree.heading("# 2", text="Name")
    tree.column("# 3", anchor=CENTER,width=75)
    tree.heading("# 3", text="Gender")
    tree.column("# 4", anchor=CENTER,width=50)
    tree.heading("# 4", text="DOB")
    tree.column("# 5", anchor=CENTER,width=75)
    tree.heading("# 5", text="Status")

    tree.pack()


    
    cursor = db.cursor()
    sql=("SELECT PatientId,patientName,Gender,patientDOB,status FROM hmsdb.patients  where Doctor_DoctorID=%s ")
    val=(doctorId)
    cursor.execute(sql,val)
    data=cursor.fetchall()
    
    status=str(data[0][4])+'s'
    """
    sqldtOfAppt=("select DateOfAppointment from %s where DoctorID=%s")
    valdtOfAppt=(status,doctorId)
    cursor.execute(sqldtOfAppt,valdtOfAppt)
    dataAppt=cursor.fetchall()

    print(dataAppt)
    """
    for i in data:
        tree.insert('', 'end', text="1", values=(i[0],i[1],i[2],i[3],i[4]))
    
    tkWindow.mainloop()

    logOutButton=Button(tkWindow, text="LogOut", command=tkWindow.destroy).grid(row=4, column=2)

    """
    except:
        messagebox.showerror("showerror","error occured")
    """

