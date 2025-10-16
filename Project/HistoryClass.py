from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
import Userpanel
import Userconsole

class History:
    def __init__(self, window):
        self.window = window
        self.window.title("Library Management System - Borrowed Book History")
        self.window.geometry("1530x790+0+0")
        
        lbltit = Label(
            self.window,
            text="LIBRARY MANAGEMENT SYSTEM",
            bg="powder blue",
            fg="green",
            bd=20,
            relief=RIDGE,
            font=("times new roman", 50, "bold"),
            padx=2,
            pady=6,
        )
        lbltit.pack(side=TOP, fill=X)

    
        frame = Frame(self.window, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)


        frame.grid_columnconfigure(0, weight=1)  
        frame.grid_columnconfigure(1, weight=1) 
        frame.grid_rowconfigure(1, weight=1)     

        
        lbl_member_info = Label(frame, text="Member Information", font=("arial", 16, "bold"), bg="powder blue")
        lbl_member_info.grid(row=0, column=0, padx=20, pady=10)

        
        self.user_tree = ttk.Treeview(
            frame, columns=("name", "mem_type"), show="headings"
        )
        self.user_tree.heading("name", text="Name")
        self.user_tree.heading("mem_type", text="Member Type")
        self.user_tree.column("name", width=200, anchor=CENTER)  
        self.user_tree.column("mem_type", width=150, anchor=CENTER) 
        self.user_tree.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        
        lbl_book_info = Label(frame, text="All Pending Books", font=("arial", 16, "bold"), bg="powder blue")
        lbl_book_info.grid(row=0, column=1, padx=20, pady=10)

    
        self.books_tree = ttk.Treeview(
            frame, columns=("bookid", "dudate"), show="headings"
        )
        self.books_tree.heading("bookid", text="Book ID")
        self.books_tree.heading("dudate", text="Due Date")
        self.books_tree.column("bookid", width=100, anchor=CENTER)  
        self.books_tree.column("dudate", width=150, anchor=CENTER)  
        self.books_tree.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")


        self.load_history()
        self.load_user_details()


        Framebutton = Frame(self.window, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x=0, y=530, width=1530, height=70)

    
        btnReturn = Button(
            Framebutton, text="Return Book", font=("arial", 12, "bold"), width=25, bg="light green", command=self.return_book
        )
        btnReturn.grid(row=0, column=0)

        btnExit = Button(
            Framebutton, text="Back", font=("arial", 12, "bold"), width=25, bg="light green", command=self.go_back
        )
        btnExit.grid(row=0, column=1)

    def load_history(self):
        """Fetch borrowed books and due dates from the database."""
        mem = Userconsole.member  
        table_name = ""

    
        if mem == "ADMIN":
            table_name = "admin"
        elif mem == "STUDENT":
            table_name = "students"
        elif mem == "STAFF":
            table_name = "staff"
        elif mem == "LECTURER":
            table_name = "lecturer"

        try:
            connection = pymysql.connect(host="localhost", user="root", passwd="", database="library_mnagemet")
            cursor = connection.cursor()
            
            
            query = f"""
                SELECT bookid, dudate
                FROM {table_name}
            """
            cursor.execute(query)
            result = cursor.fetchall()
            
    
            for row in result:
                self.books_tree.insert("", "end", values=row)
            
        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

    def load_user_details(self):
        """Fetch user details (name and member type) based on current member type."""
        mem = Userconsole.member 
        table_name = ""

        if mem == "ADMIN":
            table_name = "admin"
        elif mem == "STUDENT":
            table_name = "students"
        elif mem == "STAFF":
            table_name = "staff"
        elif mem == "LECTURER":
            table_name = "lecturer"

        try:
            connection = pymysql.connect(host="localhost", user="root", passwd="", database="library_mnagemet")
            cursor = connection.cursor()
            
            query = f"""
                SELECT name
                FROM {table_name}
            """
            cursor.execute(query)
            result = cursor.fetchall()
            
        
            for row in result:

                self.user_tree.insert("", "end", values=(row[0], mem))
            
        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

    def return_book(self):
        """Handle return book functionality."""
        print("Return Book functionality")
    
    def go_back(self):
        """Go back to the previous screen."""
        self.window.destroy()
        main_window = Tk()
        Userpanel.UserPanel(main_window)
        main_window.mainloop()
