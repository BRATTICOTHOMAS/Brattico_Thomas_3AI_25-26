# CRUD
# Create, Read, Update, Delete
# INFORMATICA

# -------------- TESTO DEL PROBLEMA -------------------
# collezionare gli iscritti ad una lotteria
#------------------------------------------------------

# ------------------ PROGETTAZIONE -------------------
# 1) quali informazioni ci serve collezionare?
# - nome della persona che ha acquistato il biglietto
# - cognome della persona che ha acquistato il biglietto
# - i numeri dei biglietti acquistati (ognuno può acquistare più di un biglietto)
# - numero di telefono
# 2) quali controlli devo fare?
# - nome: solo lettere (niente numeri nè caratteri speciali), può contenere spazi, minimo 3 lettere
# - cognome: solo lettere (niente numeri nè caratteri speciali), può contere spazi, minimo 3 lettere
# - codice biglietto: formato LNNN 
# - numero di telefono: numero cellulare, 10 cifre numeriche   
# 3) la/e struttura/i dati     --> variabili semplici, liste, liste parallele, tupla, dizionari, set 
# 4) ha senso l'operazione di update? se si, quale informazioni?
# 5) ha senso l'operazione di delete?
# ---------------------------------------------------

# -----------------------------------------------
# collezionare solo nome e cognome (insieme)  --> stringa --> lista di stringhe
#   [ "alessio amato", "carlo bacuzzi", "guidi marco"]
# collezionare anche il codice del biglietto comprato -->stringa --->lista di stringhe
# ["A000", "A001", "A002"]
# collezionare anche il numero di telefono --> stringa ---> lista di stringhe
#["012346789", "5555555555", "4545454545"]
# ---------------------------------------------------

from termcolor import colored

nominativi = []
codicibiglietti=[]
esci = False
while not esci:
    
    print("---------------SOFTWARE DI VENDITA BIGLIETTI------------")
    print("Scegli:")
    print(colored("1 per inserire il nominativo di un acquirente (CREATE)", "blue"))
    print(colored("2 per visualizzare i nominativi degli acquirenti (READ)", "blue"))
    print(colored("3 per modificare il nominativo di un acquirente (UPDATE)", "blue"))
    print(colored("4 per eliminare un nominativo (DELETE)", "blue"))
    print(colored("0 per terminare il programma", "red"))

    scelta = input("Scelta: ")
    if scelta not in ("0", "1", "2", "3", "4"):
        print(colored("Scelta non valida", "red"))
    elif scelta == "1":

        #fase di input
        corretto = False
        while not corretto:
            nominativo = input("Inserisci il nominativo ").strip()
            if len(nominativo) < 7:
                print(colored("Nominativo troppo corto. Inserire almeno 7 caratteri", "red"))
            elif not nominativo.replace(" ", "").isalpha():
                print(colored("Il nominativo deve contenere solo lettere minuscole o maiuscole", "red"))
            else:
                corretto = True
        corretto = False
        while not corretto:
            codicebiglietto = input("Inserisci il codice biglietto ").strip()
            if len(codicebiglietto) < 4:
                print(colored("codice troppo corto." "red"))
            elif not codicebiglietto[0].isalpha() or not codicebiglietto[1:4].isdigit():
                print(colored("Il formato del biglietto non è valido", "red"))
            elif codicebiglietto in codicibiglietti:
                print(colored("biglietto già acquistato da qualcuno", "red"))
            else:
                corretto = True

        #create
        nominativi.append(nominativo.title())   #aggiungo il nominativo con le maisucole su nome e cognome così ho tutti i nominativi nella stessa forma

    elif scelta == "2":
        #read
        # print(nominativi)  💩 non si fa --> 4 in verifica
        if len(nominativi) == 0:
            print(colored("Non hai ancora registrato alcun nominativo", "green"))
        else:
            print(f"Nel tuo archivio ci sono {len(nominativi)} nominativi: ")
            for i in range(len(nominativi)):
                print(F"{nominativi} CODICE BIGLIETTO: {codicibiglietti}")
        
    elif scelta == "3":

        if len(nominativi) == 0:
            print(colored("Non hai ancora registrato alcun nominativo", "green"))
        else:

            #prima mostro l'elenco dei nominativi disponibili con un riferimento numerico davanti
            print(f"Nel tuo archivio ci sono {len(nominativi)} nominativi: ")
            for i, n in enumerate(nominativi):
                print(f"{i+1} - {n}")

            #chiedo quale nominativo si vuole modificare
            corretto = False
            while not corretto:
                
                try:
                    indice = int(input("Quale è l'indice del nominativo che vuoi modificare?"))
                    if indice < 1 or indice > len(nominativi):
                        print(colored("Indice non corretto.", "red"))   
                    else:
                        corretto = True

                        print(f"Stai per modificare il nominativo {nominativi[indice-1]}")
                        #inserimento del nuovo nominativo
                        correttoNominativo = False
                        while not correttoNominativo:
                            nominativo = input("Inserisci il nominativo ").strip()
                            if len(nominativo) < 7:
                                print(colored("Nominativo troppo corto. Inserire almeno 7 caratteri", "red"))
                            elif not nominativo.replace(" ", "").isalpha():
                                print(colored("Il nominativo deve contenere solo lettere minuscole o maiuscole", "red"))
                            else:
                                correttoNominativo = True

                        # il nominativo è corretto
                        #update
                        nominativi[indice-1] = nominativo

                        #ATTENZIONE!!!!
                        #c'è una netta differenza tra modifica e sostituzione
                        #modifica:     lista[n] = ....
                        #sostituzione:
                        #              lista.pop(n)
                        #              lista.append(...)

                except:
                    print(colored("Formato indice non corretto.", "red"))   

    elif scelta == "4":
        
        if len(nominativi) == 0:
            print(colored("Non hai ancora registrato alcun nominativo", "green"))
        else:

            #prima mostro l'elenco dei nominativi disponibili con un riferimento numerico davanti
            print(f"Nel tuo archivio ci sono {len(nominativi)} nominativi: ")
            for i, n in enumerate(nominativi):
                print(f"{i+1} - {n}")

            #chiedo quale nominativo si vuole eliminare
            corretto = False
            while not corretto:
                
                try:
                    indice = int(input("Quale è l'indice del nominativo che vuoi eliminare?"))
                    if indice < 1 or indice > len(nominativi):
                        print(colored("Indice non corretto.", "red"))   
                    else:
                        corretto = True

                        #delete
                        nominativi.pop(indice-1)

                except:
                    print(colored("Formato indice non corretto.", "red"))   

        pass
    elif scelta == "0":
        esci = True
