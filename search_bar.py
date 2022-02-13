from nowy import *
import test2
from copy import deepcopy
try:
    labels = ['Tytuł', 'Producent', 'Gatunek', 'Platforma', 'Data wydania', 'Ilość sztuk', 'Cena']
    def string_limits(records):
        rec = deepcopy(records)
        rec.append(labels)
        records = ([list(i) for i in zip(*rec)])
        result = {}
        for record in records:
            result[records.index(record)] = len(max(map(str, record), key=len)) + 2
        return result

    def print_row(row):
        result = ""
        for record in row:
            result += str(record) + " " * (limits[row.index(record)] - len(str(record)))
        result += "\n"
        return result


    search_label = Label()
    def wydrukuj_wyniki(wyniki):
        records = print_row(labels) + "\n"
        global search_label

        if not wyniki:
            records = 'Brak wyników.'
        else:
            for row in wyniki:
                #print(row)
                records += print_row(row)
        print(records)
        search_label.destroy()
        search_label = ttk.Label(root, text = records.strip(), justify=LEFT, style="Courier.TButton")
        search_label.grid(row = 2, column = 3, columnspan = 10, rowspan = 10)

    def wyszukaj():
        platforma = variable.get()
        nazwa = search.get()
        dostepnosc = av.get()
        fetch_que = '''
                    SELECT * FROM wyszukiwarka
                    WHERE nazwa LIKE '%{}%'
                    '''.format(nazwa)
        if platforma != "Dowolna":
            fetch_que +=  '''
            AND platforma = '{}'
            '''.format(platforma)
        elif dostepnosc:
            print("a")
            fetch_que += '''
            AND ilosc_sztuk > 0
            '''
        fetch_que += ';'

        main.cursor.execute(fetch_que)
        results = main.cursor.fetchall()
        global limits
        limits = string_limits(results)
        wydrukuj_wyniki(results)


    platformy_query = '''
        SELECT * FROM platformy;
        '''

    main.cursor.execute(platformy_query)

    platformy = main.cursor.fetchall()

    for i in range(len(platformy)):
        platformy[i] = platformy[i][0]
    platformy.insert(0, "Dowolna")
    variable = StringVar(root)
    variable.set(platformy[0])


    search = Entry(root, width=30)
    search.grid(row=0, column=3, padx=20)

    enter = Button(root, text = "Szukaj", command = wyszukaj)
    enter.grid(row = 1, column = 3 , pady = 10, padx = 10, ipadx = 80)

    av = BooleanVar()
    check_av = Checkbutton(root, text='Wyszukaj pozycje, \n które są ma w magazynie',
                     variable=av, onvalue=True, offvalue=False)
    check_av.grid(row = 1, column =4)

    gatunki = OptionMenu(root, variable, *platformy)
    gatunki.grid(row=0, column=4)



except (Exception, main.psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)