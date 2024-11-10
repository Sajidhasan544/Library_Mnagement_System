from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
import LIB

connection = pymysql.connect(host="localhost", user="root", passwd="", database="library_mnagemet")
mycursor = connection.cursor()
class Registration:
    def __init__(self, window):
        self.window = window
        self.window.title("Library Management System - Registration")
        self.window.geometry("1530x790+0+0")

        lbltit = Label(self.window, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltit.pack(side=TOP, fill=X)

        frame = Frame(self.window, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)

        lblmember = Label(frame, bg="powder blue", text="Member Type", font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblmember.grid(row=0, column=0, sticky=W)

        self.commember = ttk.Combobox(frame, font=("times new roman", 15, "bold"), width=27, state="readonly")
        self.commember["values"] = ("ADMIN", "STAFF", "STUDENT", "LECTURER")
        self.commember.grid(row=0, column=1)
        self.commember.bind("<<ComboboxSelected>>", self.update_registration_form)

        # Existing form fields for registration
        self.lbldptName = Label(frame, font=("times new roman", 15, "bold"), text="Department", padx=2, pady=6, bg="powder blue")
        self.dpt = ttk.Combobox(frame, font=("times new roman", 15, "bold"), width=27, state="readonly")

        self.lblFirstName = Label(frame, font=("times new roman", 15, "bold"), text="First Name", padx=2, pady=6, bg="powder blue")
        self.txtFirstName = Entry(frame, font=("times new roman", 15, "bold"), width=29)

        self.lblLstName = Label(frame, font=("times new roman", 15, "bold"), text="Last Name", padx=2, pady=6, bg="powder blue")
        self.txtLstName = Entry(frame, font=("times new roman", 15, "bold"), width=29)

        self.ld_no = Label(frame, bg="powder blue", text="ID NO", font=("times new roman", 15, "bold"), padx=2, pady=6)
        self.txtId_no = Entry(frame, font=("times new roman", 15, "bold"), width=29)

        self.lblIntake = Label(frame, bg="powder blue", text="Intake", font=("times new roman", 15, "bold"), padx=2, pady=6)
        self.txtIntake = Entry(frame, font=("times new roman", 15, "bold"), width=29)

        self.lblSec = Label(frame, bg="powder blue", text="Section", font=("times new roman", 15, "bold"), padx=2, pady=6)
        self.txtSec = Entry(frame, font=("times new roman", 15, "bold"), width=29)

        lblUsername = Label(frame, font=("times new roman", 15, "bold"), text="Username", padx=2, pady=6, bg="powder blue")
        lblUsername.grid(row=0, column=2, sticky=W)
        self.txtUsername = Entry(frame, font=("times new roman", 15, "bold"), width=29)
        self.txtUsername.grid(row=0, column=3)

        lblPassword = Label(frame, font=("times new roman", 15, "bold"), text="Password", padx=2, pady=6, bg="powder blue")
        lblPassword.grid(row=1, column=2, sticky=W)
        self.txtPassword = Entry(frame, font=("times new roman", 15, "bold"), width=29, show="*")
        self.txtPassword.grid(row=1, column=3)

        lblConfirmPassword = Label(frame, font=("times new roman", 15, "bold"), text="Confirm Password", padx=2, pady=6, bg="powder blue")
        lblConfirmPassword.grid(row=2, column=2, sticky=W)
        self.txtConfirmPassword = Entry(frame, font=("times new roman", 15, "bold"), width=29, show="*")
        self.txtConfirmPassword.grid(row=2, column=3)

        Framebutton = Frame(self.window, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x=0, y=530, width=1530, height=70)

        btnRegister = Button(Framebutton, text="Register", font=("arial", 12, "bold"), width=25, bg="light coral", command=self.register_member)
        btnRegister.grid(row=0, column=0)

        btnExit = Button(Framebutton, text="Back", font=("arial", 12, "bold"), width=25, bg="light coral", command=self.go_back)
        btnExit.grid(row=0, column=1)

    def update_registration_form(self, event):
        membertype = self.commember.get()

        self.reset_registration_form()

        if membertype == "ADMIN":
            self.lblFirstName.grid(row=1, column=0, sticky=W)
            self.txtFirstName.grid(row=1, column=1)
            self.lblLstName.grid(row=2, column=0, sticky=W)
            self.txtLstName.grid(row=2, column=1)

        elif membertype == "STAFF":
            self.lbldptName.grid(row=1, column=0, sticky=W)
            self.dpt.grid(row=1, column=1)
            self.lblFirstName.grid(row=2, column=0, sticky=W)
            self.txtFirstName.grid(row=2, column=1)
            self.lblLstName.grid(row=3, column=0, sticky=W)
            self.txtLstName.grid(row=3, column=1)
            self.ld_no.grid(row=4, column=0, sticky=W)
            self.txtId_no.grid(row=4, column=1)

        elif membertype == "LECTURER":
            self.lbldptName.grid(row=1, column=0, sticky=W)
            self.dpt.grid(row=1, column=1)
            self.lblFirstName.grid(row=2, column=0, sticky=W)
            self.txtFirstName.grid(row=2, column=1)
            self.lblLstName.grid(row=3, column=0, sticky=W)
            self.txtLstName.grid(row=3, column=1)

        elif membertype == "STUDENT":
            self.lbldptName.grid(row=1, column=0, sticky=W)
            self.dpt.grid(row=1, column=1)
            self.lblFirstName.grid(row=2, column=0, sticky=W)
            self.txtFirstName.grid(row=2, column=1)
            self.lblLstName.grid(row=3, column=0, sticky=W)
            self.txtLstName.grid(row=3, column=1)
            self.ld_no.grid(row=4, column=0, sticky=W)
            self.txtId_no.grid(row=4, column=1)
            self.lblIntake.grid(row=5, column=0, sticky=W)
            self.txtIntake.grid(row=5, column=1)
            self.lblSec.grid(row=6, column=0, sticky=W)
            self.txtSec.grid(row=6, column=1)

        if membertype == "ADMIN":
            self.dpt["values"] = ("Management", "IT Support", "HR")
        elif membertype == "STAFF":
            self.dpt["values"] = ("Library", "Maintenance", "Security")
        elif membertype == "STUDENT":
            self.dpt["values"] = ("CSE", "EEE", "BBA", "LAW", "English")
        else:
            self.dpt["values"] = ("Math", "English", "CSE", "EEE", "Accounting", "LAW", "Economics")
        self.dpt.set('')

    def reset_registration_form(self):
        self.lbldptName.grid_remove()
        self.dpt.grid_remove()
        self.lblFirstName.grid_remove()
        self.txtFirstName.grid_remove()
        self.lblLstName.grid_remove()
        self.txtLstName.grid_remove()
        self.ld_no.grid_remove()
        self.txtId_no.grid_remove()
        self.lblIntake.grid_remove()
        self.txtIntake.grid_remove()
        self.lblSec.grid_remove()
        self.txtSec.grid_remove()

    def register_member(self):
        member = self.commember.get()
        fnme = self.txtFirstName.get()
        lname = self.txtLstName.get()
        id = self.txtId_no.get()
        member_type = self.commember.get()
        dpt = self.dpt.get()
        intke = self.txtIntake.get()
        section = self.txtSec.get()
        username = self.txtUsername.get()
        password = self.txtPassword.get()
        confirm_password = self.txtConfirmPassword.get()

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        try:
            if member_type == "STUDENT":
                sqlformula = "INSERT INTO userinfo (membertype, dpt, nam, id, intake, sec, username, pass) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                student1 = (member, dpt, f"{fnme} {lname}", id, intke, section, username, password)
                mycursor.execute(sqlformula, student1)



            elif member_type == "ADMIN":
                sqlformula1 = "INSERT INTO userinfo (membertype, nam, username, pass) VALUES (%s, %s, %s, %s)"
                admin1 = (member, f"{fnme} {lname}", username, password)
                mycursor.execute(sqlformula1, admin1)

            elif member_type == "STAFF":
                sqlformula2 = "INSERT INTO userinfo (membertype, nam, dept, id, username, pass) VALUES (%s, %s, %s, %s, %s, %s)"
                staff = (member, f"{fnme} {lname}", dpt, id, username, password)
                mycursor.execute(sqlformula2, staff)

            elif member_type == "LECTURER":
                sqlformula3 = "INSERT INTO userinfo (membertype, nam, dpt, username, pass) VALUES (%s, %s, %s, %s, %s)"
                lec = (member, f"{fnme} {lname}", dpt, username, password)
                mycursor.execute(sqlformula3, lec)

            connection.commit()
            messagebox.showinfo("Success", "Registration Successful")
            self.open_new_window()
        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")
            connection.rollback()

    def open_new_window(self):
        self.window.destroy()
        new_window = Tk()
        LIB.InitialMenu(new_window)
        new_window.mainloop()

    def go_back(self):
        self.window.destroy()
        main_window = Tk()
        LIB.InitialMenu(main_window)
        main_window.mainloop()

