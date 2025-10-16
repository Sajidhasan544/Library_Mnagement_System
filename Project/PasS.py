import tkinter as tk
from tkinter import messagebox
import Admin
import LIB

class PasswordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("1530x790+0+0") 
        
        lbltit = tk.Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="green", font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltit.pack(side=tk.TOP, fill=tk.X)
        
        frame = tk.Frame(self.root, bg="powder blue")
        frame.place(relx=0.5, rely=0.4, anchor="center") 
        

        self.label = tk.Label(frame, text="Enter Password:", bg="powder blue", fg="green", font=("times new roman", 20, "bold"))
        self.label.pack(pady=20)  
        
        
        self.password_entry = tk.Entry(frame, show="*", font=("times new roman", 18), bd=5, relief="ridge")
        self.password_entry.pack(pady=10)
        
        self.submit_button = tk.Button(frame, text="Submit", font=("arial", 12, "bold"), width=20, bg="light green", command=self.check_password)
        self.submit_button.pack(pady=10)
        
        
        self.backbutton = tk.Button(frame, text="Back", font=("arial", 12, "bold"), width=20, bg="light green", command=self.go_back)
        self.backbutton.pack(pady=4)
        
        
        self.root.config(bg="powder blue")  

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
