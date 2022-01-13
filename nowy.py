import main
from tkinter import *

root = Tk()
root.geometry("400x400")

def rejestracja():
    if n_mieszkania.get().find("/") == -1:
        numer_budynku = n_mieszkania.get()
        numer_mieszkania = "NULL"
    main.cursor.execute("INSERT INTO adresy VALUES ('{}', '{}', '{}', {}, {}, {}, {})"
                        .format(email.get(), miasto.get(), ulica.get(), numer_budynku, numer_mieszkania, kod.get(),telefon.get()))
    main.connection.commit()


    email.delete(0, END)
    imie.delete(0, END)
    nazwisko.delete(0, END)
    miasto.delete(0, END)
    ulica.delete(0, END)
    n_mieszkania.delete(0, END)
    kod.delete(0, END)
    telefon.delete(0, END)


#okienka do rejestracji
email = Entry(root, width = 30)
email.grid(row =0, column = 1, padx = 20)
imie = Entry(root, width = 30)
imie.grid(row =1, column = 1, padx = 20, pady = 10)
nazwisko = Entry(root, width = 30)
nazwisko.grid(row =2, column = 1, padx = 20, pady = 10)
miasto = Entry(root, width = 30)
miasto.grid(row =3, column = 1, padx = 20, pady = 10)
ulica = Entry(root, width = 30)
ulica.grid(row =4, column = 1, padx = 20, pady = 10)
n_mieszkania = Entry(root, width = 30)
n_mieszkania.grid(row =5, column = 1, padx = 20, pady = 10)
kod = Entry(root, width = 30)
kod.grid(row =6, column = 1, padx = 20, pady = 10)
telefon = Entry(root, width = 30)
telefon.grid(row =7, column = 1, padx = 20, pady = 10)

email_label = Label(root, text = "Adres email")
email_label.grid(row = 0, column = 0)
email_label = Label(root, text = "Imię")
email_label.grid(row = 1, column = 0)
email_label = Label(root, text = "Nazwisko")
email_label.grid(row = 2, column = 0)
email_label = Label(root, text = "Miasto")
email_label.grid(row = 3, column = 0)
email_label = Label(root, text = "Ulica")
email_label.grid(row = 4, column = 0)
email_label = Label(root, text = "Numer domu/Numer mieszkania")
email_label.grid(row = 5, column = 0)
email_label = Label(root, text = "Kod pocztowy")
email_label.grid(row = 6, column = 0)
email_label = Label(root, text = "Telefon")
email_label.grid(row = 7, column = 0)

rejestr_button = Button(root, text = "Zarejestruj się", command = rejestracja)
rejestr_button.grid(row = 8, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

root.mainloop()