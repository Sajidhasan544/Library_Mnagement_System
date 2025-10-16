import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import LIB

class ResetSystem:
    def __init__(self, window):
        self.window = window
        self.window.title("Library Management System - Reset System")
        self.window.geometry("1530x790+0+0")
        
        lbltit = Label(self.window, text="Library Management System", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltit.pack(side=TOP, fill=X)

        frame = Frame(self.window, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=180, width=1530, height=400)

        self.tree = ttk.Treeview(frame, columns=("Username", "Nam"), show="headings", height=15)
        self.tree.heading("Username", text="Username")
        self.tree.heading("Nam", text="Name")
        
        self.tree.column("Username", width=200)
        self.tree.column("Nam", width=300)

        scrollbar = Scrollbar(frame, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.tree.pack(fill=BOTH, expand=True)

    
        self.load_user_data()

        self.entry_username = Entry(self.window, font=("times new roman", 20), bd=5, relief=GROOVE)
        self.entry_username.place(x=100, y=630, width=400, height=50)

        
        remove_button = Button(self.window, text="Remove User", font=("times new roman", 20, "bold"), bg="orange", command=self.remove_user)
        remove_button.place(x=520, y=630, width=400, height=50)

    
        reset_button = Button(self.window, text="Reset System", font=("times new roman", 20, "bold"), bg="red", command=self.reset_system)
        reset_button.place(x=100, y=720, width=400, height=60)

        btnback = Button(self.window, text="Back", font=("times new roman", 20, "bold"), bg="light coral", command=self.go_back)
        btnback.place(x=520, y=720, width=400, height=60)

    def load_user_data(self):
        """Fetch and load the user data from the database into the Treeview."""
        try:
            connection = pymysql.connect(host="localhost", user="root", passwd="", database="library_mnagemet")
            mycursor = connection.cursor()

            
            mycursor.execute("SELECT username, nam FROM userinfo")
            users = mycursor.fetchall()

            for user in users:
                self.tree.insert("", END, values=user)

            connection.close()
        except pymysql.MySQLError as e:
            messagebox.showerror("Error", f"Error loading user data: {e}")

    def remove_user(self):
        """Remove the user from the database and update the Treeview."""
        username = self.entry_username.get()
        
        if username == "":
            messagebox.showwarning("Input Required", "Please enter a username to remove.")
            return

        try:
            connection = pymysql.connect(host="localhost", user="root", passwd="", database="library_mnagemet")
            mycursor = connection.cursor()

            
            mycursor.execute("DELETE FROM userinfo WHERE username = %s", (username,))
            connection.commit()

            if mycursor.rowcount > 0:
                messagebox.showinfo("Success", f"User {username} has been removed.")
                
        
                for row in self.tree.get_children():
                    if self.tree.item(row)["values"][0] == username:
                        self.tree.delete(row)
                        break
            else:
                messagebox.showerror("Error", f"No user found with username: {username}")
            
            connection.close()
        except pymysql.MySQLError as e:
            messagebox.showerror("Error", f"Error removing user: {e}")

    def reset_system(self):
        """Reset the system by truncating all tables."""
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
            self.tree.delete(*self.tree.get_children()) 
            self.load_user_data()
        except pymysql.MySQLError as e:
            messagebox.showerror("Error", f"Error resetting tables: {e}")

    def go_back(self):
        """Go back to the main menu."""
        self.window.destroy() 
        main_window = Tk()  
        LIB.InitialMenu(main_window) 
        main_window.mainloop()


if __name__ == "__main__":
    root = Tk()
    app = ResetSystem(root)
    root.mainloop()
