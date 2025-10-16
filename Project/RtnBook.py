from tkinter import *
from tkinter import ttk, messagebox
import pymysql
import Userpanel
import Userconsole

class ReturnBook:
    def __init__(self, window):
        self.window = window
        self.window.title("Library Management System - Return a Book")
        self.window.geometry("1530x790+0+0")

        lbltit = Label(self.window, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltit.pack(side=TOP, fill=X)

        frame = Frame(self.window, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)

        lblbookid = Label(frame, text="Enter Book ID to Return", font=("times new roman", 20, "bold"), padx=2, pady=6, bg="powder blue")
        lblbookid.grid(row=0, column=0, sticky=W)

        self.txtbookid = Entry(frame, font=("times new roman", 20, "bold"), width=30)
        self.txtbookid.grid(row=0, column=1)
        
        lbldudate = Label(frame, text="Enter Due Date (only day) to Return", font=("times new roman", 20, "bold"), padx=2, pady=6, bg="powder blue")
        lbldudate.grid(row=1, column=0, sticky=W)

        self.dudate = Entry(frame, font=("times new roman", 20, "bold"), width=30)
        self.dudate.grid(row=1, column=1)

        Framebutton = Frame(self.window, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x=0, y=530, width=1530, height=70)

        btnReturn = Button(Framebutton, text="Return Book", font=("arial", 12, "bold"), width=25, bg="light green", command=self.return_book)
        btnReturn.grid(row=0, column=0)

        btnExit = Button(Framebutton, text="Back", font=("arial", 12, "bold"), width=25, bg="light green", command=self.go_back)
        btnExit.grid(row=0, column=1)

    def return_book(self):
        book_id = self.txtbookid.get()
        due_date_day = self.dudate.get()  # This contains only the day (as string or integer)
        mem = Userconsole.member
        table_name = ""

    # Determine the table name based on member type
        if mem == "ADMIN":
            table_name = "admin"
        elif mem == "STUDENT":
            table_name = "students"
        elif mem == "STAFF":
            table_name = "staff"
        elif mem == "LECTURER":
            table_name = "lecturer"
        else:
            messagebox.showerror("Error", "Invalid member type!")
            return

    # Validate input fields
        if not book_id or not due_date_day:
            messagebox.showerror("Error", "Please fill all fields!")
            return

        try:
            # Connect to the database
            connection = pymysql.connect(host="localhost", user="root", passwd="", database="library_mnagemet")
            cursor = connection.cursor()

        # Query to find the matching book entry
            query = f"""
                SELECT * FROM {table_name} 
                WHERE bookid = %s AND dudate = %s
            """
            cursor.execute(query, (book_id, due_date_day))
            result = cursor.fetchone()

            if result:
            # If found, delete the row
                delete_query = f"DELETE FROM {table_name} WHERE bookid = %s AND dudate = %s"
                cursor.execute(delete_query, (book_id, due_date_day))
                connection.commit()
                messagebox.showinfo("Success", "Book returned successfully!")
            else:
                messagebox.showerror("Error", "No matching book found or incorrect due date.")

        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            cursor.close()
            connection.close()


    def go_back(self):
        self.window.destroy()
        main_window = Tk()
        Userpanel.UserPanel(main_window)
        main_window.mainloop()
