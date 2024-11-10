import tkinter as tk
from tkinter import messagebox
import Admin
import LIB

class PasswordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("300x150")
        
        self.label = tk.Label(self.root, text="Enter Password:")
        self.label.pack(pady=10)
        
        self.password_entry = tk.Entry(self.root, show="*") 
        self.password_entry.pack(pady=5)
        
        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_password)
        self.submit_button.pack(pady=10)
        self.backbutton = tk.Button(self.root,text="Back",command=self.go_back)
        self.backbutton.pack(pady=4)
        
    def check_password(self):
        entered_password = self.password_entry.get()
        correct_password = "123" 
        
        if entered_password == correct_password:
            self.open_new_window()
        else:
            messagebox.showerror("Error", "Incorrect Password")

    def open_new_window(self):
        self.root.destroy()  
        admin_window = tk.Tk() 
        Admin.ResetSystem(admin_window) 
        admin_window.mainloop()
        
    def go_back(self):
        self.root.destroy()
        main_window = tk.Tk()
        LIB.InitialMenu(main_window)
        main_window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordApp(root)
    root.mainloop()
