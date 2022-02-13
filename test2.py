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
    
    INSERT INTO klienci(email, haslo, id_koszyka, saldo) VALUES
    ('szymonpawlak0@yahoo.com', 'ahsCxSI9r', 0, 0),
    ('polabaran1@yahoo.com', '12loCEyaO', 1, 0),
    ('janwrobel2@gmail.com', 'QdUaJwPe7', 2, 0),
    ('alicjamazur3@gmail.com', '70Rp2lwIy', 3, 0),
    ('lauraszewczyk4@o2.com', 'qh8nSa75O', 4, 0),
    ('antonizajac5@gmail.com', 'rBGj4h2wO', 5, 0),
    ('polawrobel6@interia.com', 'qrU7pFkxX', 6, 0),
    ('poladudek7@wp.com', 'rbI3xWfgD', 7, 0),
    ('zuzannamarciniak8@onet.com', 'XK1veLrFB', 8, 0),
    ('lenabaran9@yahoo.com', 'lD4vZmaE9', 9, 0),
    ('franciszekwalczak10@yahoo.com', 'FrJMSgcdz', 10, 0),
    ('filipkrol11@o2.com', 'CMPrp7Ze8', 11, 0),
    ('zofiapawlak12@gmail.com', 'mALSH6v1X', 12, 0),
    ('mikolajpawlak13@interia.com', 'jIAfGWVkb', 13, 0),
    ('polapietrzak14@gmail.com', 'Um0dgp7ZH', 14, 0),
    ('leondudek15@yahoo.com', 'KdThsprI6', 15, 0),
    ('hannakaczmarek16@interia.com', 'junDVWkS3', 16, 0),
    ('laurawozniak17@gmail.com', 'p3FYshk5v', 17, 0),
    ('hannanowak18@onet.com', 'cAb7KC4Zw', 18, 0),
    ('leonwojcik19@gmail.com', 'AYLjDuVE5', 19, 0);
    
    UPDATE adresy SET imie = 'Szymon', nazwisko = 'Pawlak', miasto = 'Szczecin', ulica = 'Lipowa', numer_budynku = 46, numer_mieszkania = 27, kod_pocztowy = '95-763', telefon = 921648075 WHERE email = 'szymonpawlak0@yahoo.com';
    UPDATE adresy SET imie = 'Pola', nazwisko = 'Baran', miasto = 'Lodz', ulica = 'Ogrodowa', numer_budynku = 23, numer_mieszkania = 14, kod_pocztowy = '74-580', telefon = 029617438 WHERE email = 'polabaran1@yahoo.com';
    UPDATE adresy SET imie = 'Jan', nazwisko = 'Wrobel', miasto = 'Poznan', ulica = 'Brzozowa', numer_budynku = 46, numer_mieszkania = 14, kod_pocztowy = '70-175', telefon = 576230981 WHERE email = 'janwrobel2@gmail.com';
    UPDATE adresy SET imie = 'Alicja', nazwisko = 'Mazur', miasto = 'Wroclaw', ulica = 'Polna', numer_budynku = 53, numer_mieszkania = 12, kod_pocztowy = '42-144', telefon = 056937418 WHERE email = 'alicjamazur3@gmail.com';
    UPDATE adresy SET imie = 'Laura', nazwisko = 'Szewczyk', miasto = 'Wroclaw', ulica = 'Polna', numer_budynku = 24, numer_mieszkania = 4, kod_pocztowy = '83-141', telefon = 748906512 WHERE email = 'lauraszewczyk4@o2.com';
    UPDATE adresy SET imie = 'Antoni', nazwisko = 'Zajac', miasto = 'Bialystok', ulica = 'Kwiatowa', numer_budynku = 39, numer_mieszkania = 8, kod_pocztowy = '21-342', telefon = 124685903 WHERE email = 'antonizajac5@gmail.com';
    UPDATE adresy SET imie = 'Pola', nazwisko = 'Wrobel', miasto = 'Bydgoszcz', ulica = 'Polna', numer_budynku = 67, numer_mieszkania = 10, kod_pocztowy = '98-118', telefon = 230674815 WHERE email = 'polawrobel6@interia.com';
    UPDATE adresy SET imie = 'Pola', nazwisko = 'Dudek', miasto = 'Wroclaw', ulica = 'Ogrodowa', numer_budynku = 61, numer_mieszkania = 28, kod_pocztowy = '37-749', telefon = 493627058 WHERE email = 'poladudek7@wp.com';
    UPDATE adresy SET imie = 'Zuzanna', nazwisko = 'Marciniak', miasto = 'Lodz', ulica = 'Brzozowa', numer_budynku = 40, numer_mieszkania = 28, kod_pocztowy = '10-725', telefon = 186043952 WHERE email = 'zuzannamarciniak8@onet.com';
    UPDATE adresy SET imie = 'Lena', nazwisko = 'Baran', miasto = 'Bialystok', ulica = 'Krotka', numer_budynku = 4, numer_mieszkania = 25, kod_pocztowy = '13-474', telefon = 458120693 WHERE email = 'lenabaran9@yahoo.com';
    UPDATE adresy SET imie = 'Franciszek', nazwisko = 'Walczak', miasto = 'Szczecin', ulica = 'Brzozowa', numer_budynku = 63, numer_mieszkania = 8, kod_pocztowy = '35-578', telefon = 289674351 WHERE email = 'franciszekwalczak10@yahoo.com';
    UPDATE adresy SET imie = 'Filip', nazwisko = 'Krol', miasto = 'Bydgoszcz', ulica = 'Lesna', numer_budynku = 47, numer_mieszkania = 30, kod_pocztowy = '54-227', telefon = 791438602 WHERE email = 'filipkrol11@o2.com';
    UPDATE adresy SET imie = 'Zofia', nazwisko = 'Pawlak', miasto = 'Gdansk', ulica = 'Sloneczna', numer_budynku = 76, numer_mieszkania = 21, kod_pocztowy = '14-819', telefon = 296574380 WHERE email = 'zofiapawlak12@gmail.com';
    UPDATE adresy SET imie = 'Mikolaj', nazwisko = 'Pawlak', miasto = 'Bialystok', ulica = 'Lakowa', numer_budynku = 63, numer_mieszkania = 15, kod_pocztowy = '15-512', telefon = 327658910 WHERE email = 'mikolajpawlak13@interia.com';
    UPDATE adresy SET imie = 'Pola', nazwisko = 'Pietrzak', miasto = 'Wroclaw', ulica = 'Krotka', numer_budynku = 3, numer_mieszkania = 19, kod_pocztowy = '41-736', telefon = 651780432 WHERE email = 'polapietrzak14@gmail.com';
    UPDATE adresy SET imie = 'Leon', nazwisko = 'Dudek', miasto = 'Poznan', ulica = 'Krotka', numer_budynku = 76, numer_mieszkania = 5, kod_pocztowy = '83-167', telefon = 493258071 WHERE email = 'leondudek15@yahoo.com';
    UPDATE adresy SET imie = 'Hanna', nazwisko = 'Kaczmarek', miasto = 'Wroclaw', ulica = 'Sloneczna', numer_budynku = 2, numer_mieszkania = 6, kod_pocztowy = '42-358', telefon = 350817249 WHERE email = 'hannakaczmarek16@interia.com';
    UPDATE adresy SET imie = 'Laura', nazwisko = 'Wozniak', miasto = 'Wroclaw', ulica = 'Sloneczna', numer_budynku = 42, numer_mieszkania = 10, kod_pocztowy = '36-889', telefon = 213405897 WHERE email = 'laurawozniak17@gmail.com';
    UPDATE adresy SET imie = 'Hanna', nazwisko = 'Nowak', miasto = 'Szczecin', ulica = 'Lesna', numer_budynku = 29, numer_mieszkania = 9, kod_pocztowy = '56-289', telefon = 239478650 WHERE email = 'hannanowak18@onet.com';
    UPDATE adresy SET imie = 'Leon', nazwisko = 'Wojcik', miasto = 'Bydgoszcz', ulica = 'Sloneczna', numer_budynku = 51, numer_mieszkania = 13, kod_pocztowy = '22-505', telefon = 546387190 WHERE email = 'leonwojcik19@gmail.com';

    INSERT INTO wypozyczone(id_zamowienia, id_gry, email, data_zlozenia, data_platnosci, kod_zwrotu) VALUES
    (1,2,'szymonpawlak0@yahoo.com', '19-11-1998', '19-11-1998', 13);
'''

    main.cursor.execute(goticzek)
    main.connection.commit()

except (Exception, main.psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)