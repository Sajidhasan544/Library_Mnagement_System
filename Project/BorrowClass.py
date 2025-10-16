from tkinter import *
from tkinter import ttk 
import LIB
import pymysql
import Userpanel
import Userconsole
from datetime import date, timedelta
class Libs:
    def __init__(self, window):
        self.connection = pymysql.connect(host="localhost", user="root", passwd="", database="library_mnagemet")
        self.mycursor = self.connection.cursor()
        self.member = Userconsole.member
        self.fname = Userconsole.fname
        self.lname = Userconsole.lname
        self.id_no = Userconsole.id
        self.dept = Userconsole.dprt
        self.intake = Userconsole.intake
        self.section = Userconsole.section

        self.window = window
        self.window.title("Library Management System - Borrow a Book")
        self.window.geometry("1530x790+0+0")

        lbltit = Label(self.window, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltit.pack(side=TOP, fill=X)
        frame = Frame(self.window, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)

        DataFrameLeft = LabelFrame(frame, text="MEMBERS INFORMATION", bg="powder blue", bd=12, relief=RIDGE, font=("times new roman", 20, "bold"), padx=2, pady=6)
        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        lblmember = Label(DataFrameLeft, bg="powder blue", text="Member Type", font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblmember.grid(row=0, column=0, sticky=W)

        self.commember = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)
        self.commember.grid(row=0, column=1)
        self.commember.insert(END,self.member)
        

        self.lbldptName = Label(DataFrameLeft, font=("times new roman", 15, "bold"), text="Dpt.", padx=2, pady=6, bg="powder blue")
        self.dpt = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)
        if self.dept != None:
            self.dpt.insert(END,self.dept)

        self.lblFirstName = Label(DataFrameLeft, font=("times new roman", 15, "bold"), text="FirstName", padx=2, pady=6, bg="powder blue")
        self.txtFirstName = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)


        self.lblLstName = Label(DataFrameLeft, font=("times new roman", 15, "bold"), text="LastName", padx=2, pady=6, bg="powder blue")
        self.txtLstName = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)

        self.ld_no = Label(DataFrameLeft, bg="powder blue", text="ID NO", font=("times new roman", 15, "bold"), padx=2, pady=6)
        self.txtId_no = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)

        self.lblIntake = Label(DataFrameLeft, bg="powder blue", text="Intake", font=("times new roman", 15, "bold"), padx=2, pady=6)
        self.txtIntake = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)

        self.lblSec = Label(DataFrameLeft, bg="powder blue", text="Section", font=("times new roman", 15, "bold"), padx=2, pady=6)
        self.txtSec = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)

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

        self.txtbox = Text(DataFrameRight, font=("arial", 12, "bold"), width=32, height=14, padx=2, pady=6)
        self.txtbox.grid(row=1, column=2)



        listscrolbar = Scrollbar(DataFrameRight)
        listscrolbar.grid(row=1, column=1, sticky="ns")

        self.listofbooks = ['Head first Book', 'Learn Python The Hard Way', 'Python Programming', 'Secret Rahasya', 'The Secret',
                            'Othello', 'Romeo and Juliet', 'Machine Learning', 'ML Development', 'SW Development', 'Cyber Security',
                            'C++ Learning', 'Web Development', 'AI Basics']

        self.listbox = Listbox(DataFrameRight, font=("arial", 12, "bold"), width=20, height=12)
        self.listbox.bind('<<ListboxSelect>>', self.on_select)
        self.listbox.grid(row=1, column=0, padx=8)
        listscrolbar.config(command=self.listbox.yview)

        for item in self.listofbooks:
            self.listbox.insert(END, item)

        self.search_var = StringVar()
        search_entry = Entry(DataFrameRight, textvariable=self.search_var, font=("arial", 12, "bold"), width=20)
        search_entry.place(x=8,y=-5)
        search_entry.bind("<FocusOut>", self.set_placeholder)
        search_entry.bind("<KeyRelease>", self.search_books)
        search_entry.bind("<FocusIn>", self.clear_placeholder)
        
        
        Framebutton = Frame(self.window, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x=0, y=530, width=1530, height=58)

        btnBorrow = Button(Framebutton, text="Borrow", font=("arial", 12, "bold"), width=25, bg="light blue", command=self.borrow_book)
        btnBorrow.grid(row=0, column=0)

        btnBack = Button(Framebutton, text="Back", font=("arial", 12, "bold"), width=25, bg="light blue", command=self.go_back)
        btnBack.grid(row=0, column=1)

        showtable = Frame(self.window, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        showtable.place(x=0, y=576, width=1530, height=200)

        self.tree = ttk.Treeview(showtable, columns=("Member Info", "Book Info"), show='headings', height=8)

        self.tree.heading("Member Info", text="Member Information")
        self.tree.heading("Book Info", text="Book Information")

        self.tree.column("Member Info", width=350)
        self.tree.column("Book Info", width=350)
        self.tree.pack(fill=BOTH, expand=1)
        
        self.update_dpt_op()
    def update_dpt_op(self):
        membertype = self.commember.get()
        self.reset_grid_positions() 
        print(f"Name is {self.fname} and lname is {self.lname}")
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

        elif membertype == "LECTURER":
            
            
            self.lbldptName.grid(row=1, column=0, sticky=W)
            self.dpt.grid(row=1, column=1)
            self.lblFirstName.grid(row=2, column=0, sticky=W)
            self.txtFirstName.grid(row=2, column=1)
            self.lblLstName.grid(row=3, column=0, sticky=W)
            self.txtLstName.grid(row=3, column=1)

        
        self.insertvalues(membertype)

        
        
    def search_books(self, event):
        search_term = self.search_var.get().lower()
        self.listbox.delete(0, END)
        for book in self.listofbooks:
            if search_term in book.lower():
                self.listbox.insert(END, book)
                
                
    def clear_placeholder(self, event):
        if self.search_var.get() == "Search":
            self.search_var.set("")
    
    def set_placeholder(self, event):
        if not self.search_var.get():
            self.search_var.set("Search")
        
        
    def reset_grid_positions(self):
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

    def on_select(self, event):
        selected_book = event.widget.get(event.widget.curselection())
        book_details = {
            'Head first Book': ('001', 'Head first Book', 'Author A','This is my first book','400'),
            'Learn Python The Hard Way': ('002', 'Learn Python The Hard Way', 'Author B','Good book for learning python Hard way','500'),
            'Python Programming': ('003', 'Python Programming', 'Author C','Learn basic Python program','450'),
            'Secret Rahasya': ('004', 'Secret Rahasya', 'Author D',' It is based on the belief of the pseudoscientific law of attraction','600'),
            'The Secret': ('005', 'The Secret', 'Author E','Secreate book','650'),
            'Othello': ('006', 'Othello', 'Author F','Othello books','700'),
            'Romeo and Juliet': ('007', 'Romeo and Juliet', 'Author G','Romantic book','740'),
            'Maching Learning': ('008','Maching Learning', 'Author H','Good ML learning book','750'),
            'ML Development' : ('009','ML Development','Author I','ML Development book','800'),
            'SW Development' : ('010','SW Development','Author J','SW development book','900'),
            'Cyber Security' : ('011','Cyber Security','Author K','Learn Cyber security','300'),
            'C++ Learning' : ('012','C++ Learning','Author L','Basic C++','690'),
            'Web Development' : ('013','Web Development','Author M','Web Development','1100'),
            'AI Basics' : ('014','AI Basics','Author L','Learn basics of AI','1000')
        }
        
        if selected_book in book_details:
            book_id, title, author,bookinfo,actprice = book_details[selected_book]
            today = date.today()
            duedate = today + timedelta(days=5)
            overdue = today + timedelta(days=7)
            self.txtBookid.delete(0, END)
            self.txtBookid.insert(END, book_id)
            self.txtBooktitle.delete(0, END)
            self.txtBooktitle.insert(END, title)
            self.txtAuthorname.delete(0, END)
            self.txtAuthorname.insert(END, author)
            self.txtbox.delete(1.0,END)
            self.txtbox.insert(END,bookinfo)
            self.txtDatebor.delete(0, END)
            self.txtDatebor.insert(END,today)
            self.txtDatedu.delete(0, END)
            self.txtDatedu.insert(END, duedate)
            self.txtOverdu.delete(0, END)
            self.txtOverdu.insert(END, overdue)
            self.txtActp.delete(0, END)
            self.txtActp.insert(END, actprice)
            
            
    def borrow_book(self):
        self.tree.delete(*self.tree.get_children())

        fname = self.txtFirstName.get()
        lname = self.txtLstName.get()
        member_type = self.commember.get()
        book_id = self.txtBookid.get()
        book_title = self.txtBooktitle.get()
        author_name = self.txtAuthorname.get()
        date_borrowed = self.txtDatebor.get()
        date_due = self.txtDatedu.get()
        date_overdue = self.txtOverdu.get()
        actual_price = self.txtActp.get()

        member_info = f"    Type: {member_type}\n    Name : {fname} {lname}"
        book_info = f"    Book ID: {book_id}\n    Book Title: {book_title}\n    Author: {author_name}\n    Borrowed: {date_borrowed}\n    Due: {date_due}\n    Overdue: {date_overdue}\n    Price: {actual_price}"
        
        self.tree.insert("", "end", values=(member_info, book_info))
        self.updates()
        self.clear_fields()


    def updates(self):
        try:
            connection = pymysql.connect(host="localhost", user="root", passwd="", database="library_mnagemet")
            mycursor = connection.cursor()
            fname = self.txtFirstName.get()
            lname = self.txtLstName.get()
            id = self.txtId_no.get()
            member_type = self.commember.get()
            dpt = self.dpt.get()
            intke = self.txtIntake.get()
            section = self.txtSec.get()
            bookid = self.txtBookid.get()
            today = date.today()
            du_day = today + timedelta(days=5)
            duedate = du_day.day

            if member_type == "STUDENT":
                sqlformula = "INSERT INTO students (Name, id, dept, intke, Section,bookid,dudate) VALUES (%s,%s,%s, %s, %s, %s, %s)"
                student_data = (f"{fname} {lname}", id, dpt, intke, section,bookid,duedate)
                mycursor.execute(sqlformula, student_data)

            elif member_type == "ADMIN":
                sqlformula = "INSERT INTO admin (name,bookid,dudate) VALUES (%s,%s,%s)"
                admin_data = (f"{fname} {lname}",bookid,duedate)
                mycursor.execute(sqlformula, admin_data)

            elif member_type == "STAFF":
                sqlformula = "INSERT INTO staff (name, dept, id,bookid,dudate) VALUES (%s,%s, %s, %s,%s)"
                staff_data = (f"{fname} {lname}", dpt, id,bookid,duedate)
                mycursor.execute(sqlformula, staff_data)

            elif member_type == "LECTURER":
                sqlformula = "INSERT INTO lecturer (name, dpt,bookid,dudate) VALUES (%s, %s,%s,%s)"
                lecturer_data = (f"{fname} {lname}", dpt,bookid,duedate)
                mycursor.execute(sqlformula, lecturer_data)

            connection.commit()
        finally:
            mycursor.close()
            connection.close()
        
        
        
    def insertvalues(self,membertype):
        if membertype == "ADMIN":
            self.txtFirstName.delete(0, END)
            self.txtFirstName.insert(END, self.fname)
            self.txtLstName.delete(0, END)
            self.txtLstName.insert(END, self.lname)
    
        elif membertype == "STAFF":
            self.txtFirstName.delete(0, END)
            self.txtFirstName.insert(0, self.fname)
            self.txtLstName.delete(0, END)
            self.txtLstName.insert(0, self.lname)
            self.txtId_no.delete(0, END)
            self.txtId_no.insert(0, self.id_no)
            self.dpt.set(self.dept)
            
        elif membertype == "STUDENT":
            self.txtFirstName.delete(0, END)
            self.txtFirstName.insert(0, self.fname)
            self.txtLstName.delete(0, END)
            self.txtLstName.insert(0, self.lname)
            self.txtId_no.delete(0, END)
            self.txtId_no.insert(0, self.id_no)
            self.txtIntake.delete(0, END)
            self.txtIntake.insert(0, self.intake)
            self.txtSec.delete(0, END)
            self.txtSec.insert(0, self.section)
            self.dpt.set(self.dept)
        elif membertype == "LECTURER":
            self.txtFirstName.delete(0, END)
            self.txtFirstName.insert(0, self.fname)
            self.txtLstName.delete(0, END)
            self.txtLstName.insert(0, self.lname)
            self.txtId_no.delete(0, END)
            self.txtId_no.insert(0, self.id_no)
            self.dpt.set(self.dept)
            
            
            

    def clear_fields(self):
        self.txtFirstName.delete(0, END)
        self.txtLstName.delete(0, END)
        self.txtId_no.delete(0, END)
        self.dpt.set('')
        self.txtIntake.delete(0, END)
        self.txtSec.delete(0, END)
        self.txtBookid.delete(0, END)
        self.txtBooktitle.delete(0, END)
        self.txtAuthorname.delete(0, END)
        self.txtDatebor.delete(0, END)
        self.txtDatedu.delete(0, END)
        self.txtOverdu.delete(0, END)
        self.txtActp.delete(0, END)

    def go_back(self):
        self.window.destroy()
        main_window = Tk()
        Userpanel.UserPanel(main_window)
        main_window.mainloop()

