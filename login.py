from tkinter import *
import subprocess


def login():

    tela = Tk()

    tela.title("Sofisticão Petshop")
    tela.config(background='#FFFFFF')
    tela.resizable(False, False)
    tela.maxsize(width=1280, height=720)
    tela.minsize(width=1280, height=720)

    from PIL import Image, ImageTk

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

    ####

    containerForm = Frame(tela, width=500, height=500)
    containerForm.place(x=450, y=130)

    title_page = Label(tela, text="Login",
                       font="Inter 25 bold")
    title_page.place(x=635, y=155)

    emailEntry = Entry(tela, width=55, bg="white")
    emailEntry.place(x=550, y=350)
    emailLabel = Label(tela, text="E-mail: ", font="Inter 10 bold",)
    emailLabel.place(x=495, y=347)

    passwordEntry = Entry(tela, width=52, bg="white")
    passwordEntry.place(x=570, y=380)
    passwordLabel = Label(tela, text="Password: ", font="Inter 10 bold",)
    passwordLabel.place(x=495, y=377)

    btnSignUp = Button(tela, text="Login",
                       font="Inter 10 bold", fg="white", bg="#8C30F5", border=5, background="#8C30F5", bd=0, width=48)
    btnSignUp.place(x=495, y=435)

    tela.mainloop()


login()
