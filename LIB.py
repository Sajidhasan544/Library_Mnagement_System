from tkinter import *
from tkinter import ttk
from PIL import Image, ImageDraw, ImageTk
import BorrowClass
import RtnBook
import RGST
import PasS
import Userconsole

class InitialMenu:
    def __init__(self, window):
        self.window = window
        self.window.title("Library Management System")
        self.window.geometry("1530x790+0+0")

        lbltit = Label(self.window, text="Library Management System", 
                       bg="powder blue", fg="green", bd=20, relief=RIDGE, 
                       font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltit.pack(side=TOP, fill=X)

        frame = Frame(self.window, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)

        self.btnBorrow_img = self.create_rounded_button(400, 100, radius=25, color=(173, 216, 230))  
        self.btnRegister_img = self.create_rounded_button(430, 100, radius=25, color=(240, 128, 128)) 
        self.btnExit_img = self.create_rounded_button(150, 50, radius=25, color=(255, 0, 0)) 
        self.btnAdmin_img = self.create_rounded_button(200, 50, radius=25, color=(0, 128, 0)) 

        btnBorrow = Button(frame, image=self.btnBorrow_img, text="User Login", 
                           font=("times new roman", 20, "bold"), borderwidth=0, 
                           compound="center", bg="powder blue", command=self.open_user)
        btnBorrow.place(x=100, y=150)

        btnRegister = Button(frame, image=self.btnRegister_img, text="First Time Registration", 
                             font=("times new roman", 20, "bold"), borderwidth=0, 
                             compound="center", bg="powder blue", command=self.open_registration_window)
        btnRegister.place(x=450, y=275)

        btnExit = Button(frame, image=self.btnExit_img, text="Exit", 
                         font=('times new roman', 20, 'bold'), borderwidth=0, 
                         compound="center", bg="powder blue", command=self.exit)
        btnExit.place(x=1310, y=320)

        btnAdmin = Button(frame, image=self.btnAdmin_img, text="Admin Panel", 
                          font=('times new roman', 20, 'bold'), borderwidth=0, 
                          compound="center", bg="powder blue", command=self.open_admin_panel)
        btnAdmin.place(x=100, y=320)

    def create_rounded_button(self, width, height, radius, color):
        """Create a rounded button image with the specified color."""
        image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)

        draw.rounded_rectangle((0, 0, width, height), radius=radius, fill=color)
        return ImageTk.PhotoImage(image)

    def open_admin_panel(self):
        self.window.destroy()
        admin_window = Tk()
        PasS.PasswordApp(admin_window)
        admin_window.mainloop()

    def open_user(self):
        self.window.destroy()
        borrow_window = Tk()
        Userconsole.LibraryLogin(borrow_window)
        borrow_window.mainloop()

    def open_return_window(self):
        self.window.destroy()
        return_window = Tk()
        RtnBook.ReturnBook(return_window)
        return_window.mainloop()

    def open_registration_window(self):
        self.window.destroy()
        registration_window = Tk()
        RGST.Registration(registration_window)
        registration_window.mainloop()

    def exit(self):
        self.window.destroy()


if __name__ == "__main__":
    root = Tk()
    app = InitialMenu(root)
    root.mainloop()
