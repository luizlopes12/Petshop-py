from tkinter import *
from tkinter import ttk
import subprocess


def services():
    from PIL import Image, ImageTk

    root = Tk()

    root.title("Petshop Dog's")
    root.config(background='#FFFFFF')
    root.resizable(False, False)
    root.maxsize(width=1280, height=720)
    root.minsize(width=1280, height=720)
    # Menu - Navbar

    photo = PhotoImage(file="assets\\window_icon.png")
    root.iconphoto(False, photo)

    def open_home():
        root.destroy()
        subprocess.run(["python", "main.py"])

    def open_signup():
        root.destroy()
        subprocess.run(["python", "signup.py"])

    def open_animal_register():
        root.destroy()
        subprocess.run(["python", "animalRegister.py"])

    def open_services():
        root.destroy()
        subprocess.run(["python", "services.py"])

    def open_login():
        root.destroy()
        subprocess.run(["python", "login.py"])

    font_default = "Inter 13 bold"
    # home_option
    home_option__navbar = Button(
        root, text="Home", font=font_default, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=open_home)
    home_option__navbar.grid(row=0, column=0)

    # signup_option
    signup_option__navbar = Button(
        root, text="Client Register", font=font_default, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=open_signup)
    signup_option__navbar.grid(row=0, column=1)

    # animal_rgister_option
    animal_register_option__navbar = Button(
        root, text="Animal register", font=font_default, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=open_animal_register)
    animal_register_option__navbar.grid(row=0, column=2)

    # services_option
    services_option__navbar = Button(
        root, text="Services", font=font_default, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=open_services)
    services_option__navbar.grid(row=0, column=3)

    # login_option
    login_option__navbar = Button(
        root, text="Login", font=font_default, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=open_login)
    login_option__navbar.grid(row=0, column=4)

    # Container - Form
    containerForm = Frame(root, width=500, height=500)
    containerForm.place(x=450, y=130)

    # Title
    title_page = Label(root, text="Services",
                       font="Inter 25 bold")
    title_page.place(x=635, y=155)

    # Purple - Circle
    circle_img = Image.open('assets\\circle_home.png')
    circle_convert = ImageTk.PhotoImage(circle_img)
    lbl_image = Label(root, image=circle_convert, bg="#FFFFFF")
    lbl_image.place(x=980, y=-80)

    # Orange - Circle
    orange_image = Image.open('assets\\orange_circle.png')
    orange_convert_tk = ImageTk.PhotoImage(orange_image)
    lbl_image = Label(root, image=orange_convert_tk, bg="#FFFFFF")
    lbl_image.place(x=320, y=120)

    # Turquoise - Circle
    turquoise_image = Image.open('assets\\turquoise_circle.png')
    turquoise_convert_tk = ImageTk.PhotoImage(turquoise_image)
    lbl_image = Label(root, image=turquoise_convert_tk, bg="#FFFFFF")
    lbl_image.place(x=1000, y=550)

    # Form

    # Code

    codeEntry = Entry(root, width=55, bg="white")
    codeEntry.place(x=550, y=290)
    codeLabel = Label(root, text="Code: ", font="Inter 10 bold",)
    codeLabel.place(x=495, y=287)

    # Name
    nameEntry = Entry(root, width=55, bg="white")
    nameEntry.place(x=550, y=320)
    nameLabel = Label(root, text="Name: ", font="Inter 10 bold",)
    nameLabel.place(x=495, y=317)

    # Services
    serviceBox = ttk.Combobox(root, values=["Health", "Education", "Dog Bath"])
    serviceBox.place(x=550, y=350)
    serviceLabel = Label(root, text="Service type: ", font="Inter 10 bold",)
    serviceLabel.place(x=455, y=347)

    # Value
    valueEntry = Entry(root, width=55, bg="white")
    valueEntry.place(x=550, y=380)
    valueLabel = Label(root, text="Value: ", font="Inter 10 bold",)
    valueLabel.place(x=495, y=377)

    # Description
    descriptionEntry = Entry(root, width=55, bg="white")
    descriptionEntry.place(x=550, y=410)
    descriptionLabel = Label(root, text="Description: ", font="Inter 10 bold",)
    descriptionLabel.place(x=460, y=407)

    # Duration
    durationEntry = Entry(root, width=55, bg="white")
    durationEntry.place(x=550, y=440)
    durationLabel = Label(root, text="Duration: ", font="Inter 10 bold",)
    durationLabel.place(x=475, y=437)

    # Button
    btnSignUp = Button(root, text="Register service",
                       font="Inter 10 bold", fg="white", bg="#8C30F5", border=5, background="#8C30F5", bd=0, width=48)
    btnSignUp.place(x=495, y=475)

    btnDelete = Button(root, text="Delete",
                       font="Inter 10 bold", fg="white", bg="red", border=5, background="red", bd=0, width=48)
    btnDelete.place(x=495, y=505)

    btnUpdate = Button(root, text="Update",
                       font="Inter 10 bold", fg="white", bg="green", border=5, background="green", bd=0, width=48)
    btnUpdate.place(x=495, y=535)

    btnSearch = Button(root, text="Search",
                       font="Inter 10 bold", fg="white", bg="blue", border=5, background="blue", bd=0, width=48)
    btnSearch.place(x=495, y=565)

    root.mainloop()


services()
