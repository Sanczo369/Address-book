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

    root.mainloop()
if __name__ == '__main__':
    main()