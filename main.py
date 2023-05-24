import tkinter
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

import customtkinter as CTk


class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("460x370")
        self.title("PasswordGenerator")
        self.resizable(False, False)




if __name__ =="__main__":
    app = App()
    app.mainloop()


