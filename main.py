from tkinter import *
import subprocess


def home():

    root = Tk()

    root.title("Petshop Dog's")
    root.config(background='#FFFFFF')
    root.resizable(False, False)
    root.maxsize(width=1280, height=720)
    root.minsize(width=1280, height=720)

    from components.title__home import TitleHome
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

    titleHome = TitleHome(master=root, bg="#FFFFFF")
    titleHome.place(x=5, y=150)

    # Purple - Circle
    circle_image_main = Image.open('assets\\circle_home.png')
    circle_convert_tk_main = ImageTk.PhotoImage(circle_image_main)
    lbl_image_main = Label(root, image=circle_convert_tk_main, bg="#FFFFFF")
    lbl_image_main.place(x=800, y=-80)

    # Orange - Circle
    orange_image_main = Image.open('assets\\orange_circle.png')
    orange_convert_tk_main = ImageTk.PhotoImage(orange_image_main)
    lbl_image_main = Label(root, image=orange_convert_tk_main, bg="#FFFFFF")
    lbl_image_main.place(x=670, y=300)

    # Turquoise - Circle
    turquoise_image_main = Image.open('assets\\turquoise_circle.png')
    turquoise_convert_tk_main = ImageTk.PhotoImage(turquoise_image_main)
    lbl_image_main = Label(root, image=turquoise_convert_tk_main, bg="#FFFFFF")
    lbl_image_main.place(x=885, y=550)

    # Dog - Image
    dog_image_main = Image.open('assets\\dog_home.png')
    dog_convert_tk_main = ImageTk.PhotoImage(dog_image_main)
    lbl_image_main = Label(root, image=dog_convert_tk_main, bg="#FFFFFF")
    lbl_image_main.place(x=750, y=125)

    root.mainloop()


home()
