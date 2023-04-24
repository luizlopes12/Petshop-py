from tkinter import *
import subprocess
from PIL import Image, ImageTk


def home_init():
    tela = Tk()
    tela.title("Sofisticão Petshop")
    tela.maxsize(width=1280, height=720)
    tela.minsize(width=1280, height=720)
    tela.config(background='#FFFFFF')
    tela.resizable(False, False)
    photo = PhotoImage(file="assets\\favicon.png")
    tela.iconphoto(False, photo)

    def home_open():
        tela.destroy()
        subprocess.run(["python", "index.py"])

    def register_open():
        tela.destroy()
        subprocess.run(["python", "register.py"])

    def animal_register_open():
        tela.destroy()
        subprocess.run(["python", "addPet.py"])

    def services_open():
        tela.destroy()
        subprocess.run(["python", "options.py"])

    def login_open():
        tela.destroy()
        subprocess.run(["python", "login.py"])

    font = "Inter 13 bold"

    home_option = Button(
        tela, text="Home", font=font, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=home_open)
    home_option.grid(row=0, column=0)

    signup_option = Button(
        tela, text="Client Register", font=font, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=register_open)
    signup_option.grid(row=0, column=1)

    animal_register_option = Button(
        tela, text="Animal register", font=font, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=animal_register_open)
    animal_register_option.grid(row=0, column=2)

    services_option = Button(
        tela, text="Services", font=font, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=services_open)
    services_option.grid(row=0, column=3)

    login_option = Button(
        tela, text="Login", font=font, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=login_open)
    login_option.grid(row=0, column=4)

    dog_image_main = Image.open('assets\\home_image.png')
    dog_convert_tk_main = ImageTk.PhotoImage(dog_image_main)
    lbl_image_main = Label(tela, image=dog_convert_tk_main, bg="#FFFFFF")
    lbl_image_main.place(x=750, y=125)

    tela.mainloop()


home_init()
