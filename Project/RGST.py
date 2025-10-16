import re
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import ttk
from tkinter import messagebox
from hashlib import sha256
import LIB
from PIL import Image, ImageDraw, ImageTk

connection = pymysql.connect(host="localhost", user="root", passwd="", database="library_mnagemet")
mycursor = connection.cursor()

class Registration:
    def __init__(self, window):
        self.window = window
        self.window.title("Library Management System - Registration")
        self.window.geometry("1530x790+0+0")

        lbltit = Label(self.window, text="LIBRARY MANAGEMENT SYSTEM", bg="white", fg="green", relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltit.pack(side=TOP, fill=X)

        frame = Frame(self.window, relief=RIDGE, padx=20, bg="white")
        frame.place(x=0, y=130, width=1530, height=700)

        lblmember = Label(frame, bg="white", text="Member Type", font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblmember.grid(row=0, column=0, sticky=W)

        self.commember = ttk.Combobox(frame, font=("times new roman", 15, "bold"), width=27, state="readonly")
        self.commember["values"] = ("ADMIN", "STAFF", "STUDENT", "LECTURER")
        self.commember.grid(row=0, column=1)
        self.commember.bind("<<ComboboxSelected>>", self.update_registration_form)

        self.lblFirstName = Label(frame, font=("times new roman", 15, "bold"), text="First Name", padx=2, pady=6, bg="white")
        self.txtFirstName = Entry(frame, font=("times new roman", 15, "bold"), width=29)

        self.lblLstName = Label(frame, font=("times new roman", 15, "bold"), text="Last Name", padx=2, pady=6, bg="white")
        self.txtLstName = Entry(frame, font=("times new roman", 15, "bold"), width=29)

        self.lblUsername = Label(frame, font=("times new roman", 15, "bold"), text="Username", padx=2, pady=6, bg="white")
        self.txtUsername = Entry(frame, font=("times new roman", 15, "bold"), width=29)

        self.lblPassword = Label(frame, font=("times new roman", 15, "bold"), text="Password", padx=2, pady=6, bg="white")
        self.txtPassword = Entry(frame, font=("times new roman", 15, "bold"), width=29, show="*")

        self.lblConfirmPassword = Label(frame, font=("times new roman", 15, "bold"), text="Confirm Password", padx=2, pady=6, bg="white")
        self.txtConfirmPassword = Entry(frame, font=("times new roman", 15, "bold"), width=29, show="*")

        self.ld_no = Label(frame, bg="white", text="ID NO", font=("times new roman", 15, "bold"), padx=2, pady=6)
        self.txtId_no = Entry(frame, font=("times new roman", 15, "bold"), width=29)

        self.lbldptName = Label(frame, font=("times new roman", 15, "bold"), text="Department", padx=2, pady=6, bg="white")
        self.dpt = ttk.Combobox(frame, font=("times new roman", 15, "bold"), width=27, state="readonly")

        self.lblIntake = Label(frame, bg="white", text="Intake", font=("times new roman", 15, "bold"), padx=2, pady=6)
        self.txtIntake = Entry(frame, font=("times new roman", 15, "bold"), width=29)

        self.lblSec = Label(frame, bg="white", text="Section", font=("times new roman", 15, "bold"), padx=2, pady=6)
        self.txtSec = Entry(frame, font=("times new roman", 15, "bold"), width=29)

        Framebutton = Frame(self.window, relief=RIDGE, padx=20, bg="white")
        Framebutton.place(x=0, y=700, width=1530, height=70)

        btnRegister = Button(Framebutton, text="Register", font=("arial", 12, "bold"), width=25, bg="light coral", command=self.register_member)
        btnRegister.grid(row=0, column=0)

        btnExit = Button(Framebutton, text="Back", font=("arial", 12, "bold"), width=25, bg="light coral", command=self.go_back)
        btnExit.grid(row=0, column=1)
        
        self.add_side_image(frame, x=550, y=20)

    def update_registration_form(self, event):
        membertype = self.commember.get()
        
        self.reset_registration_form()

        if membertype == "ADMIN":
            self.lblFirstName.grid(row=1, column=0, sticky=W)
            self.txtFirstName.grid(row=1, column=1)
            self.lblLstName.grid(row=2, column=0, sticky=W)
            self.txtLstName.grid(row=2, column=1)
            self.lblUsername.grid(row=3, column=0, sticky=W)
            self.txtUsername.grid(row=3, column=1)
            self.lblPassword.grid(row=4, column=0, sticky=W)
            self.txtPassword.grid(row=4, column=1)
            self.lblConfirmPassword.grid(row=5, column=0, sticky=W)
            self.txtConfirmPassword.grid(row=5, column=1)

        elif membertype == "STAFF":
            self.lbldptName.grid(row=1, column=0, sticky=W)
            self.dpt.grid(row=1, column=1)
            self.lblFirstName.grid(row=2, column=0, sticky=W)
            self.txtFirstName.grid(row=2, column=1)
            self.lblLstName.grid(row=3, column=0, sticky=W)
            self.txtLstName.grid(row=3, column=1)
            self.lblUsername.grid(row=4, column=0, sticky=W)
            self.txtUsername.grid(row=4, column=1)
            self.lblPassword.grid(row=5, column=0, sticky=W)
            self.txtPassword.grid(row=5, column=1)
            self.lblConfirmPassword.grid(row=6, column=0, sticky=W)
            self.txtConfirmPassword.grid(row=6, column=1)

        elif membertype == "LECTURER":
            self.lbldptName.grid(row=1, column=0, sticky=W)
            self.dpt.grid(row=1, column=1)
            self.lblFirstName.grid(row=2, column=0, sticky=W)
            self.txtFirstName.grid(row=2, column=1)
            self.lblLstName.grid(row=3, column=0, sticky=W)
            self.txtLstName.grid(row=3, column=1)
            self.lblUsername.grid(row=4, column=0, sticky=W)
            self.txtUsername.grid(row=4, column=1)
            self.lblPassword.grid(row=5, column=0, sticky=W)
            self.txtPassword.grid(row=5, column=1)
            self.lblConfirmPassword.grid(row=6, column=0, sticky=W)
            self.txtConfirmPassword.grid(row=6, column=1)

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
            self.lblUsername.grid(row=7, column=0, sticky=W)
            self.txtUsername.grid(row=7, column=1)
            self.lblPassword.grid(row=8, column=0, sticky=W)
            self.txtPassword.grid(row=8, column=1)
            self.lblConfirmPassword.grid(row=9, column=0, sticky=W)
            self.txtConfirmPassword.grid(row=9, column=1)

        if membertype == "ADMIN":
            self.dpt["values"] = ("Management", "IT Support", "HR")
        elif membertype == "STAFF":
            self.dpt["values"] = ("Library", "Maintenance", "Security")
        elif membertype == "LECTURER":
            self.dpt["values"] = ("CSE", "EEE", "ME")
        elif membertype == "STUDENT":
            self.dpt["values"] = ("CSE", "EEE", "ME", "BBA")
            
    def add_side_image(self, parent, x, y):
        """Add an image to the right side of the buttons."""
        try:
            img = Image.open("download.jpeg").resize((800, 400))  
            img = ImageTk.PhotoImage(img)
            side_image_label = Label(parent, image=img, bg="white")
            side_image_label.image = img  
            side_image_label.place(x=x, y=y)  
        except FileNotFoundError:
            print("Image file not found. Please check the path.")

    def reset_registration_form(self):
        self.lblFirstName.grid_forget()
        self.txtFirstName.grid_forget()
        self.lblLstName.grid_forget()
        self.txtLstName.grid_forget()
        self.lblUsername.grid_forget()
        self.txtUsername.grid_forget()
        self.lblPassword.grid_forget()
        self.txtPassword.grid_forget()
        self.lblConfirmPassword.grid_forget()
        self.txtConfirmPassword.grid_forget()
        self.ld_no.grid_forget()
        self.txtId_no.grid_forget()
        self.lbldptName.grid_forget()
        self.dpt.grid_forget()
        self.lblIntake.grid_forget()
        self.txtIntake.grid_forget()
        self.lblSec.grid_forget()
        self.txtSec.grid_forget()

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

        password_pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{6,}$'
        if not re.match(password_pattern, password):
            messagebox.showerror("Error", "Password must be at least 6 characters long, contain an uppercase letter, a digit, and a special character.")
            return


        hashed_password = sha256(password.encode()).hexdigest()
        hashed_confirm_password = sha256(confirm_password.encode()).hexdigest()

        if hashed_password != hashed_confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        if member_type == "STUDENT":
            
            if not id.isdigit():
                messagebox.showerror("Error", "ID No must be an integer.")
                return

        
            if not intke.isdigit():
                messagebox.showerror("Error", "Intake must be an integer.")
                return

    
            if not section.isdigit():
                messagebox.showerror("Error", "Section must be an integer.")
                return

    
        elif member_type in ["ADMIN", "STAFF", "LECTURER"]:
            if not fnme or not lname or not username or not password or not confirm_password:
                messagebox.showerror("Error", "Please fill all required fields")
                return
        else:
            messagebox.showerror("Error", "Invalid member type selected")
            return

    
        try:
            query = "SELECT * FROM userinfo WHERE username = %s"
            mycursor.execute(query, (username,))
            existing_user = mycursor.fetchone()
            if existing_user:
                messagebox.showerror("Error", "Username already exists. Please choose a different username.")
                return
        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", f"An error occurred while checking the username: {e}")
            return


        try:
            if member_type == "STUDENT":
                sqlformula = "INSERT INTO userinfo (membertype, dpt, nam, id, intake, sec, username, pass) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                student1 = (member, dpt, f"{fnme} {lname}", id, intke, section, username, hashed_password)
                mycursor.execute(sqlformula, student1)

            elif member_type == "ADMIN":
                sqlformula1 = "INSERT INTO userinfo (membertype, nam, username, pass) VALUES (%s, %s, %s, %s)"
                admin1 = (member, f"{fnme} {lname}", username, hashed_password)
                mycursor.execute(sqlformula1, admin1)

            elif member_type == "STAFF":
                sqlformula2 = "INSERT INTO userinfo (membertype, nam, dpt, id, username, pass) VALUES (%s, %s, %s, %s, %s, %s)"
                staff = (member, f"{fnme} {lname}", dpt, id, username, hashed_password)
                mycursor.execute(sqlformula2, staff)

            elif member_type == "LECTURER":
                sqlformula3 = "INSERT INTO userinfo (membertype, nam, dpt, username, pass) VALUES (%s, %s, %s, %s, %s)"
                lec = (member, f"{fnme} {lname}", dpt, username, hashed_password)
                mycursor.execute(sqlformula3, lec)

            connection.commit()
            messagebox.showinfo("Success", "Registration Successful")
            self.open_new_window()

        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")
            connection.rollback()

    def go_back(self):
        self.window.destroy() 
        main_window = Tk()  
        LIB.InitialMenu(main_window) 
        main_window.mainloop()


    def open_new_window(self):
        pass


if __name__ == "__main__":
    root = Tk()
    app = Registration(root)
    root.mainloop()
