from tkinter import *
from PIL import Image, ImageDraw, ImageTk
import BorrowClass  
import HistoryClass  
import LIB  
import RtnBook

class UserPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("User Panel")
        self.root.geometry("1530x790+0+0")
        self.root.config(bg="white")

        lbltit = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="white", fg="green", relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltit.pack(side=TOP, fill=X)

        Framebutton = Frame(self.root, relief="ridge", padx=20, bg="white")
        Framebutton.place(x=0, y=130, width=1530, height=700)

        button_width = 350
        button_height = 100
        button_color = (173, 216, 230)  
        button_padding = 20
        top_padding = 20 

        self.button_image = self.create_rounded_button(button_width, button_height, radius=30, color=button_color)

        buttons = [
            ("Borrow Book", self.open_borrow_book_window),
            ("Return a Book", self.open_return_window),
            ("Show My History", self.show_user_history),
            ("Log out", self.back)
        ]

        for index, (text, command) in enumerate(buttons):
            Button(
                Framebutton,
                image=self.button_image,
                text=text,
                font=("times new roman", 20, "bold"),
                borderwidth=0,
                compound="center",
                bg="white",
                command=command,
                height=button_height,
                width=button_width
            ).place(x=20, y=top_padding + index * (button_height + button_padding))

    
        self.add_side_image(Framebutton, x=800, y=50)

    def create_rounded_button(self, width, height, radius, color):
        """Create a rounded button image with the specified color."""
        image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        draw.rounded_rectangle((0, 0, width, height), radius=radius, fill=color)
        return ImageTk.PhotoImage(image)

    def add_side_image(self, parent, x, y):
        """Add an image to the right side of the buttons."""
        try:
            img = Image.open("download.jpeg").resize((600, 300)) 
            img = ImageTk.PhotoImage(img)
            side_image_label = Label(parent, image=img, bg="white")
            side_image_label.image = img 
            side_image_label.place(x=x, y=y) 
        except FileNotFoundError:
            print("Image file not found. Please check the path.")

    def open_return_window(self):
        self.root.destroy()
        return_window = Tk()
        RtnBook.ReturnBook(return_window)
        return_window.mainloop()

    def open_borrow_book_window(self):
        self.root.destroy()
        borrow_window = Tk()
        BorrowClass.Libs(borrow_window)
        borrow_window.mainloop()

    def show_user_history(self):
        self.root.destroy()
        history_window = Tk()
        HistoryClass.History(history_window)
        history_window.mainloop()

    def back(self):
        self.root.destroy()
        login_window = Tk()
        LIB.InitialMenu(login_window)
        login_window.mainloop()

if __name__ == "__main__":
    root = Tk()
    UserPanel(root)
    root.mainloop()
