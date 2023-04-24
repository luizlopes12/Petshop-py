import tkinter as tk
import subprocess
from PIL import Image, ImageTk

def register():
    root = tk.Tk()
    root.title("Sofisticão Petshop")
    root.config(background='#FFFFFF')
    root.resizable(False, False)
    root.geometry("1280x720")

    photo = tk.PhotoImage(file="assets\\window_icon.png")
    root.iconphoto(False, photo)

    def open_window(filename):
        root.destroy()
        subprocess.run(["python", filename])

    def open_home():
        open_window("index.py")

    def open_signup():
        open_window("signup.py")

    def open_animal_register():
        open_window("addPet.py")

    def open_services():
        open_window("options.py")

    def open_login():
        open_window("login.py")

    font = "Inter 13 bold"

    home_button = tk.Button(root, text="Home", font=font, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=open_home)
    home_button.grid(row=0, column=0)

    signup_button = tk.Button(root, text="Client Register", font=font, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=open_signup)
    signup_button.grid(row=0, column=1)

    animal_register_button = tk.Button(root, text="Animal register", font=font, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=open_animal_register)
    animal_register_button.grid(row=0, column=2)

    services_button = tk.Button(root, text="Services", font=font, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=open_services)
    services_button.grid(row=0, column=3)

    login_button = tk.Button(root, text="Login", font=font, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=open_login)
    login_button.grid(row=0, column=4)

    container_form = tk.Frame(root, width=500, height=580)
    container_form.place(x=450, y=130)

    title = tk.Label(root, text="Client Register", font="Inter 25 bold")
    title.place(x=600, y=155)

    circle_image = Image.open('assets\\circle_home.png')
    circle_tk = ImageTk.PhotoImage(circle_image)
    circle_label = tk.Label(root, image=circle_tk, bg="#FFFFFF")
    circle_label.place(x=980, y=-80)

    orange_image = Image.open('assets\\orange_circle.png')
    orange_tk = ImageTk.PhotoImage(orange_image)
    orange_label = tk.Label(root, image=orange_tk, bg="#FFFFFF")
    orange_label.place(x=320, y=120)

    turquoise_image = Image.open('assets\\turquoise_circle.png')
    turquoise_tk = ImageTk.PhotoImage(turquoise_image)
    turquoise_label = tk.Label(root, image=turquoise_tk, bg="#FFFFFF")
    turquoise_label.place(x=1000, y=550)

    fields = ["Code", "Name", "CPF", "Birth", "Age", "Address", "Phone", "Register date", "Email", "Password"]
    for i in range(len(fields)):
        Label(root, text=fields[i] + ": ", font="Inter 10 bold").grid(row=i, column=0, padx=10, pady=10)
        Entry(root, width=55, bg="white").grid(row=i, column=1, padx=10, pady=10)

    btnSignUp = Button(root, text="Register", font="Inter 10 bold", fg="white", bg="#8C30F5", border=5, background="#8C30F5", bd=0, width=48)
    btnDelete = Button(root, text="Delete", font="Inter 10 bold", fg="white", bg="red", border=5, background="red", bd=0, width=48)
    btnUpdate = Button(root, text="Update", font="Inter 10 bold", fg="white", bg="green", border=5, background="green", bd=0, width=48)
    btnSearch = Button(root, text="Search", font="Inter 10 bold", fg="white", bg="blue", border=5, background="blue", bd=0, width=48)
    btnSignUp.grid(row=len(fields)+1, column=0, padx=10, pady=10)
    btnDelete.grid(row=len(fields)+1, column=1, padx=10, pady=10)
    btnUpdate.grid(row=len(fields)+1, column=2, padx=10, pady=10)
    btnSearch.grid(row=len(fields)+1, column=3, padx=10, pady=10)

    root.mainloop()

register()
