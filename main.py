import sqlite3
from tkinter import *
from PIL import ImageTk, Image
import func

def main():
    global root
    global name_entry
    global second_name_entry
    global surname_entry
    global street_entry
    global home_number_entry
    global city_entry
    global zipcode_entry
    global adress_email_entry
    global phone_number_entry
    global id_entry
    # create Table with addresses in addresses.db file
    # conn=sqlite3.connect('address.db')
    # c=conn.cursor()
    # c.execute("""CREATE TABLE addresses (
    # name text,
    # second_name text,
    # surname text,
    # street text,
    # home_number text,
    # city text,
    # zipcode text,
    # adress_email text,
    # phone_number text)""")
    # conn.commit()
    # conn.close()

    # root Option
    root = Tk()
    root.title("Address")
    #root.iconbitmap("icona.ico")
    root.config(padx=3,pady=2)
    logo1 = ImageTk.PhotoImage(Image.open("logo1.png"))
    logo2 = ImageTk.PhotoImage(Image.open("logo2.png"))
    logo3 = ImageTk.PhotoImage(Image.open("logo3.png"))
    logo4 = ImageTk.PhotoImage(Image.open("logo4.png"))
    # Window Menu
    mainMenu = Menu()
    root.config(menu=mainMenu)
    file_menu = Menu(mainMenu)
    mainMenu.add_cascade(label="File", menu=file_menu)
    edit_menu = Menu(mainMenu)
    mainMenu.add_cascade(label="Edit", menu=edit_menu)

    # Add elements
    logo_frame = LabelFrame(root)
    head = Label(logo_frame, text=" Adress Book", font=("Comic Sans MS", 20, "bold"))
    logo0_label= Label(logo_frame, image=logo1)
    logo1_label= Label(logo_frame, image=logo2)
    logo2_label= Label(logo_frame, image=logo3)
    logo3_label= Label(logo_frame, image=logo4)
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
    var=IntVar()
    # Regulamin
    regulamin= Checkbutton(root, text="Akceptuje regulamin", variable=var, onvalue=1, offvalue=0)
    regulamin.deselect()
    submit_btn=Button(root, text="Submit",width=19, command=lambda:func.submit(var,name_entry,second_name_entry,surname_entry,street_entry,home_number_entry,city_entry,zipcode_entry,adress_email_entry,phone_number_entry))
    clear_btn=Button(root, text="Clear",width=19, command=lambda:func.clear(name_entry,second_name_entry,surname_entry,street_entry,home_number_entry,city_entry,zipcode_entry,adress_email_entry,phone_number_entry))
    id_label = Label(root, text="ID:")
    id_entry = Entry(root)
    edit_btn=Button(root, text="Edit",width=19, command=lambda:func.edit(id_entry))
    delete_btn=Button(root, text="Delete",width=19, command=lambda:func.delete(id_entry))
    show_btn=Button(root, text="Show", width=42, command=lambda:func.query(root))


    # Element Position
    logo_frame.grid(row=1, columnspan=2)
    head.grid(row=0, column=2, columnspan=4)
    logo0_label.grid(row=0, column=0)
    logo1_label.grid(row=0, column=1)
    logo2_label.grid(row=0, column=6)
    logo3_label.grid(row=0, column=7)

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
    regulamin.grid(row=11, columnspan=2)

    submit_btn.grid(row=12, column=0)
    clear_btn.grid(row=12, column=1)
    id_label.grid(row=13, column=0)
    id_entry.grid(row=13, column=1)
    edit_btn.grid(row=14, column=0)
    delete_btn.grid(row=14, column=1)
    show_btn.grid(row=15, columnspan=2)

    root.mainloop()
if __name__ == '__main__':
    main()