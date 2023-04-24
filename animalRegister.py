from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import subprocess


def animalRegister():
    root = Tk()

    root.title("Petshop Dog's")
    root.config(background='#FFFFFF')
    root.resizable(False, False)
    root.maxsize(width=1280, height=720)
    root.minsize(width=1280, height=720)

    photo = PhotoImage(file="assets\\window_icon.png")
    root.iconphoto(False, photo)

    # Menu - Navbar

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
    containerForm = Frame(root, width=500, height=585)
    containerForm.place(x=450, y=130)

    # Title
    title_page = Label(root, text="Animal Register",
                       font="Inter 25 bold")
    title_page.place(x=570, y=155)

    # Purple - Circle
    circle_img_animal_register = Image.open('assets\\circle_home.png')
    circle_convert_animal = ImageTk.PhotoImage(circle_img_animal_register)
    lbl_image_animal = Label(root, image=circle_convert_animal, bg="#FFFFFF")
    lbl_image_animal.place(x=980, y=-80)

    # Orange - Circle
    orange_image_animal = Image.open('assets\\orange_circle.png')
    orange_convert_tk_animal = ImageTk.PhotoImage(orange_image_animal)
    lbl_image_animal = Label(
        root, image=orange_convert_tk_animal, bg="#FFFFFF")
    lbl_image_animal.place(x=320, y=120)

    # Turquoise - Circle
    turquoise_image_animal = Image.open('assets\\turquoise_circle.png')
    turquoise_convert_tk_animal = ImageTk.PhotoImage(turquoise_image_animal)
    lbl_image_animal = Label(
        root, image=turquoise_convert_tk_animal, bg="#FFFFFF")
    lbl_image_animal.place(x=1000, y=550)

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

    # Weight
    emailEntry = Entry(root, width=55, bg="white")
    emailEntry.place(x=550, y=350)
    emailLabel = Label(root, text="Weight: ", font="Inter 10 bold",)
    emailLabel.place(x=485, y=347)

    # Age
    passwordEntry = Entry(root, width=55, bg="white")
    passwordEntry.place(x=550, y=380)
    passwordLabel = Label(root, text="Age: ", font="Inter 10 bold",)
    passwordLabel.place(x=495, y=377)

    # Raca
    raceEntry = Entry(root, width=55, bg="white")
    raceEntry.place(x=550, y=410)
    raceLabel = Label(root, text="Race: ", font="Inter 10 bold",)
    raceLabel.place(x=495, y=407)

    # Gender
    genderLabel = Label(root, text="Gender: ", font="Inter 10 bold",)
    genderLabel.place(x=485, y=437)

    gender = StringVar()
    gender.set("M")

    optionMGender = Radiobutton(root, text="M", variable=gender, value="M")
    optionMGender.place(x=550, y=438)

    optionFGender = Radiobutton(root, text="F", variable=gender, value="F")
    optionFGender.place(x=600, y=438)

    # Specie
    specieEntry = Entry(root, width=55, bg="white")
    specieEntry.place(x=550, y=468)
    specieLabel = Label(root, text="Specie: ", font="Inter 10 bold",)
    specieLabel.place(x=485, y=465)

    # Birth
    birthEntry = Entry(root, width=55, bg="white")
    birthEntry.place(x=550, y=498)
    birthLabel = Label(root, text="Birth: ", font="Inter 10 bold",)
    birthLabel.place(x=495, y=495)

    # Update
    updateEntry = Entry(root, width=55, bg="white")
    updateEntry.place(x=551, y=528)
    updateLabel = Label(root, text="Update date: ", font="Inter 10 bold",)
    updateLabel.place(x=460, y=525)

    # Registration Date
    registrationEntry = Entry(root, width=49, bg="white")
    registrationEntry.place(x=583, y=558)
    registrationLabel = Label(
        root, text="Registration date: ", font="Inter 10 bold",)
    registrationLabel.place(x=460, y=555)

    # Description
    descriptionEntry = Entry(root, width=53, bg="white")
    descriptionEntry.place(x=565, y=585)
    descriptionLabel = Label(root, text="Description: ", font="Inter 10 bold",)
    descriptionLabel.place(x=475, y=583)

    # Choose an image

    initial_folder = ""

    def choose_image():
        image_path = filedialog.askopenfilename(initialdir=initial_folder, title="Choose an image", filetypes=(
            ("Arquivos de imagem", "*.jpg;*.jpeg;*.png"), ("Todos os arquivos", "*.*")))

        image_pil = Image.open(image_path)
        widthImage, heightImage = image_pil.size
        if widthImage > 150:
            proportion = widthImage / 150
            new_height = int(widthImage/proportion)
            image_pil = image_pil.resize((110, new_height))
        image_tk = ImageTk.PhotoImage(image_pil)
        lbl_image = Label(root, image=image_tk)
        lbl_image.image = image_tk
        lbl_image.place(x=200, y=250)

    descriptionButton = Button(
        root, text="Choose an image", width=15, height=1, bg="white", command=choose_image)
    descriptionButton.place(x=585, y=610)
    descriptionLabel = Label(
        root, text="Choose an image: ", font="Inter 10 bold",)
    descriptionLabel.place(x=460, y=612)

    # Button
    btnSignUp = Button(root, text="Register Animal",
                       font="Inter 10 bold", fg="white", bg="#8C30F5", border=5, background="#8C30F5", bd=0, width=20)
    btnSignUp.place(x=495, y=650)

    btnDelete = Button(root, text="Delete",
                       font="Inter 10 bold", fg="white", bg="red", border=5, background="red", bd=0, width=20)
    btnDelete.place(x=685, y=650)

    btnUpdate = Button(root, text="Update",
                       font="Inter 10 bold", fg="white", bg="green", border=5, background="green", bd=0, width=20)
    btnUpdate.place(x=495, y=680)

    btnSearch = Button(root, text="Search",
                       font="Inter 10 bold", fg="white", bg="blue", border=5, background="blue", bd=0, width=20)
    btnSearch.place(x=685, y=680)

    root.mainloop()


animalRegister()
