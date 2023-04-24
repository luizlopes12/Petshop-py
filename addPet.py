from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import subprocess


def addPet():
    tela = Tk()

    tela.config(background='#FFFFFF')
    tela.resizable(False, False)
    tela.maxsize(width=1280, height=720)
    tela.minsize(width=1280, height=720)

    favicon = PhotoImage(file="assets\\favicon.png")
    tela.iconphoto(False, favicon)

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

    containerForm = Frame(tela, width=500, height=585)
    containerForm.place(x=450, y=130)

    title_page = Label(tela, text="Animal Register",
                       font="Inter 25 bold")
    title_page.place(x=570, y=155)

    codeEntry = Entry(tela, width=55, bg="white")
    codeEntry.place(x=550, y=290)
    codeLabel = Label(tela, text="Code: ", font="Inter 10 bold",)
    codeLabel.place(x=495, y=287)

    userEntry = Entry(tela, width=55, bg="white")
    userEntry.place(x=550, y=320)
    userLabel = Label(tela, text="Name: ", font="Inter 10 bold",)
    userLabel.place(x=495, y=317)

    emailEntry = Entry(tela, width=55, bg="white")
    emailEntry.place(x=550, y=350)
    emailLabel = Label(tela, text="Weight: ", font="Inter 10 bold",)
    emailLabel.place(x=485, y=347)

    passwordEntry = Entry(tela, width=55, bg="white")
    passwordEntry.place(x=550, y=380)
    passwordLabel = Label(tela, text="Age: ", font="Inter 10 bold",)
    passwordLabel.place(x=495, y=377)

    raceEntry = Entry(tela, width=55, bg="white")
    raceEntry.place(x=550, y=410)
    raceLabel = Label(tela, text="Race: ", font="Inter 10 bold",)
    raceLabel.place(x=495, y=407)

    genderLabel = Label(tela, text="Gender: ", font="Inter 10 bold",)
    genderLabel.place(x=485, y=437)

    gender = StringVar()
    gender.set("M")

    optionMGender = Radiobutton(tela, text="M", variable=gender, value="M")
    optionMGender.place(x=550, y=438)

    optionFGender = Radiobutton(tela, text="F", variable=gender, value="F")
    optionFGender.place(x=600, y=438)

    specieEntry = Entry(tela, width=55, bg="white")
    specieEntry.place(x=550, y=468)
    specieLabel = Label(tela, text="Specie: ", font="Inter 10 bold",)
    specieLabel.place(x=485, y=465)

    birthEntry = Entry(tela, width=55, bg="white")
    birthEntry.place(x=550, y=498)
    birthLabel = Label(tela, text="Birth: ", font="Inter 10 bold",)
    birthLabel.place(x=495, y=495)

    updateEntry = Entry(tela, width=55, bg="white")
    updateEntry.place(x=551, y=528)
    updateLabel = Label(tela, text="Update date: ", font="Inter 10 bold",)
    updateLabel.place(x=460, y=525)

    registrationEntry = Entry(tela, width=49, bg="white")
    registrationEntry.place(x=583, y=558)
    registrationLabel = Label(
        tela, text="Registration date: ", font="Inter 10 bold",)
    registrationLabel.place(x=460, y=555)

    descriptionEntry = Entry(tela, width=53, bg="white")
    descriptionEntry.place(x=565, y=585)
    descriptionLabel = Label(tela, text="Description: ", font="Inter 10 bold",)
    descriptionLabel.place(x=475, y=583)

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
        lbl_image = Label(tela, image=image_tk)
        lbl_image.image = image_tk
        lbl_image.place(x=200, y=250)

    descriptionButton = Button(
        tela, text="Choose an image", width=15, height=1, bg="white", command=choose_image)
    descriptionButton.place(x=585, y=610)
    descriptionLabel = Label(
        tela, text="Choose an image: ", font="Inter 10 bold",)
    descriptionLabel.place(x=460, y=612)

    btnSignUp = Button(tela, text="Register Animal",
                       font="Inter 10 bold", fg="white", bg="#8C30F5", border=5, background="#8C30F5", bd=0, width=20)
    btnSignUp.place(x=495, y=650)

    btnDelete = Button(tela, text="Delete",
                       font="Inter 10 bold", fg="white", bg="red", border=5, background="red", bd=0, width=20)
    btnDelete.place(x=685, y=650)

    btnUpdate = Button(tela, text="Update",
                       font="Inter 10 bold", fg="white", bg="green", border=5, background="green", bd=0, width=20)
    btnUpdate.place(x=495, y=680)

    btnSearch = Button(tela, text="Search",
                       font="Inter 10 bold", fg="white", bg="blue", border=5, background="blue", bd=0, width=20)
    btnSearch.place(x=685, y=680)

    tela.mainloop()


addPet()
