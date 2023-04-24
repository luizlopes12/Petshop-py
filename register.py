import tkinter as tk
import subprocess
from PIL import Image, ImageTk

def register():
    tela = tk.Tk()
    tela.title("Sofisticão Petshop")
    tela.config(background='#FFFFFF')
    tela.resizable(False, False)
    tela.geometry("1280x720")

    photo = tk.PhotoImage(file="assets\\favicon.png")
    tela.iconphoto(False, photo)

    def open_window(filename):
        tela.destroy()
        subprocess.run(["python", filename])

    def home_open():
        open_window("index.py")

    def register_open():
        open_window("signup.py")

    def animal_register_open():
        open_window("addPet.py")

    def services_open():
        open_window("options.py")

    def login_open():
        open_window("login.py")

    font = "Inter 13 bold"

    home_button = tk.Button(tela, text="Home", font=font, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=home_open)
    home_button.grid(row=0, column=0)

    signup_button = tk.Button(tela, text="Client Register", font=font, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=register_open)
    signup_button.grid(row=0, column=1)

    animal_register_button = tk.Button(tela, text="Animal register", font=font, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=animal_register_open)
    animal_register_button.grid(row=0, column=2)

    services_button = tk.Button(tela, text="Services", font=font, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=services_open)
    services_button.grid(row=0, column=3)

    login_button = tk.Button(tela, text="Login", font=font, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=login_open)
    login_button.grid(row=0, column=4)

    container_form = tk.Frame(tela, width=500, height=580)
    container_form.place(x=450, y=130)

    title = tk.Label(tela, text="Client Register", font="Inter 25 bold")
    title.place(x=600, y=155)

    fields = ["Code", "Name", "CPF", "Birth", "Age", "Address", "Phone", "Register date", "Email", "Password"]
    for i in range(len(fields)):
        Label(tela, text=fields[i] + ": ", font="Inter 10 bold").grid(row=i, column=0, padx=10, pady=10)
        Entry(tela, width=55, bg="white").grid(row=i, column=1, padx=10, pady=10)

    btnSignUp = Button(tela, text="Register", font="Inter 10 bold", fg="white", bg="#8C30F5", border=5, background="#8C30F5", bd=0, width=48)
    btnDelete = Button(tela, text="Delete", font="Inter 10 bold", fg="white", bg="red", border=5, background="red", bd=0, width=48)
    btnUpdate = Button(tela, text="Update", font="Inter 10 bold", fg="white", bg="green", border=5, background="green", bd=0, width=48)
    btnSearch = Button(tela, text="Search", font="Inter 10 bold", fg="white", bg="blue", border=5, background="blue", bd=0, width=48)
    btnSignUp.grid(row=len(fields)+1, column=0, padx=10, pady=10)
    btnDelete.grid(row=len(fields)+1, column=1, padx=10, pady=10)
    btnUpdate.grid(row=len(fields)+1, column=2, padx=10, pady=10)
    btnSearch.grid(row=len(fields)+1, column=3, padx=10, pady=10)

    tela.mainloop()

register()
