from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
import LIB
import BorrowClass
import Userpanel
from PIL import Image, ImageDraw, ImageTk
from hashlib import sha256



class LibraryLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Library User Login")
        self.root.geometry("1530x790+0+0")
        self.root.config(bg="white")

        lbltit = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="white", fg="green", relief="ridge", font=("times new roman", 25, "bold"), padx=2, pady=6)
        lbltit.pack(side=TOP, fill=X)

        frame = Frame(self.root, relief="ridge", padx=20, pady=20, bg="white")
        frame.place(x=0, y=130, width=650, height=500) 

        lblmember = Label(frame, bg="white", text="Member Type", font=("times new roman", 14, "bold"))
        lblmember.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        self.selected = StringVar()
        self.commember = ttk.Combobox(frame, font=("times new roman", 14, "bold"), width=28, state="readonly", textvariable=self.selected)
        self.commember["values"] = ("ADMIN", "STAFF", "STUDENT", "LECTURER")
        self.commember.grid(row=0, column=1, padx=10, pady=10)
        
        self.username_label = Label(frame, text="Username", bg="white", font=("times new roman", 14, "bold"))
        self.username_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.username_entry = Entry(frame, font=("times new roman", 14, "bold"), width=30)
        self.username_entry.grid(row=1, column=1, padx=10, pady=10)

        self.password_label = Label(frame, text="Password", bg="white", font=("times new roman", 14, "bold"))
        self.password_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.password_entry = Entry(frame, show="*", font=("times new roman", 14, "bold"), width=30)
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)

        button_width = 350
        button_height = 60
        button_color = (77, 0, 25)  
        button_padding = 0  
        top_padding = 20 

        self.button_image = self.create_rounded_button(button_width, button_height, radius=30, color=button_color)

        Button(
            frame,
            text="Login",
            font=("arial", 12, "bold"),
            bg="white",
            fg="white",
            image=self.button_image,
            compound="center",
            command=self.login,
            height=button_height,
            width=button_width,
            borderwidth=0
        ).grid(row=3, columnspan=2, pady=top_padding)

        Button(
            frame,
            text="Back",
            font=("arial", 12, "bold"),
            bg="white",
            fg="white",
            image=self.button_image,
            compound="center",
            command=self.back,
            height=button_height,
            width=button_width,
            borderwidth=0
        ).grid(row=4, columnspan=2, pady=button_padding)

        self.connection = pymysql.connect(host="localhost", user="root", passwd="", database="library_mnagemet")
        self.mycursor = self.connection.cursor()

    def create_rounded_button(self, width, height, radius, color):
        """Create a rounded button image with the specified color."""
        image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        draw.rounded_rectangle((0, 0, width, height), radius=radius, fill=color)
        return ImageTk.PhotoImage(image)
    
   
    def get_result_for_membertype(self, membertype):
        username = usernames
        sql = "SELECT * FROM userinfo WHERE username = %s AND membertype = %s"
        self.mycursor.execute(sql, (username, membertype))
        result = self.mycursor.fetchone()
        return result


    def login(self):
        username = self.username_entry.get()
        global usernames
        usernames = usernames
        input_password = self.password_entry.get()
        membertype = self.commember.get()    
        global member
        member = membertype
        
        sql = "SELECT * FROM userinfo WHERE username = %s AND membertype = %s"
        self.mycursor.execute(sql, (username, membertype))
        result = self.mycursor.fetchone()
        
        if result:
            stored_hashed_password = result[7] 
            input_hashed_password = sha256(input_password.encode()).hexdigest()

            if input_hashed_password == stored_hashed_password:
                global fname,lname
                fname, lname = result[2].split()[0], result[2].split()[1] 
                global dprt
                dprt = result[1]
                global id
                id = result[3]
                global intake
                intake = result[4]
                global section 
                section = result[5]
                    
                self.root.destroy()
                admin_window = Tk()
                Userpanel.UserPanel(admin_window)
                admin_window.mainloop()
                
            else:
                messagebox.showerror("Login Failed", "Invalid username or password.")
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
        
        
usernames = None
member = None
fname = None
lname = None
dprt =  None
intake = None
section = None
id = None

if __name__ == "__main__":
    root = Tk()
    app = LibraryLogin(root)
    root.mainloop()
    
