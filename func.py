import sqlite3
from tkinter import *

def query(root):
    global print_records
    conn = sqlite3.connect('addresses.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print_records = ""
    for record in records:
        print_records += str(record[0])+" "+str(record[2])+" "+str(record[len(record)-1])+"\n"
    quary_label = Label(root, text=print_records)
    quary_label.grid(row=16, columnspan=2)
    conn.commit()
    conn.close()

def delete(id_entry):
    conn = sqlite3.connect('addresses.db')
    c = conn.cursor()
    c.execute("DELETE from addresses WHERE oid="+id_entry.get())
    id_entry.delete(0,END)
    conn.commit()
    conn.close()

def save(id_entry):
    conn = sqlite3.connect('addresses.db')
    c = conn.cursor()
    record_id = id_entry.get()
    c.execute("""UPDATE addresses SET
    name=:name,
    second_name=:second_name,
    surname=:surname,
    street=:street,
    home_number=:home_number,
    city=:city,
    zipcode=:zipcode,
    adress_email=:adress_email,
    phone_number=:phone_number
    WHERE oid=:oid""",
        {'name': name_entry_editor.get(),
         'second_name': second_name_entry_editor.get(),
         'surname': surname_entry_editor.get(),
         'street': street_entry_editor.get(),
         'home_number': home_number_entry_editor.get(),
         'city': city_entry_editor.get(),
         'zipcode': zipcode_entry_editor.get(),
         'adress_email': adress_email_entry_editor.get(),
         'phone_number': phone_number_entry_editor.get(),
         'oid': record_id
        })

    conn.commit()
    conn.close()
    editor.destroy()

def edit(id_entry):
    global editor
    global save
    global name_entry_editor
    global second_name_entry_editor
    global surname_entry_editor
    global street_entry_editor
    global home_number_entry_editor
    global city_entry_editor
    global zipcode_entry_editor
    global adress_email_entry_editor
    global phone_number_entry_editor
    editor= Tk()
    editor.title="Update"
    editor.geometry('')

    conn = sqlite3.connect('addresses.db')
    c = conn.cursor()
    record_id = id_entry.get()
    c.execute("SELECT * FROM addresses WHERE oid="+record_id)
    records=c.fetchall()

    # Add elements
    name_label_editor = Label(editor, text="Imie")
    name_entry_editor = Entry(editor)
    second_name_label_editor = Label(editor, text="Drugie Imie")
    second_name_entry_editor = Entry(editor)
    surname_label_editor = Label(editor, text="Nazwisko")
    surname_entry_editor = Entry(editor)
    street_label_editor = Label(editor, text="Ulica")
    street_entry_editor = Entry(editor)
    home_number_label_editor = Label(editor, text="Numer Mieszkania")
    home_number_entry_editor = Entry(editor)
    city_label_editor = Label(editor, text="Miasto")
    city_entry_editor = Entry(editor)
    zipcode_label_editor = Label(editor, text="Kod Pocztowy")
    zipcode_entry_editor = Entry(editor)
    adress_email_label_editor = Label(editor, text="Adres Email")
    adress_email_entry_editor = Entry(editor)
    phone_number_label_editor = Label(editor, text="Numer Telefonu")
    phone_number_entry_editor = Entry(editor)
    save_btn= Button(editor, text="Save", width=40, command=lambda:save(id_entry))

    # Element Position
    name_label_editor.grid(row=1, column=0)
    name_entry_editor.grid(row=1, column=1)
    second_name_label_editor.grid(row=2, column=0)
    second_name_entry_editor.grid(row=2, column=1)
    surname_label_editor.grid(row=3, column=0)
    surname_entry_editor.grid(row=3, column=1)
    street_label_editor.grid(row=4, column=0)
    street_entry_editor.grid(row=4, column=1)
    home_number_label_editor.grid(row=5, column=0)
    home_number_entry_editor.grid(row=5, column=1)
    city_label_editor.grid(row=6, column=0)
    city_entry_editor.grid(row=6, column=1)
    zipcode_label_editor.grid(row=7, column=0)
    zipcode_entry_editor.grid(row=7, column=1)
    adress_email_label_editor.grid(row=8, column=0)
    adress_email_entry_editor.grid(row=8, column=1)
    phone_number_label_editor.grid(row=9, column=0)
    phone_number_entry_editor.grid(row=9, column=1)
    save_btn.grid(row=10, columnspan=2)

    for record in records:
        name_entry_editor.insert(0,record[0])
        second_name_entry_editor.insert(0,record[1])
        surname_entry_editor.insert(0,record[2])
        street_entry_editor.insert(0,record[3])
        home_number_entry_editor.insert(0,record[4])
        city_entry_editor.insert(0,record[5])
        zipcode_entry_editor.insert(0,record[6])
        adress_email_entry_editor.insert(0,record[7])
        phone_number_entry_editor.insert(0,record[8])

    conn.commit()
    conn.close()

def submit(name_entry,second_name_entry,surname_entry,street_entry,home_number_entry,city_entry,zipcode_entry,adress_email_entry,phone_number_entry):
    conn = sqlite3.connect('addresses.db')
    c = conn.cursor()
    c.execute("INSERT INTO addresses VALUES(:name, :second_name, :surname, :street, :home_number, :city, :zipcode, :adress_email, :phone_number)",
              {'name': name_entry.get(),
               'second_name': second_name_entry.get(),
               'surname': surname_entry.get(),
               'street': street_entry.get(),
               'home_number': home_number_entry.get(),
               'city': city_entry.get(),
               'zipcode': zipcode_entry.get(),
               'adress_email': adress_email_entry.get(),
               'phone_number': phone_number_entry.get()
               })
    conn.commit()
    conn.close()
def clear(name_entry,second_name_entry,surname_entry,street_entry,home_number_entry,city_entry,zipcode_entry,adress_email_entry,phone_number_entry):
    name_entry.delete(0, END)
    second_name_entry.delete(0, END)
    surname_entry.delete(0, END)
    street_entry.delete(0, END)
    home_number_entry.delete(0, END)
    city_entry.delete(0, END)
    zipcode_entry.delete(0, END)
    adress_email_entry.delete(0, END)
    phone_number_entry.delete(0, END)
