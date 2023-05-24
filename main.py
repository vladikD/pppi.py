import tkinter
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

import customtkinter as CTk


class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("460x370")
        self.title("PasswordGenerator")
        self.resizable(False, False)

        self.password_frame = CTk.CTkFrame(master=self, fg_color="transparent")
        self.password_frame.grid(row=1, column=0, padx=(20, 20), sticky="nsew")

        self.entry_password = CTk.CTkEntry(master=self.password_frame, width=300)
        self.entry_password.grid(row=0, column=0, padx=(0, 20))
    def set_password(self):
        pass
if __name__ =="__main__":
    app = App()
    app.mainloop()


