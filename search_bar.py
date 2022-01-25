from nowy import *
import test2
try:

    search_label = Label()
    def wydrukuj_wyniki(wyniki):
        records = ''
        global search_label
        if not wyniki:
            records = 'Brak wyników.'
        else:
            for row in wyniki:
                #print(row)
                records += str(row) + "\n"

        search_label.destroy()
        search_label = Label(root, text = records)
        search_label.grid(row = 2, column = 3, columnspan = 2, rowspan = 5)

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

    root.mainloop()

except (Exception, main.psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)