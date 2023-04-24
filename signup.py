from tkinter import *
import subprocess


def signUp():

    root = Tk()

    root.title("Petshop Dog's")
    root.config(background='#FFFFFF')
    root.resizable(False, False)
    root.maxsize(width=1280, height=720)
    root.minsize(width=1280, height=720)

    from PIL import Image, ImageTk
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

    ####

    # Container - Form
    containerForm = Frame(root, width=500, height=580)
    containerForm.place(x=450, y=130)

    # Title
    title_page = Label(root, text="Client Register",
                       font="Inter 25 bold")
    title_page.place(x=600, y=155)

    # Purple - Circle
    circle_image_signup = Image.open('assets\\circle_home.png')
    circle_convert_signup = ImageTk.PhotoImage(circle_image_signup)
    lbl_image_signup = Label(root, image=circle_convert_signup, bg="#FFFFFF")
    lbl_image_signup.place(x=980, y=-80)

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
    userEntry = Entry(root, width=55, bg="white")
    userEntry.place(x=550, y=320)
    userLabel = Label(root, text="Name: ", font="Inter 10 bold",)
    userLabel.place(x=495, y=317)

    # CPF
    cpfEntry = Entry(root, width=55, bg="white")
    cpfEntry.place(x=550, y=350)
    cpfLabel = Label(root, text="CPF: ", font="Inter 10 bold",)
    cpfLabel.place(x=495, y=347)

    # Birth
    birthEntry = Entry(root, width=55, bg="white")
    birthEntry.place(x=550, y=380)
    birthLabel = Label(root, text="Birth: ", font="Inter 10 bold",)
    birthLabel.place(x=495, y=377)

    # Age
    ageEntry = Entry(root, width=55, bg="white")
    ageEntry.place(x=550, y=410)
    ageLabel = Label(root, text="Age: ", font="Inter 10 bold",)
    ageLabel.place(x=495, y=407)

    # Address
    addressEntry = Entry(root, width=55, bg="white")
    addressEntry.place(x=550, y=440)
    addressLabel = Label(root, text="Address: ", font="Inter 10 bold",)
    addressLabel.place(x=475, y=437)

    # Phone
    phoneEntry = Entry(root, width=55, bg="white")
    phoneEntry.place(x=550, y=470)
    phoneLabel = Label(root, text="Phone: ", font="Inter 10 bold",)
    phoneLabel.place(x=495, y=467)

    # Registration date
    registrationDateEntry = Entry(root, width=51, bg="white")
    registrationDateEntry.place(x=575, y=500)
    registrationDateLabel = Label(
        root, text="Registration date: ", font="Inter 10 bold",)
    registrationDateLabel.place(x=450, y=497)

    # Email
    emailEntry = Entry(root, width=55, bg="white")
    emailEntry.place(x=550, y=530)
    emailLabel = Label(root, text="E-mail: ", font="Inter 10 bold",)
    emailLabel.place(x=495, y=527)

    # Password
    passwordEntry = Entry(root, width=52, bg="white")
    passwordEntry.place(x=570, y=560)
    passwordLabel = Label(root, text="Password: ", font="Inter 10 bold",)
    passwordLabel.place(x=495, y=557)

    # Buttons
    btnSignUp = Button(root, text="Register",
                       font="Inter 10 bold", fg="white", bg="#8C30F5", border=5, background="#8C30F5", bd=0, width=48)
    btnSignUp.place(x=495, y=590)

    btnDelete = Button(root, text="Delete",
                       font="Inter 10 bold", fg="white", bg="red", border=5, background="red", bd=0, width=48)
    btnDelete.place(x=495, y=620)

    btnUpdate = Button(root, text="Update",
                       font="Inter 10 bold", fg="white", bg="green", border=5, background="green", bd=0, width=48)
    btnUpdate.place(x=495, y=650)

    btnSearch = Button(root, text="Search",
                       font="Inter 10 bold", fg="white", bg="blue", border=5, background="blue", bd=0, width=48)
    btnSearch.place(x=495, y=680)

    root.mainloop()


signUp()
