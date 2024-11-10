from tkinter import *
from tkinter import ttk 
import LIB
import Userpanel

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

        Framebutton = Frame(self.window, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x=0, y=530, width=1530, height=70)

        btnReturn = Button(Framebutton, text="Return Book", font=("arial", 12, "bold"), width=25, bg="light green", command=self.return_book)
        btnReturn.grid(row=0, column=0)

        btnExit = Button(Framebutton, text="Back", font=("arial", 12, "bold"), width=25, bg="light green", command=self.go_back)
        btnExit.grid(row=0, column=1)

    def return_book(self):
        
        print("Returned book information recorded.")


    def go_back(self):
        self.window.destroy()
        main_window = Tk()
        Userpanel.UserPanel(main_window)
        main_window.mainloop()