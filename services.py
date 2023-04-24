from tkinter import *
from tkinter import ttk
import subprocess


def options():
    from PIL import Image, ImageTk
    tela = Tk()
    tela.title("Sofisticão Petshop")
    tela.config(background='#FFFFFF')
    tela.resizable(False, False)
    tela.maxsize(width=1280, height=720)
    tela.minsize(width=1280, height=720)

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

    containerForm = Frame(tela, width=500, height=500)
    containerForm.place(x=450, y=130)

    title_page = Label(tela, text="Services",
                       font="Inter 25 bold")
    title_page.place(x=635, y=155)

    codeEntry = Entry(tela, width=55, bg="white")
    codeEntry.place(x=550, y=290)
    codeLabel = Label(tela, text="Code: ", font="Inter 10 bold",)
    codeLabel.place(x=495, y=287)

    nameEntry = Entry(tela, width=55, bg="white")
    nameEntry.place(x=550, y=320)
    nameLabel = Label(tela, text="Name: ", font="Inter 10 bold",)
    nameLabel.place(x=495, y=317)

    serviceBox = ttk.Combobox(tela, values=["Health", "Education", "Dog Bath"])
    serviceBox.place(x=550, y=350)
    serviceLabel = Label(tela, text="Service type: ", font="Inter 10 bold",)
    serviceLabel.place(x=455, y=347)

    valueEntry = Entry(tela, width=55, bg="white")
    valueEntry.place(x=550, y=380)
    valueLabel = Label(tela, text="Value: ", font="Inter 10 bold",)
    valueLabel.place(x=495, y=377)

    descriptionEntry = Entry(tela, width=55, bg="white")
    descriptionEntry.place(x=550, y=410)
    descriptionLabel = Label(tela, text="Description: ", font="Inter 10 bold",)
    descriptionLabel.place(x=460, y=407)

    durationEntry = Entry(tela, width=55, bg="white")
    durationEntry.place(x=550, y=440)
    durationLabel = Label(tela, text="Duration: ", font="Inter 10 bold",)
    durationLabel.place(x=475, y=437)

    btnSignUp = Button(tela, text="Register service",
                       font="Inter 10 bold", fg="white", bg="#8C30F5", border=5, background="#8C30F5", bd=0, width=48)
    btnSignUp.place(x=495, y=475)

    btnDelete = Button(tela, text="Delete",
                       font="Inter 10 bold", fg="white", bg="red", border=5, background="red", bd=0, width=48)
    btnDelete.place(x=495, y=505)

    btnUpdate = Button(tela, text="Update",
                       font="Inter 10 bold", fg="white", bg="green", border=5, background="green", bd=0, width=48)
    btnUpdate.place(x=495, y=535)

    btnSearch = Button(tela, text="Search",
                       font="Inter 10 bold", fg="white", bg="blue", border=5, background="blue", bd=0, width=48)
    btnSearch.place(x=495, y=565)

    tela.mainloop()


options()
