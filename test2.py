import main
try:
    goticzek = '''
    INSERT INTO producenci (nazwa, lokalizacja)
    VALUES ('Valve', 'USA');
    INSERT INTO producenci (nazwa, lokalizacja)
    VALUES ('Piranha Bytes', 'Austria');
    INSERT INTO producenci (nazwa, lokalizacja)
    VALUES ('Square Enix', 'Japonia');
    INSERT INTO producenci (nazwa, lokalizacja)
    VALUES ('Nintendo', 'Japonia');
    INSERT INTO producenci (nazwa, lokalizacja)
    VALUES ('Microsoft Studios', 'USA');
    INSERT INTO producenci (nazwa, lokalizacja)
    VALUES ('Capcom', 'Japonia');
    INSERT INTO producenci (nazwa, lokalizacja)
    VALUES ('Rockstar Games', 'USA');
    INSERT INTO producenci (nazwa, lokalizacja)
    VALUES ('Tate Multimedia', 'Polska');
    INSERT INTO producenci (nazwa, lokalizacja)
    VALUES ('EA DICE', 'Szwecja');
    INSERT INTO producenci (nazwa, lokalizacja)
    VALUES ('Insomniac Games', 'USA');
    INSERT INTO producenci (nazwa, lokalizacja)
    VALUES ('id Software', 'USA');
    INSERT INTO producenci (nazwa, lokalizacja)
    VALUES ('EA Canada', 'Kanada');
    INSERT INTO gatunki (nazwa)
    VALUES ('FPS');
    INSERT INTO gatunki (nazwa)
    VALUES ('RPG');
    INSERT INTO gatunki (nazwa)
    VALUES ('Horror');
    INSERT INTO gatunki (nazwa)
    VALUES ('Przygodowa');
    INSERT INTO gatunki (nazwa)
    VALUES ('Akcji');
    INSERT INTO gatunki (nazwa)
    VALUES ('Platformowa');
    INSERT INTO gatunki (nazwa)
    VALUES ('Wyścigowa');
    INSERT INTO platformy (nazwa)
    VALUES ('PC');
    INSERT INTO platformy (nazwa)
    VALUES ('Xbox');
    INSERT INTO platformy (nazwa)
    VALUES ('Nintendo 64');
    INSERT INTO platformy (nazwa)
    VALUES ('PlayStation'); 
    INSERT INTO platformy (nazwa)
    VALUES ('PlayStation 2');
    INSERT INTO klasy (cena)
    VALUES (10);
    INSERT INTO klasy (cena)
    VALUES (20);
    INSERT INTO klasy (cena)
    VALUES (30);
    INSERT INTO gry (nazwa, id_klasy, producent, gatunek, platforma, data_wydania, ilosc_sztuk)
    VALUES ('Gothic', 2, 'Piranha Bytes', 'RPG', 'PC', '15-03-2001', 2);
    INSERT INTO gry (nazwa, id_klasy, producent, gatunek, platforma, data_wydania, ilosc_sztuk)
    VALUES ('Resident Evil 2', 1, 'Capcom', 'Horror', 'PlayStation', '21-01-1998', 1);
    INSERT INTO gry (nazwa, id_klasy, producent, gatunek, platforma, data_wydania, ilosc_sztuk)
    VALUES ('Half-Life', 1, 'Valve', 'FPS', 'PC', '19-11-1998', 4);
    INSERT INTO gry (nazwa, id_klasy, producent, gatunek, platforma, data_wydania, ilosc_sztuk)
    VALUES ('Half-Life 2', 3, 'Valve', 'FPS', 'PC', '16-11-2004', 0);
    INSERT INTO gry (nazwa, id_klasy, producent, gatunek, platforma, data_wydania, ilosc_sztuk)
    VALUES ('The Legend of Zelda: Ocarina of Time', 2, 'Nintendo', 'Przygodowa', 'Nintendo 64', '21-11-1998', 2);
    INSERT INTO gry (nazwa, id_klasy, producent, gatunek, platforma, data_wydania, ilosc_sztuk)
    VALUES ('Grand Theft Auto III', 3, 'Rockstar Games', 'Akcji', 'PlayStation 2', '22-11-2001', 1);
    INSERT INTO gry (nazwa, id_klasy, producent, gatunek, platforma, data_wydania, ilosc_sztuk)
    VALUES ('Grand Theft Auto III', 3, 'Rockstar Games', 'Akcji', 'PC', '21-05-2002', 0);
    INSERT INTO gry (nazwa, id_klasy, producent, gatunek, platforma, data_wydania, ilosc_sztuk)
    VALUES ('Final Fantasy VII', 3, 'Square Enix', 'RPG', 'PlayStation', '31-01-1997', 2);
    INSERT INTO gry (nazwa, id_klasy, producent, gatunek, platforma, data_wydania, ilosc_sztuk)
    VALUES ('Kangurek Kao', 1, 'Tate Multimedia', 'Platformowa', 'PC', '23-11-2000', 6);
    INSERT INTO gry (nazwa, id_klasy, producent, gatunek, platforma, data_wydania, ilosc_sztuk)
    VALUES ('Kangurek Kao 2', 2, 'Tate Multimedia', 'Platformowa', 'PC', '4-11-2003', 3);
    INSERT INTO gry (nazwa, id_klasy, producent, gatunek, platforma, data_wydania, ilosc_sztuk)
    VALUES ('Super Mario 64', 3, 'Nintendo', 'Platformowa', 'Nintendo 64', '23-06-1996', 2);
    INSERT INTO gry (nazwa, id_klasy, producent, gatunek, platforma, data_wydania, ilosc_sztuk)
    VALUES ('Battlefield 1942', 2, 'EA DICE', 'FPS', 'PC', '10-09-2002', 1);
    INSERT INTO gry (nazwa, id_klasy, producent, gatunek, platforma, data_wydania, ilosc_sztuk)
    VALUES ('Ratchet & Clank', 2, 'Insomniac Games', 'Przygodowa', 'PlayStation 2', '4-11-2002', 3);
    INSERT INTO gry (nazwa, id_klasy, producent, gatunek, platforma, data_wydania, ilosc_sztuk)
    VALUES ('Ratchet & Clank 2', 3, 'Insomniac Games', 'Przygodowa', 'PlayStation 2', '11-11-2003',2);
    INSERT INTO gry (nazwa, id_klasy, producent, gatunek, platforma, data_wydania, ilosc_sztuk)
    VALUES ('Quake', 1, 'id Software', 'FPS', 'PC', '22-06-1996', 7);
    INSERT INTO gry (nazwa, id_klasy, producent, gatunek, platforma, data_wydania, ilosc_sztuk)
    VALUES ('Quake III: Arena', 2, 'id Software', 'FPS', 'PC', '3-12-1999', 4);
    INSERT INTO gry (nazwa, id_klasy, producent, gatunek, platforma, data_wydania, ilosc_sztuk)
    VALUES ('Need for Speed II', 1, 'EA Canada', 'Wyścigowa', 'PC', '12-04-1997', 9);
    INSERT INTO gry (nazwa, id_klasy, producent, gatunek, platforma, data_wydania, ilosc_sztuk)
    VALUES ('Need for Speed II', 1, 'EA Canada', 'Wyścigowa', 'PlayStation', '17-11-1997', 12);
    '''

    main.cursor.execute(goticzek)
    main.connection.commit()

except (Exception, main.psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)