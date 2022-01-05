import psycopg2
try:
    connection = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password = "haslo123",
    port = "5432"
    )

    cursor = connection.cursor()

    drop_table = '''
DROP TABLE producenci CASCADE;
DROP TABLE gatunki CASCADE;
DROP TABLE klasy CASCADE;
DROP TABLE platformy CASCADE;
DROP TABLE gry CASCADE;
DROP TABLE platnosci CASCADE;
DROP TABLE klienci CASCADE;
DROP TABLE adresy CASCADE;
DROP TABLE koszyki CASCADE;
DROP TABLE zamowienia CASCADE;
'''


    cursor.execute(drop_table)
    connection.commit()

    create_table_query = '''
            CREATE TABLE producenci
            (nazwa TEXT UNIQUE PRIMARY KEY,
            lokalizacja TEXT);
            
            CREATE TABLE gatunki
            (id_gatunku SERIAL PRIMARY KEY,
            nazwa TEXT UNIQUE);

            CREATE TABLE klasy
            (id_klasy SERIAL PRIMARY KEY,
            cena INT);

            CREATE TABLE platformy
            (id_platformy SERIAL PRIMARY KEY,
            nazwa TEXT);

          CREATE TABLE gry
          (id_gry SERIAL PRIMARY KEY,
          nazwa TEXT,
          id_klasy INT REFERENCES klasy(id_klasy) ON UPDATE CASCADE ON DELETE RESTRICT,
          id_producenta TEXT REFERENCES producenci(nazwa) ON UPDATE CASCADE ON DELETE RESTRICT,
          id_gatunku INT REFERENCES gatunki(id_gatunku) ON UPDATE CASCADE ON DELETE RESTRICT,
          id_platformy INT REFERENCES platformy(id_platformy) ON UPDATE CASCADE ON DELETE RESTRICT,
          data_wydania DATE,
          ilosc_sztuk INT
          );


          CREATE TABLE platnosci
          (id_platnosci SERIAL PRIMARY KEY,
          ilosc_sztuk INT
          );

          CREATE TABLE klienci
          (ID_KLIENTA SERIAL PRIMARY KEY,
          imie TEXT,
          nazwisko TEXT,
          id_koszyka INT,
          saldo INT
          );

          CREATE TABLE adresy
          (id_klienta SERIAL PRIMARY KEY REFERENCES klienci(id_klienta) ON UPDATE CASCADE ON DELETE CASCADE,
          miasto TEXT,
          ulica TEXT,
          numer_budynku INT,
          numer_mieszkania INT,
          kod_pocztowy INT,
          telefon INT
          );

          CREATE TABLE koszyki
          (id_koszyka SERIAL PRIMARY KEY,
          id_gry INT REFERENCES gry(id_gry),
          id_klienta INT REFERENCES klienci(id_klienta) ON UPDATE CASCADE ON DELETE CASCADE);

          CREATE TABLE zamowienia
          (id_zamowienia SERIAL PRIMARY KEY,
          id_klienta INT REFERENCES klienci(id_klienta) ON UPDATE CASCADE ON DELETE CASCADE,
          id_platnosci INT REFERENCES platnosci(id_platnosci) ON UPDATE CASCADE ON DELETE CASCADE,
          id_gry INT REFERENCES gry(id_gry),
          data_rozpoczecia DATE);
          '''

    cursor.execute(create_table_query)
    connection.commit()

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)