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

        self.btn_generate = CTk.CTkButton(master=self.password_frame, text="Generate", width=100,
                                          command=self.set_password)
        self.btn_generate.grid(row=0, column=1)

        self.setting_frame = CTk.CTkFrame(master=self)
        self.setting_frame.grid(row=2, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.password_length_slider = CTk.CTkSlider(master=self.setting_frame, from_=0, to=100, number_of_steps=100,
                                                    command=self.slider_event)
        self.password_length_slider.grid(row=1, column=0, columnspan=3, pady=(20, 20), sticky="ew")

        self.password_length_entry = CTk.CTkEntry(master=self.setting_frame, width=50)
        self.password_length_entry.grid(row=1, column=3, padx=(20, 10), sticky="we")

        self.cb_digits_var = tkinter.StringVar()
        self.cb_digits = CTk.CTkCheckBox(master=self.setting_frame, text="0-9", variable=self.cb_digits_var,
                                         onvalue=digits, offvalue="")
        self.cb_digits.grid(row=2, column=0, padx=10)

        self.cb_lower_var = tkinter.StringVar()
        self.cb_lower = CTk.CTkCheckBox(master=self.setting_frame, text="a-z", variable=self.cb_lower_var,
                                        onvalue=ascii_lowercase, offvalue="")
        self.cb_lower.grid(row=2, column=1)

        self.cb_upper_var = tkinter.StringVar()
        self.cb_upper = CTk.CTkCheckBox(master=self.setting_frame, text="A-Z", variable=self.cb_upper_var,
                                        onvalue=ascii_uppercase, offvalue="")
        self.cb_upper.grid(row=2, column=2)

        self.cb_symbol_var = tkinter.StringVar()
        self.cb_symbol = CTk.CTkCheckBox(master=self.setting_frame, text=("@#$%"), variable=self.cb_symbol_var,
                                         onvalue=punctuation, offvalue="")

        self.cb_symbol.grid(row=2, column=3)

        self.appearance_mode_option_menu = CTk.CTkOptionMenu(master=self.setting_frame,
                                                             values=["Light", "Dark", "System"],
                                                             command=self.change_appearance_mode_event)
        self.appearance_mode_option_menu.grid(row=3, column=0, columnspan=4, pady=(10, 10))

    def change_appearance_mode_event(self, new_appearance_mode):
        CTk.set_appearance_mode(new_appearance_mode)

    def slider_event(self, value):
        self.password_length_entry.delete(0, "end")
        self.password_length_entry.insert(0,int(value))

    def get_characters(self):
        chars = "".join(self.cb_digits_var.get() + self.cb_lower_var.get() + self.cb_upper_var.get() +
                       self.cb_symbol_var.get())
        return chars
    def set_password(self):
        pass
if __name__ =="__main__":
    app = App()
    app.mainloop()


