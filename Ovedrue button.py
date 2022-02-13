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
    root.mainloop()

except (Exception, main.psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)