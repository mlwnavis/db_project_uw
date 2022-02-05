import main
from tkinter import *
import re
from tkinter import messagebox
from tkinter import ttk
root = Tk()
style = ttk.Style()
style.configure("Courier.TButton", font=("Courier", 10))

def check_rejestracja(mail, password, city, street, number, postal, tel):
    email ='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    haslo = ''
    miasto = '^([A-ZŚŹŻŁ]{1}[a-ząćęłńóśźż]{1,})$'
    ulica = '^([A-ZŚŹŻŁ]{1}[a-ząćęłńóśźż]{2,})$'
    adres = '^([1-9]{1,2})+[/]?([1-9]{1,2})$'
    kod = '^[0-9]{2}-[0-9]{3}$'
    tele = '^[1-9][0-9]{8}$'

    if not re.search(email, mail):
        return "adres email"
    elif not re.search(haslo, password):
        return "haslo"
    elif not re.search(miasto, city):
        return "miasto"
    elif not re.search(ulica, street):
        return "ulicę"
    elif not re.search(adres, number):
        return "numer budynku"
    elif not re.search(kod, postal):
        return "kod pocztowy"
    elif not re.search(tele, tel):
        return "telefon"
    else:
        return True


def rejestracja():
    mail = email.get()
    password = haslo.get()
    city = str(miasto.get()).capitalize()
    street = str(ulica.get()).capitalize()
    number = n_mieszkania.get()
    postal = str(kod.get())
    tel = telefon.get()
    check = check_rejestracja(mail, password, city, street, number, postal, tel)
    if check is True:
        if number.find("/") == -1:
            numer_budynku = number
            numer_mieszkania = "NULL"

        else:
            numer = number.split("/")
            numer_budynku = numer[0]
            numer_mieszkania = numer[1]
        main.cursor.execute("INSERT INTO klienci(email, haslo, saldo) VALUES ('{}', '{}', '{}')"
                            .format(mail, password, 0))
        main.cursor.execute("UPDATE adresy SET imie='{}', nazwisko='{}', miasto='{}', "
                            "ulica='{}', numer_budynku={}, numer_mieszkania={}, kod_pocztowy='{}', telefon={}"
                            "WHERE email='{}'"
                            .format(imie.get(), nazwisko.get(), city, street, numer_budynku, numer_mieszkania, postal, tel, mail))
        main.connection.commit()

        email.delete(0, END)
        haslo.delete(0, END)
        imie.delete(0, END)
        nazwisko.delete(0, END)
        miasto.delete(0, END)
        ulica.delete(0, END)
        n_mieszkania.delete(0, END)
        kod.delete(0, END)
        telefon.delete(0, END)
        messagebox.showinfo("", "Założono konto.")
    else:
        messagebox.showerror("", "Niepoprawnie wprowadzono {}.".format(check))


# okienka do rejestracji
email = Entry(root, width = 30)
email.grid(row =0, column = 1, padx = 20)
haslo = Entry(root, width = 30)
haslo.grid(row =1, column = 1, padx = 20, pady = 10)
imie = Entry(root, width = 30)
imie.grid(row =2, column = 1, padx = 20, pady = 10)
nazwisko = Entry(root, width = 30)
nazwisko.grid(row =3, column = 1, padx = 20, pady = 10)
miasto = Entry(root, width = 30)
miasto.grid(row =4, column = 1, padx = 20, pady = 10)
ulica = Entry(root, width = 30)
ulica.grid(row =5, column = 1, padx = 20, pady = 10)
n_mieszkania = Entry(root, width = 30)
n_mieszkania.grid(row =6, column = 1, padx = 20, pady = 10)
kod = Entry(root, width = 30)
kod.grid(row =7, column = 1, padx = 20, pady = 10)
telefon = Entry(root, width = 30)
telefon.grid(row =8, column = 1, padx = 20, pady = 10)



email_label = Label(root, text = "Adres email")
email_label.grid(row = 0, column = 0)
email_label = Label(root, text = "Haslo")
email_label.grid(row = 1, column = 0)
email_label = Label(root, text = "Imię")
email_label.grid(row = 2, column = 0)
email_label = Label(root, text = "Nazwisko")
email_label.grid(row = 3, column = 0)
email_label = Label(root, text = "Miasto")
email_label.grid(row = 4, column = 0)
email_label = Label(root, text = "Ulica")
email_label.grid(row = 5, column = 0)
email_label = Label(root, text = "Numer domu/Numer mieszkania")
email_label.grid(row = 6, column = 0)
email_label = Label(root, text = "Kod pocztowy")
email_label.grid(row = 7, column = 0)
email_label = Label(root, text = "Telefon")
email_label.grid(row = 8, column = 0)

rejestr_button = Button(root, text = "Zarejestruj się", command = rejestracja)
rejestr_button.grid(row = 9, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

