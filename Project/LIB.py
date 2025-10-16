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
                       bg="White", fg="black", relief=RIDGE,
                       font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltit.pack(side=TOP, fill=X)

        frame = Frame(self.window, relief=RIDGE, padx=20, bg="White")
        frame.place(x=0, y=130, width=1530, height=700)

        button_width = 350
        button_height = 100
        button_color = (153, 0, 51) 
        button_padding = 20 
        top_padding = 20 

        self.button_image = self.create_rounded_button(button_width, button_height, radius=30, color=button_color)

    
        buttons = [
            ("User Login", self.open_user),
            ("First Time Registration", self.open_registration_window),
            ("Admin Panel", self.open_admin_panel),
            ("Exit", self.exit)
        ]

        for index, (text, command) in enumerate(buttons):
            Button(
                frame,
                fg="white",
                image=self.button_image,
                text=text,
                font=("times new roman", 20, "bold"),
                borderwidth=0,
                compound="center",
                bg="white",
                command=command,
                height=button_height,
                width=button_width
            ).place(x=0, y=top_padding + index * (button_height + button_padding))

        self.add_side_image(frame, x=400, y=50)

    def create_rounded_button(self, width, height, radius, color):
        """Create a rounded button image with the specified color."""
        image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        draw.rounded_rectangle((0, 0, width, height), radius=radius, fill=color)
        return ImageTk.PhotoImage(image)

    def add_side_image(self, parent, x, y):
        """Add an image to the right side of the buttons."""
        try:
            img = Image.open("vecteezy_book-stack-clipart-design-illustration_46338982.png").resize((800, 400))  
            img = ImageTk.PhotoImage(img)
            side_image_label = Label(parent, image=img, bg="white")
            side_image_label.image = img  
            side_image_label.place(x=x, y=y)  
        except FileNotFoundError:
            print("Image file not found. Please check the path.")

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
