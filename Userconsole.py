from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
import LIB
import BorrowClass
import Userpanel

class LibraryLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Library User Login")
        self.root.geometry("1530x790+0+0")
        self.root.config(bg="powder blue")

        lbltit = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="green", bd=20, relief="ridge", font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltit.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief="ridge", padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)
        
        lblmember = Label(frame, bg="powder blue", text="Member Type", font=("times new roman", 20, "bold"))
        lblmember.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        
        self.commember = ttk.Combobox(frame, font=("times new roman", 20, "bold"), width=30, state="readonly")
        self.commember["values"] = ("ADMIN", "STAFF", "STUDENT", "LECTURER")
        self.commember.grid(row=0, column=1 ,padx=10, pady=10)

        self.username_label = Label(frame, text="Username", bg="powder blue", font=("times new roman", 20, "bold"))
        self.username_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.username_entry = Entry(frame, font=("times new roman", 20, "bold"), width=30)
        self.username_entry.grid(row=1, column=1, padx=10, pady=10)

        self.password_label = Label(frame, text="Password", bg="powder blue", font=("times new roman", 20, "bold"))
        self.password_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.password_entry = Entry(frame, show="*", font=("times new roman", 20, "bold"), width=30)
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)

        Framebutton = Frame(self.root, bd=12, relief="ridge", padx=20, bg="powder blue")
        Framebutton.place(x=0, y=530, width=1530, height=70)

        self.login_button = Button(Framebutton, text="Login", font=("arial", 12, "bold"), width=25, bg="light green", command=self.login)
        self.login_button.grid(row=0, column=0)

        self.back_button = Button(Framebutton, text="Back", font=("arial", 12, "bold"), width=25, bg="light green", command=self.back)
        self.back_button.grid(row=0, column=1)

        self.connection = pymysql.connect(host="localhost", user="root", passwd="", database="library_mnagemet")
        self.mycursor = self.connection.cursor()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        sql = "SELECT * FROM userinfo WHERE username = %s AND pass = %s"
        self.mycursor.execute(sql, (username, password))
        result = self.mycursor.fetchone()

        if result:
            self.root.destroy()
            admin_window = Tk()
            Userpanel.UserPanel(admin_window)
            admin_window.mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def back(self):
        self.root.destroy()
        main_window = Tk()
        LIB.InitialMenu(main_window)
        main_window.mainloop()

    def __del__(self):
        self.mycursor.close()
        self.connection.close()
