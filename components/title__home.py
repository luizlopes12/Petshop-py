from tkinter import *
import subprocess


class TitleHome(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        def open_signup():
            self.destroy()
            subprocess.run(["python", "signup.py"])

        # main title
        main_title = Label(
            self, text="Petshop Dog's", font="Inter 50 bold", fg="#18191F", bg="#FFFFFF", padx=10)
        main_title.grid(row=0, column=0)

        # subtitle
        subtitle = Label(
            self, text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc \n odio in et, lectus sit lorem id integer.", font="Inter 15 bold", fg="#18191F", bg="#FFFFFF", padx=10)
        subtitle.grid(row=2, column=0)

        # button

        def on_enter(e):
            btn['background'] = '#A863F8'

        def on_leave(e):
            btn['background'] = '#8C30F5'

        btn = Button(self, text="Client register",
                     font="Inter 15 bold", fg="white", bg="#8C30F5", border=5, background="#8C30F5", bd=0, width=15, command=open_signup)
        btn.grid(row=3, column=0, pady=50)

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
