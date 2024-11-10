import pymysql
from tkinter import *
from tkinter import messagebox
import LIB

class ResetSystem:
    def __init__(self, window):
        self.window = window
        self.window.title("Library Management System - Return a Book")
        self.window.geometry("1530x790+0+0")
        
        lbltit = Label(self.window, text="Library Management System", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltit.pack(side=TOP, fill=X)
        
        frame = Frame(self.window, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)

        reset_button = Button(frame, text="Reset System", font=("times new roman", 20, "bold"), bg="red", command=self.reset_system)
        reset_button.place(x=100, y=150, width=400, height=100)
        
        btnback = Button(frame, text="Back", font=("times new roman", 20, "bold"), bg="light coral", command=self.go_back)
        btnback.place(x=450, y=275, width=630, height=100)
        
    def reset_system(self):
        try:
            connection = pymysql.connect(host="localhost", user="root", passwd="", database="library_mnagemet")
            mycursor = connection.cursor()

            mycursor.execute("TRUNCATE TABLE students")
            mycursor.execute("TRUNCATE TABLE admin")
            mycursor.execute("TRUNCATE TABLE staff")
            mycursor.execute("TRUNCATE TABLE lecturer")
            mycursor.execute("TRUNCATE TABLE userinfo")

            connection.commit()
            mycursor.close()
            connection.close()
            messagebox.showinfo("Success", "System has been reset successfully.")
        except pymysql.MySQLError as e:
            messagebox.showerror("Error", f"Error resetting tables: {e}")

    def go_back(self):
        self.window.destroy() 
        main_window = Tk()  
        LIB.InitialMenu(main_window) 
        main_window.mainloop()
