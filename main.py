import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="haslo123",
        port="5432"
    )

    cursor = connection.cursor()

    drop_table = '''
DROP TABLE IF EXISTS producenci CASCADE;
DROP TABLE IF EXISTS gatunki CASCADE;
DROP TABLE IF EXISTS klasy CASCADE;
DROP TABLE IF EXISTS platformy CASCADE;
DROP TABLE IF EXISTS gry CASCADE;
DROP TABLE IF EXISTS klienci CASCADE;
DROP TABLE IF EXISTS poczekalnia CASCADE;
DROP TABLE IF EXISTS wypozyczone CASCADE;
DROP TABLE IF EXISTS historia CASCADE;
DROP TABLE IF EXISTS adresy CASCADE;
'''
    drop_views = '''
    DROP VIEW IF EXISTS wyszukiwarka;
    '''
    drop_triggers = '''
        DROP TRIGGER IF EXISTS nowy_uzytkownik
        ON adresy CASCADE;
    '''

    cursor.execute(drop_table)
    connection.commit()
    cursor.execute(drop_views)
    connection.commit()
    cursor.execute(drop_triggers)
    connection.commit()

    create_table_query = '''
            CREATE TABLE producenci
            (nazwa TEXT UNIQUE PRIMARY KEY,
            lokalizacja TEXT);
            
            CREATE TABLE gatunki
            (nazwa TEXT PRIMARY KEY);

            CREATE TABLE klasy
            (id_klasy SERIAL PRIMARY KEY,
            cena INT);

            CREATE TABLE platformy
            (nazwa TEXT PRIMARY KEY);

          CREATE TABLE gry
          (id_gry SERIAL PRIMARY KEY,
          nazwa TEXT,
          id_klasy INT REFERENCES klasy(id_klasy) ON UPDATE CASCADE ON DELETE RESTRICT,
          producent TEXT REFERENCES producenci(nazwa) ON UPDATE CASCADE ON DELETE RESTRICT,
          gatunek TEXT REFERENCES gatunki(nazwa) ON UPDATE CASCADE ON DELETE RESTRICT,
          platforma TEXT REFERENCES platformy(nazwa) ON UPDATE CASCADE ON DELETE RESTRICT,
          data_wydania DATE,
          ilosc_sztuk INT
          );

          CREATE TABLE klienci
          (email TEXT PRIMARY KEY,
          haslo TEXT,
          id_koszyka SERIAL,
          saldo INT DEFAULT 0
          );

          CREATE TABLE adresy
          (email TEXT PRIMARY KEY REFERENCES klienci(email) ON UPDATE CASCADE ON DELETE CASCADE,
          imie TEXT,
          nazwisko TEXT,
          miasto TEXT,
          ulica TEXT,
          numer_budynku INT,
          numer_mieszkania INT,
          kod_pocztowy TEXT,
          telefon INT
          );
          
          CREATE TABLE poczekalnia
          (id_zamowienia SERIAL,
          id_gry INT REFERENCES gry(id_gry),
          email TEXT REFERENCES klienci(email) ON UPDATE CASCADE ON DELETE RESTRICT,
          data_zlozenia DATE,
          kod_platnosci INT);
          
          CREATE TABLE wypozyczone
          (id_zamowienia INT,
          id_gry INT REFERENCES gry(id_gry),
          email TEXT REFERENCES klienci(email) ON UPDATE CASCADE ON DELETE RESTRICT,
          data_zlozenia DATE,
          data_platnosci DATE,
          kod_zwrotu INT);
          
          CREATE TABLE historia
          (id_zamowienia INT,
          id_gry INT,
          email TEXT,
          data_zlozenia DATE,
          data_platnosci DATE,
          data_zwrotu DATE);
          '''

    views = '''
    CREATE VIEW wyszukiwarka AS
    SELECT nazwa, producent, gatunek, platforma, data_wydania, ilosc_sztuk, cena FROM
    gry INNER JOIN klasy ON gry.id_klasy = klasy.id_klasy;
    '''

    triggers = '''
          CREATE OR REPLACE FUNCTION new_user() RETURNS TRIGGER AS $$
          BEGIN
            INSERT INTO adresy(email) VALUES (new.email);
            RETURN NEW;
          END;
          $$ LANGUAGE 'plpgsql';
          
          CREATE TRIGGER 
          nowy_uzytkownik
          AFTER INSERT ON klienci
          FOR EACH ROW EXECUTE PROCEDURE new_user();
          '''

    cursor.execute(create_table_query)
    connection.commit()
    cursor.execute(views)
    connection.commit()
    cursor.execute(triggers)
    connection.commit()


except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)