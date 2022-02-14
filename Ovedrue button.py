import random as r
import string as s
from search_bar import *

try:
    def overdue_f():

        overdue_query = '''
            SELECT * FROM overdue;
            '''

        main.cursor.execute(overdue_query)

        overdue = main.cursor.fetchall()

        if overdue:
            result = ""
            for record in overdue:
                result += str(record) + "\n"
            messagebox.showinfo("", "{}".format(result))
        else:
            messagebox.showinfo("", "Brak przetrzymanych produktów")

    overdue_label = Label(root, text="Sprawdź przetrzymane produkty")
    overdue_label.grid(row=0, column=5)
    overdue_button = Button(root, text="Sprawdź", command=overdue_f)
    overdue_button.grid(row=1, column=5, pady=10, padx=10, ipadx=80)

    class datetime:
        def date(self, a, b, c):
            pass


    def dodaj():
        tytul = title.get()
        platforma = platf.get()
        query = '''
                SELECT id_gry FROM gry WHERE nazwa = '{}'
                AND platforma = '{}' AND ilosc_sztuk>0;
                '''.format(tytul, platforma)
        main.cursor.execute(query)
        try:
            id_gry = main.cursor.fetchall()[0][0]
        except IndexError:
            messagebox.showinfo("", "Podana pozycja nie istnieje lub nie ma jej w magazynie.")
            return

        email_n = email_2.get()
        haslo_n = password.get()
        query_2 = '''
                  SELECT email FROM klienci WHERE email = '{}'
                  AND haslo = '{}';
                  '''.format(email_n, haslo_n)
        main.cursor.execute(query_2)
        try:
            email_n = main.cursor.fetchall()[0][0]
        except IndexError:
            messagebox.showinfo("", "Błędny email lub hasło.")
            return

        kod_platnosci = ''.join(r.sample(s.ascii_letters + s.digits, 9))

        main.cursor.execute('''
                            INSERT INTO poczekalnia(id_gry, email, kod_platnosci) 
                            VALUES ({}, '{}', '{}');
                            '''.format(id_gry, email_n, kod_platnosci))
        main.cursor.execute('''
                            SELECT max(id_zamowienia) FROM poczekalnia;
                            ''')
        id_zamowienia = main.cursor.fetchall()[0][0]
        main.cursor.execute('''
                            UPDATE poczekalnia SET kod_platnosci = (kod_platnosci || '{}')
                            WHERE id_zamowienia = {};
                            '''.format(id_zamowienia, id_zamowienia))
        main.cursor.execute('''
                            UPDATE gry SET ilosc_sztuk = ilosc_sztuk - 1 
                            WHERE id_gry = {};
                            '''.format(id_gry))
        main.connection.commit()
        title.delete(0, END)
        platf.delete(0, END)
        email_2.delete(0, END)
        password.delete(0, END)
        messagebox.showinfo("", "Złożono zamówienie.\nId twojego zamówienia to: {}".format(id_zamowienia))


    def wypozycz():
        id_zamowienia = id_zam.get()
        kod_platnosci = kod_pl.get()
        query = '''
                SELECT * FROM poczekalnia WHERE id_zamowienia = {} 
                AND kod_platnosci = '{}';
                '''.format(id_zamowienia, kod_platnosci)
        main.cursor.execute(query)
        try:
            id_zamowienia, id_gry, email, data_zlozenia, kod_platnosci = main.cursor.fetchall()[0]
        except ValueError:
            messagebox.showinfo("", "Błędne id zamówienia lub kod płatności.")
            return

        kod_zwrotu = ''.join(r.sample(s.ascii_letters + s.digits, 9)) + str(id_zamowienia)

        main.cursor.execute('''
                            INSERT INTO wypozyczone(id_zamowienia, id_gry, email, data_zlozenia, kod_platnosci, kod_zwrotu) 
                            VALUES({}, {}, '{}', '{}', '{}', '{}');
                            '''.format(id_zamowienia, id_gry, email, data_zlozenia, kod_platnosci, kod_zwrotu))

        main.cursor.execute('''
                            DELETE FROM poczekalnia WHERE id_zamowienia = {} 
                            AND kod_platnosci = '{}';
                            '''.format(id_zamowienia, kod_platnosci))
        main.connection.commit()
        id_zam.delete(0, END)
        kod_pl.delete(0, END)
        messagebox.showinfo("", "Zamówienie potwierdzone.\nGra zostanie wysłana na podany adres.")


    def zdaj():
        id_zamowienia = id_zam_2.get()
        kod_zwrotu = kod_zwr.get()
        query = '''
                SELECT id_zamowienia, id_gry, email, data_zlozenia, data_platnosci FROM wypozyczone 
                WHERE id_zamowienia = {} AND kod_zwrotu = '{}';
                '''.format(id_zamowienia, kod_zwrotu)
        main.cursor.execute(query)
        try:
            id_zamowienia, id_gry, email, data_zlozenia, data_platnosci = main.cursor.fetchall()[0]
        except ValueError:
            messagebox.showinfo("", "Błędne id zamówienia lub kod zwrotu.")
            return

        main.cursor.execute('''
                            INSERT INTO historia 
                            VALUES({}, {}, '{}', '{}', '{}');
                            '''.format(id_zamowienia, id_gry, email, data_zlozenia, data_platnosci))

        main.cursor.execute('''
                            DELETE FROM wypozyczone WHERE id_zamowienia = {} 
                            AND kod_zwrotu = '{}';
                            '''.format(id_zamowienia, kod_zwrotu))

        main.cursor.execute('''
                            UPDATE gry SET ilosc_sztuk = ilosc_sztuk + 1 
                            WHERE id_gry = {};
                            '''.format(id_gry))

        main.connection.commit()
        id_zam_2.delete(0, END)
        kod_zwr.delete(0, END)
        messagebox.showinfo("", "Zwrócono zamówienie.\nDziękujemy za skorzystanie z naszych usług.")


    title = Entry(root, width=30)
    title.grid(row=10, column=1, padx=20, pady=10)
    platf = Entry(root, width=30)
    platf.grid(row=11, column=1, padx=20, pady=10)
    email_2 = Entry(root, width=30)
    email_2.grid(row=12, column=1, padx=20, pady=10)
    password = Entry(root, width=30)
    password.grid(row=13, column=1, padx=20, pady=10)

    dodaj_label = Label(root, text="Tytuł")
    dodaj_label.grid(row=10, column=0)
    dodaj_label = Label(root, text="Platforma")
    dodaj_label.grid(row=11, column=0)
    dodaj_label = Label(root, text="Adres email")
    dodaj_label.grid(row=12, column=0)
    dodaj_label = Label(root, text="Haslo")
    dodaj_label.grid(row=13, column=0)

    dodaj_button = Button(root, text="Złóż zamówienie", command=dodaj)
    dodaj_button.grid(row=14, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    dodaj_label = Label(root, text="Nasz numer konta bankowego: 00 0000 0000 0000 0000 0000 0000")
    dodaj_label.grid(row=15, column=0, columnspan=2)

    id_zam = Entry(root, width=30)
    id_zam.grid(row=12, column=3, padx=20, pady=10)
    kod_pl = Entry(root, width=30)
    kod_pl.grid(row=13, column=3, padx=20, pady=10)

    wypozycz_label = Label(root, text="Id zamówienia")
    wypozycz_label.grid(row=12, column=2)
    wypozycz_label = Label(root, text="Kod platnosci")
    wypozycz_label.grid(row=13, column=2)

    wypozycz_button = Button(root, text="Potwierdź zamówienie", command=wypozycz)
    wypozycz_button.grid(row=14, column=2, columnspan=2, pady=10, padx=10, ipadx=100)

    id_zam_2 = Entry(root, width=30)
    id_zam_2.grid(row=12, column=5, padx=20, pady=10)
    kod_zwr = Entry(root, width=30)
    kod_zwr.grid(row=13, column=5, padx=20, pady=10)

    zdaj_label = Label(root, text="Id zamówienia")
    zdaj_label.grid(row=12, column=4)
    zdaj_label = Label(root, text="Kod zwrotu")
    zdaj_label.grid(row=13, column=4)

    zdaj_button = Button(root, text="Zwróć zamówienie", command=zdaj)
    zdaj_button.grid(row=14, column=4, columnspan=2, pady=10, padx=10, ipadx=100)

    root.mainloop()

except (Exception, main.psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)