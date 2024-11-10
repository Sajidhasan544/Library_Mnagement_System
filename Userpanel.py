from tkinter import *
import BorrowClass  
import HistoryClass  
import LIB  
import BorrowClass
import RtnBook
class UserPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("User Panel")
        self.root.geometry("1530x790+0+0")
        self.root.config(bg="powder blue")

        lbltit = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltit.pack(side=TOP, fill=X)

        Framebutton = Frame(self.root, bd=12, relief="ridge", padx=20, bg="powder blue")
        Framebutton.place(x=0, y=130, width=1530, height=400)


        self.borrow_button = Button(Framebutton, text="Borrow Book", font=("arial", 20, "bold"), width=20, bg="light green", command=self.open_borrow_book_window)
        self.borrow_button.grid(row=0, column=0, padx=20, pady=20)
        
        
        btnReturn = Button(Framebutton, text="Return a Book", font=("times new roman", 20, "bold"), bg="light green", command=self.open_return_window)
        btnReturn.place(x=1000, y=150, width=400, height=100)
        

        self.history_button = Button(Framebutton, text="Show My History", font=("arial", 20, "bold"), width=20, bg="light green", command=self.show_user_history)
        self.history_button.grid(row=0, column=1, padx=20, pady=20)

        btnExit = Button(Framebutton, text="Back", font=("arial", 12, "bold"), width=25, bg="light green", command=self.back)
        btnExit.grid(row=4, column=0)
        
        
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
        HistoryClass.UserHistoryWindow(history_window)
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
