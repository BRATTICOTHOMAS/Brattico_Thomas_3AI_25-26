#inserisci scuderia, cambia punteggio, visualizza punti,elimina scuderia, controllo chiavi
scelta=""
dati={"McLaren" : 833, "Mercedes": 469, "RedBull":451,"Aston Martin": 89 }
while scelta !="6":
    print("---------------------------")
    print(" 1 -----Inserisci scuderia-")
    print(" 2 -----Cambia punteggio---")
    print(" 3 -----Elimina scuderia---")
    print(" 4 -----Visualizza archivio")
    print(" 5 -----Classifica---------")
    print(" 6 -----Fine programma-----")
    print("---------------------------")
    scelta=input("cosa vuoi fare?  ( digita un numero tra questi: 1,2,3,4,5,6): ").strip()

    if scelta =="1":
        scuderia=input("inserisci il nome della scuderia").capitalize().strip()
        if scuderia in dati:
            print("la scuderia è gia presente")
        else:
            punti = int(input("inserisci il punteggo della corrispettiva scuderia"))
            try:
                if len(scuderia)>4 and punti>50:
                    print("scuderia aggiunta con successo")
                    dati[scuderia] = punti
                else:
                    print("scuderia non aggiunta (nome troppo corto o punti inferiori a 50)")
            except:
                print("errore nel nome o nei punti")

    if scelta =="2":
        scuderia=input("inserisci il nome della scuderia").capitalize().strip()
        if scuderia in dati:
            scelt=input("cosa vuoi fare (1)cambiare il punteggio o (2)aggiungerne?")
            if scelt =="1":
                puntinuovi=int(input("inserisci i punti nuovi della scuderia"))
                dati[scuderia]=puntinuovi
            if scelt =="2":
                puntinuovi=int(input("inserisci i punti da aggiungere o eliminare dalla scuderia"))
                if puntinuovi>0:
                    print("modifiche salvate con successo")
                    dati[scuderia]=puntinuovi + punti
    if scelta =="3":
        scuderia=input("inserisci il nome della scuderia da eliminare").capitalize().strip()
        if scuderia in dati:
            dati.pop(scuderia)
    if scelta =="4":
        print(dati)
    if scelta=="5":#classifica
        print("CLASSIFICA")
        classifica= sorted(dati.items(), key=lambda x: x[1], reverse=True)#per ottenere le liste di duple è : .items, lambda duple è l'ennesimo di x nel caso di 1 va in base al punteggio invece se parte da 0 va in ordine alfabetico (senza reverse); sorted è applicabile a tutto quello che è iterabile. lambda è una funzione anonima
        print(classifica)
        for s in classifica:
            print(f"Scuderia {s} - punti {s[1]}")#stampo le tuple
    if scelta=="6":
       print("BYE BYE")
    else:
        print("scelta inesistenza") 
