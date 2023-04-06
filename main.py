from tkinter import *
from PIL import ImageTk, Image
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
    logo = ImageTk.PhotoImage(Image.open("logo.png"))

    # Add elements
    head = Label(root, text=" Adress Book", font=("Arial",20))
    logo_label= Label(root, image=logo)
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
    phone_number_entry = Entry(root)

    submit_btn=Button(root, text="Submit")
    clear_btn=Button(root, text="Clear")

    # Element Position

    head.grid(row=0, columnspan=2)
    logo_label.grid(row=1, columnspan=2)
    name_label.grid(row=2, column=0)
    name_entry.grid(row=2, column=1)
    second_name_label.grid(row=3, column=0)
    second_name_entry.grid(row=3, column=1)
    surname_label.grid(row=4, column=0)
    surname_entry.grid(row=4, column=1)
    street_label.grid(row=5, column=0)
    street_entry.grid(row=5, column=1)
    home_number_label.grid(row=6, column=0)
    home_number_entry.grid(row=6, column=1)
    city_label.grid(row=7, column=0)
    city_entry.grid(row=7, column=1)
    zipcode_label.grid(row=8, column=0)
    zipcode_entry.grid(row=8, column=1)
    adress_email_label.grid(row=9, column=0)
    adress_email_entry.grid(row=9, column=1)
    phone_number_label.grid(row=10, column=0)
    phone_number_entry.grid(row=10, column=1)

    submit_btn.grid(row=11, column=0)
    clear_btn.grid(row=11, column=1)









    root.mainloop()
if __name__ == '__main__':
    main()