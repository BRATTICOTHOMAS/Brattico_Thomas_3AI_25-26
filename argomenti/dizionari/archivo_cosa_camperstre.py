#archivo risultati corsa campestre, codice CB001,
# valori: nome e cognome, anno di nascita, tempo in secondi
# dizionario1 contenente : nome e cognome: data di nascita
#dizionario2 contenente : codice: tempo in secondi
#può cambiare solo il tempo
scelta=""
dati={}
while scelta !="6":
    print("---------------------------")
    print(" 1 -----Inserisci atleta-")
    print(" 2 -----Cambia tempo---")
    print(" 3 -----Elimina atleta---")
    print(" 4 -----Visualizza archivio")
    print(" 5 -----Classifica---------")
    print(" 6 -----Fine programma-----")
    print("---------------------------")
    scelta=input("cosa vuoi fare?  ( digita un numero tra questi: 1,2,3,4,5,6): ").strip()
    if scelta=="1":
        print("inserisci un nuovo atleta")
        nome=input("inserisci il nome del nuovo atleta: ")
        cognome=input("inserisci il cognome del nuovo atleta: ")
        if cognome in dati:
            print("l' atleta è gia presente")
        else:
            secondi = int(input("inserisci i secondi del corrispettivo atleta"))
            try:
                if len(cognome)>4 and secondi>50:
                    print("scuderia aggiunta con successo")
                    dati[cognome] = secondi
                else:
                    print("scuderia non aggiunta (nome troppo corto o punti inferiori a 50)")
            except:
                print("errore nel nome o nei punti")
        data=int(input("inserisci l'anno di nascità: "))

    elif scelta=="2":
        pass
    elif scelta=="3":
        pass
    elif scelta=="4":
        pass
    elif scelta=="5":
        pass
    if scelta=="6":
       print("BYE BYE")
    else:
        print("scelta inesistenza") 
