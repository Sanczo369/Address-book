from tkinter import *
def main():
    # root Option
    root = Tk()
    root.title("Address Book")
    root.iconbitmap("icona.ico")

    # Window Menu
    mainMenu = Menu()
    root.config(menu=mainMenu)
    fileMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="File", menu=fileMenu)

    # Add elements
    name_label = Label(root, text="Imie")
    name_entry = Entry(root)
    second_name_label = Label(root, text="Drugie Imie")
    second_name_entry = Entry(root)
    surname_label = Label(root, text="Nazwisko")
    surname_entry = Entry(root)
    street_label = Label(root, text="Ulica")
    street_entry = Entry(root)
    home_number_label = Label(root, text="Numer Mieszkania")
    home_number_entry = Entry(root)
    city_label = Label(root, text="Miasto")
    city_entry = Entry(root)
    zipcode_label = Label(root, text="Kod Pocztowy")
    zipcode_entry = Entry(root)
    adress_email_label = Label(root, text="Adres Email")
    adress_email_entry = Entry(root)
    phone_number_label = Label(root, text="Numer Telefonu")
    phone_number_entry = (root)

    submit_btn=Button(root, text="Submit")
    clear_btn=Button(root, text="Clear")













    root.mainloop()
if __name__ == '__main__':
    main()