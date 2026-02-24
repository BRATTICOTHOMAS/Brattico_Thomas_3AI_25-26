#CRUD
#creat, read update, delete
#INFORMATICA
#------------TESTO PROBLEMA-------------
#colleziona iscritti ad una lotteria INFO UTILI
#-----------------------------------------
 
#-----------------------PROGETTAZIONE--------------------
#1) nome della persona che acquista il biglietto
# #cognome
#i numeri dei biglietti (acquistabili in più qta)
#-recapito telefonico
 
#2) quali controlli devo fare?
#-NOME solo lettere nome,no caratteri speciali, si spazi, minimo tre lettere
#COGNOMEsolo lettere nome,no caratteri speciali, si spazi, minimo tre lettere
#numeri biglietti acquistati
#CODICE BIGLIETTO Lnnn   LETTERA E TRE CIFRE I984
#numero telefono: numero cellulare, dieci cifre numeriche
#3)SCELTA STRUTTURE DATI:
#--> Variabili semplici
#---> liste, liste parallele
#---> tupla
#----> dizionari
#--->set
#4) ha sensol'operazione di update
#ha senso l'operazione di delete
#--------------------------------------------------
 
#--------VERSIONE RIDOTTA---------------
#colleziona nome cognome (insieme) --->stringa ----> lista stringhe
# ["alessio amato","carlo  bacuzzi", "marco guidi"]
#---------------------------------------
 
from colorama import Fore, Back, Style
 
nominativi=[]
esci=False
while not esci:
    print("--------VENDITA BIGLIETTO-----------")
    print("scegli:")
    print(Fore.YELLOW+"premi i per inserre il nominatovo dell'utente (CREATE)"+Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX+"2 per visualizzare i nominativi degli aquirenti (READ)"+Style.RESET_ALL)
    print("3 per modificare nominatvo (UPDATE)")
    print("4 eliminare il nominativo")
    print(" 0 per terminare il programma")
    scelta=input("scelta")
    if scelta not in ("0","1","2","3","4"):
        print(Fore.LIGHTRED_EX+"scelta non valida"+Style.RESET_ALL)
    elif scelta=="1":
 
        #CREATE
        #fase input
        corretto=False
        while not corretto:
            nominativo=input("inserire nominativo")
            nominativo=nominativo.strip()
            if len(nominativo)<7:
                print(Fore.LIGHTRED_EX+"NOMINATIVO NON VALIDO NON HA ABBASTANZA CARATTERI"+Style.RESET_ALL)
            elif not nominativo.replace(" ","").isalpha():
                print(Fore.LIGHTRED_EX+"NOMINATIVO NON VALIDO DEVE CONTENERE SOLO LETTERE"+Style.RESET_ALL)
            else:
                corretto=True
                print("nominativo corretto")
                nominativi.append(nominativo.title()) #nominativi tutti uguali in lista
    elif scelta=="2":
        #READ
        # print(Fore.LIGHTWHITE_EX+nominativi+Style.RESET_ALL)
        if len(nominativi)==0:
            print(Fore.LIGHTRED_EX+"NPN hai registrato ancora nominativi"+Style.RESET_ALL)
        else:
            for n in nominativi:
                print(Fore.LIGHTGREEN_EX+f"nel tuo archivio ci sono {len(nominativi)} nominativi"+Style.RESET_ALL)
                print(n)
    elif scelta=="3":
        for n,i in enumerate(nominativi):
                print(Fore.LIGHTGREEN_EX+f"nel tuo archivio ci sono {len(nominativi)} nominativi"+Style.RESET_ALL)
                print(f"{i+1} - {n}")
        corretto=False
        while not corretto:
            try:
                indice=int(input("quale nominativo vuoi modificare?"))
                if indice<1 or indice>len(nominativi):
                    print(Fore.LIGHTRED_EX+"indice non valido")
                else:
                    corretto=True
                    print(f"hai scelto di modificare il nominativo {nominativi[indice-1]}")
                    correttonominativo=False
                    while not correttonominativo:
                        nominativo=input("inserisci il nominativo: ").strip()
                        if len(nominativo)<7:
                            print(Fore.LIGHTRED_EX+"NOMINATIVO NON VALIDO NON HA ABBASTANZA CARATTERI"+Style.RESET_ALL)
                        elif not nominativo.replace(" ","").isalpha():
                            print(Fore.LIGHTRED_EX+"NOMINATIVO NON VALIDO DEVE CONTENERE SOLO LETTERE"+Style.RESET_ALL)
                        else:
                            correttonominativo=True
                            nominativi[indice-1]=nominativo.title()
                            print("nominativo modificato correttamente")    
            except :
                print("inserisci un nominativo valido")
                            
    elif scelta=="4":
        pass
    elif scelta=="0":
        esci=True
    corretto=False