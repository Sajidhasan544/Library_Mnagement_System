from tkinter import *
from tkinter import ttk

class InitialMenu:
    def __init__(self, window):
        self.window = window
        self.window.title("Library Management System")
        self.window.geometry("1530x750+0+0")

        lbltit = Label(self.window, text="Library Management System", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltit.pack(side=TOP, fill=X)

        frame = Frame(self.window, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)

        btnBorrow = Button(frame, text="Borrow a Book", font=("times new roman", 20, "bold"), bg="light blue", command=self.open_borrow_window)
        btnBorrow.place(x=100, y=150, width=400, height=100)

        btnReturn = Button(frame, text="Return a Book", font=("times new roman", 20, "bold"), bg="light green", command=self.open_return_window)
        btnReturn.place(x=800, y=150, width=400, height=100)

        btnRegister = Button(frame, text="First Time Registration", font=("times new roman", 20, "bold"), bg="light coral", command=self.open_registration_window)
        btnRegister.place(x=450, y=300, width=630, height=100)

    def open_borrow_window(self):
        self.window.destroy()
        borrow_window = Tk()
        Libs(borrow_window)
        borrow_window.mainloop()

    def open_return_window(self):
        self.window.destroy()
        return_window = Tk()
        ReturnBook(return_window)
        return_window.mainloop()

    def open_registration_window(self):
        self.window.destroy()
        registration_window = Tk()
        Registration(registration_window)
        registration_window.mainloop()

class Libs:
    def __init__(self, window):
        self.window = window
        self.window.title("Library Management System - Borrow a Book")
        self.window.geometry("1530x750+0+0")

        lbltit = Label(self.window, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltit.pack(side=TOP, fill=X)

        frame = Frame(self.window, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)

        DataFrameLeft = LabelFrame(frame, text="MEMBERSHIP INFORMATION", bg="powder blue", bd=12, relief=RIDGE, font=("times new roman", 20, "bold"), padx=2, pady=6)
        DataFrameLeft.place(x=0, y=5, width=900, height=350)
        

        lblmember = Label(DataFrameLeft, bg="powder blue", text="Member Type", font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblmember.grid(row=0, column=0, sticky=W)

        self.commember = ttk.Combobox(DataFrameLeft, font=("times new roman", 15, "bold"), width=27, state="readonly")
        self.commember["values"] = ("ADMIN", "STUFF", "STUDENT", "LECTURER")
        self.commember.grid(row=0, column=1)
        self.commember.bind("<<ComboboxSelected>>", self.update_dpt_op)

        self.lbldptName = Label(DataFrameLeft, font=("times new roman", 15, "bold"), text="Dpt.", padx=2, pady=6, bg="powder blue")
        self.dpt = ttk.Combobox(DataFrameLeft, font=("times new roman", 15, "bold"), width=27, state="readonly")

        self.lblFirstName = Label(DataFrameLeft, font=("times new roman", 15, "bold"), text="FirstName", padx=2, pady=6, bg="powder blue")
        self.txtFirstName = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)

        self.lblLstName = Label(DataFrameLeft, font=("times new roman", 15, "bold"), text="LastName", padx=2, pady=6, bg="powder blue")
        #self.lblLstName.grid(row=3, column=0, sticky=W)
        self.txtLstName = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)
        #self.txtLstName.grid(row=3, column=1)

        self.ld_no = Label(DataFrameLeft, bg="powder blue", text="ID NO", font=("times new roman", 15, "bold"), padx=2, pady=6)
        #self.ld_no.grid(row=4, column=0, sticky=W)
        self.txtId_no = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)
        #self.txtId_no.grid(row=4, column=1)

        self.lblIntake = Label(DataFrameLeft, bg="powder blue", text="Intake", font=("times new roman", 15, "bold"), padx=2, pady=6)
        #self.lblIntake.grid(row=5, column=0, sticky=W)
        self.txtIntake = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)
        #self.txtIntake.grid(row=5, column=1)

        self.lblSec = Label(DataFrameLeft, bg="powder blue", text="Section", font=("times new roman", 15, "bold"), padx=2, pady=6)
        #self.lblSec.grid(row=6, column=0, sticky=W)
        self.txtSec = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)
        #self.txtSec.grid(row=6, column=1)

        Bookid = Label(DataFrameLeft, bg="powder blue", text="Book ID", font=("times new roman", 15, "bold"), padx=2, pady=6)
        Bookid.grid(row=0, column=2, sticky=W)
        self.txtBookid = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)
        self.txtBookid.grid(row=0, column=3)

        Booktitle = Label(DataFrameLeft, bg="powder blue", text="Book Title", font=("times new roman", 15, "bold"), padx=2, pady=6)
        Booktitle.grid(row=1, column=2, sticky=W)
        self.txtBooktitle = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)
        self.txtBooktitle.grid(row=1, column=3)

        Authorname = Label(DataFrameLeft, bg="powder blue", text="Author Name", font=("times new roman", 15, "bold"), padx=2, pady=6)
        Authorname.grid(row=2, column=2, sticky=W)
        self.txtAuthorname = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)
        self.txtAuthorname.grid(row=2, column=3)

        Datebor = Label(DataFrameLeft, bg="powder blue", text="Date Borrowed", font=("times new roman", 15, "bold"), padx=2, pady=6)
        Datebor.grid(row=3, column=2, sticky=W)
        self.txtDatebor = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)
        self.txtDatebor.grid(row=3, column=3)

        Datedu = Label(DataFrameLeft, bg="powder blue", text="Date Due", font=("times new roman", 15, "bold"), padx=2, pady=6)
        Datedu.grid(row=4, column=2, sticky=W)
        self.txtDatedu = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)
        self.txtDatedu.grid(row=4, column=3)

        Overdu = Label(DataFrameLeft, bg="powder blue", text="Date Over Due", font=("times new roman", 15, "bold"), padx=2, pady=6)
        Overdu.grid(row=5, column=2, sticky=W)
        self.txtOverdu = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)
        self.txtOverdu.grid(row=5, column=3)

        Actp = Label(DataFrameLeft, bg="powder blue", text="Actual Price", font=("times new roman", 15, "bold"), padx=2, pady=6)
        Actp.grid(row=6, column=2, sticky=W)
        self.txtActp = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)
        self.txtActp.grid(row=6, column=3)



        DataFrameRight = LabelFrame(frame, text="BOOK DETAILS", bg="powder blue", bd=12, relief=RIDGE, font=("times new roman", 20, "bold"), padx=2, pady=6)
        DataFrameRight.place(x=910, y=5, width=550, height=350)
        
        
        
        
        self.txtbox = Text(DataFrameRight, font=("arial",12,"bold"),width=32,height=14,padx=2,pady=6)
        self.txtbox.grid(row=0,column=2)
        
        listscrolbar = Scrollbar(DataFrameRight)
        listscrolbar.grid(row=0,column=1,padx=4,sticky="ns")
        
        Listbooks = ['Head first Book','Learn Python','Python Programming','Python Book',
                   'C++ Book','Maching learning Engineering','AI Engineering',
                   'Game Development','SW Development']

        listbox = Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=14,)
        listbox.grid(row=0,column=0,padx=4)
        listscrolbar.config(command=listbox.yview)
        
        for item in Listbooks:
            listbox.insert(END,item)
        
        
        framebutton = Frame(self.window, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        framebutton.place(x=0, y=530, width=1530, height=70)

        btnBack = Button(framebutton, text="Back", font=("times new roman", 20, "bold"), bg="light coral", command=self.go_back)
        btnBack.pack(side=LEFT, padx=10)


    def update_dpt_op(self, event):
        membertype = self.commember.get()

        # Reset grid positions and show all fields by default
        self.reset_grid_positions()
        #self.show_widget(self.lbldptName, self.dpt, self.lblIntake, self.txtIntake, self.lblSec, self.txtSec, self.ld_no, self.txtId_no)

        if membertype == "Admin":
            # Show only FirstName and LastName
            self.hide_widget(self.lbldptName, self.dpt, self.lblIntake, self.txtIntake, self.lblSec, self.txtSec, self.ld_no)
            self.lblFirstName.grid(row=1, column=0, sticky=W)
            self.txtFirstName.grid(row=1, column=1)
            self.lblLstName.grid(row=2, column=0, sticky=W)
            self.txtLstName.grid(row=2, column=1)
            
        elif membertype == "Staff":
            # Hide department, intake, and section fields, show ID NO
            self.hide_widget(self.lblIntake, self.txtIntake, self.lblSec, self.txtSec)
            self.lbldptName.grid(row=1,column=0)
            self.dpt.grid(row=1,column=1)
            self.lblFirstName.grid(row=2, column=0, sticky=W)
            self.txtFirstName.grid(row=2, column=1)
            self.lblLstName.grid(row=3, column=0, sticky=W)
            self.txtLstName.grid(row=3, column=1)
            self.ld_no.grid(row=4, column=0, sticky=W)
            self.txtId_no.grid(row=4, column=1)

        elif membertype == "Lecturer":
            # Hide ID NO, intake, and section fields, show FirstName and LastName
            self.hide_widget(self.ld_no, self.txtId_no, self.lblIntake, self.txtIntake, self.lblSec, self.txtSec)
            self.lbldptName.grid(row=1,column= 0)
            self.dpt.grid(row=1,column=1)
            self.lblFirstName.grid(row=2, column=0, sticky=W)
            self.txtFirstName.grid(row=2, column=1)
            self.lblLstName.grid(row=3, column=0, sticky=W)
            self.txtLstName.grid(row=3, column=1)

        elif membertype == "Student":
            # Show all fields
            self.show_widget(self.lbldptName, self.dpt, self.lblIntake, self.txtIntake, self.lblSec, self.txtSec, self.ld_no, self.txtId_no,self.dpt,self.lbldptName)
            self.lbldptName.grid(row=1,column=0)
            self.dpt.grid(row=1,column=1)
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

        # Set department options based on member type
        if membertype == "Admin":
            self.dpt["values"] = ("Management", "IT Support", "HR")
        elif membertype == "Staff":
            self.dpt["values"] = ("Library", "Maintenance", "Security")
        elif membertype == "Student":
            self.dpt["values"] = ("CSE", "EEE", "BBA", "LAW", "English")
        else:
            self.dpt["values"] = ("Math", "English", "CSE", "EEE", "Accounting", "LAW", "Economics")
        self.dpt.set('')
        

    def reset_grid_positions(self):
        self.hide_widget(self.lbldptName,self.dpt,self.lblFirstName,self.txtFirstName,self.lblLstName,self.txtLstName,self.ld_no,self.txtId_no,self.lblIntake,self.txtIntake,self.lblSec,self.txtSec)
        
        
    def show_widget(self, *widgets):
        for widget in widgets:
            widget.grid()

    def hide_widget(self, *widgets):
        for widget in widgets:
            widget.grid_forget()

    def go_back(self):
        self.window.destroy()
        main_window = Tk()
        InitialMenu(main_window)
        main_window.mainloop()


    



class ReturnBook:
    def __init__(self, window):
        self.window = window
        self.window.title("Library Management System - Return a Book")
        self.window.geometry("1530x750+0+0")
        
        lbltit = Label(self.window, text="RETURN A BOOK", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltit.pack(side=TOP, fill=X)
        
        frame = Frame(self.window, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)
        
        DataFrameLeft = LabelFrame(frame, text="RETURN INFORMATION", bg="powder blue", bd=12, relief=RIDGE, font=("times new roman", 20, "bold"), padx=2, pady=6)
        DataFrameLeft.place(x=0, y=5, width=900, height=350)
        
        lblBookId = Label(DataFrameLeft, text="Book ID", font=("times new roman", 15, "bold"), padx=2, pady=6, bg="powder blue")
        lblBookId.grid(row=0, column=0, sticky=W)
        self.txtBookId = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)
        self.txtBookId.grid(row=0, column=1)
        
        lblReturnDate = Label(DataFrameLeft, text="Return Date", font=("times new roman", 15, "bold"), padx=2, pady=6, bg="powder blue")
        lblReturnDate.grid(row=1, column=0, sticky=W)
        self.txtReturnDate = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)
        self.txtReturnDate.grid(row=1, column=1)
        
        
        btnReturn = Button(frame, text="Return Book", font=("times new roman", 20, "bold"), bg="light green", command=self.return_book)
        btnReturn.place(x=20, y=320)

        btnBack = Button(frame, text="Back", font=("times new roman", 20, "bold"), bg="light coral", command=self.go_back)
        btnBack.place(x=1400, y=320)

    def return_book(self):
        book_id = self.txtBookId.get()
        return_date = self.txtReturnDate.get()
        # Add your logic to handle book return here.
        print(f"Book ID: {book_id}")
        print(f"Return Date: {return_date}")
        # Reset fields or show confirmation message here
        self.txtBookId.delete(0, END)
        self.txtReturnDate.delete(0, END)

    def go_back(self):
        self.window.destroy()
        main_window = Tk()
        InitialMenu(main_window)
        main_window.mainloop()

class Registration:
    def __init__(self, window):
        self.window = window
        self.window.title("Library Management System - Registration")
        self.window.geometry("1530x750+0+0")
        
        lbltit = Label(self.window, text="FIRST TIME REGISTRATION", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltit.pack(side=TOP, fill=X)
        
        frame = Frame(self.window, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)
        
        DataFrameLeft = LabelFrame(frame, text="REGISTRATION INFORMATION", bg="powder blue", bd=12, relief=RIDGE, font=("times new roman", 20, "bold"), padx=2, pady=6)
        DataFrameLeft.place(x=0, y=5, width=900, height=350)
        
        lblFirstName = Label(DataFrameLeft, text="First Name", font=("times new roman", 15, "bold"), padx=2, pady=6, bg="powder blue")
        lblFirstName.grid(row=0, column=0, sticky=W)
        self.txtFirstName = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)
        self.txtFirstName.grid(row=0, column=1)
        
        lblLastName = Label(DataFrameLeft, text="Last Name", font=("times new roman", 15, "bold"), padx=2, pady=6, bg="powder blue")
        lblLastName.grid(row=1, column=0, sticky=W)
        self.txtLastName = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)
        self.txtLastName.grid(row=1, column=1)
        
        lblEmail = Label(DataFrameLeft, text="Email", font=("times new roman", 15, "bold"), padx=2, pady=6, bg="powder blue")
        lblEmail.grid(row=2, column=0, sticky=W)
        self.txtEmail = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)
        self.txtEmail.grid(row=2, column=1)
        
        lblPhone = Label(DataFrameLeft, text="Phone", font=("times new roman", 15, "bold"), padx=2, pady=6, bg="powder blue")
        lblPhone.grid(row=3, column=0, sticky=W)
        self.txtPhone = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)
        self.txtPhone.grid(row=3, column=1)
        
        lblAddress = Label(DataFrameLeft, text="Address", font=("times new roman", 15, "bold"), padx=2, pady=6, bg="powder blue")
        lblAddress.grid(row=4, column=0, sticky=W)
        self.txtAddress = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)
        self.txtAddress.grid(row=4, column=1)
        
        btnRegister = Button(frame, text="Register", font=("times new roman", 20, "bold"), bg="light green", command=self.register)
        btnRegister.place(x=20, y=320)

        btnBack = Button(frame, text="Back", font=("times new roman", 20, "bold"), bg="light coral", command=self.go_back)
        btnBack.place(x=1400, y=320)

    def register(self):
        first_name = self.txtFirstName.get()
        last_name = self.txtLastName.get()
        email = self.txtEmail.get()
        phone = self.txtPhone.get()
        address = self.txtAddress.get()
        # Add your logic to handle registration here.
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print(f"Address: {address}")
        # Reset fields or show confirmation message here
        self.txtFirstName.delete(0, END)
        self.txtLastName.delete(0, END)
        self.txtEmail.delete(0, END)
        self.txtPhone.delete(0, END)
        self.txtAddress.delete(0, END)

    def go_back(self):
        self.window.destroy()
        main_window = Tk()
        InitialMenu(main_window)
        main_window.mainloop()
        
        
        

if __name__ == "__main__":
    root = Tk()
    InitialMenu(root)
    root.mainloop()
