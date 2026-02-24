#3 tipi di codici sconto:1= 11-11 è uno sconto basato sul black fryday tra il 3% e il 5%, 
# 2= sconto nominale (es carlo con 3% ipotesi no spazi e trattini-marco3 3%,sara4 4%,thomas7 7%)
#3 = sconto fisso =sconto1, sconto2, sconto3, ogni sconto è fissato da noi
#l'utente inserisce il codice sconto.
#(fatto)
#aggiungere:
#tot. di tutte le spese
#tot.di tutti gli sconti utilizzati (fatto)
#spesa max,min e valore medio 
#tempo tot. di uso programma (fatto)
sconto1= 10/100
sconto2 = 6/100
sconto3 = 2/100
sm=3/100
ss=4/100
st=7/100
serie_sconti=0
serie_spesa=0
import random
import time
from datetime import datetime
inizio=datetime.now()
sconto=random.randint(3,5)
corretto=False
while not corretto:
    try:
        prezzo=float(input("aggiungi il prezzo della spesa: "))
        if prezzo<0:
            print("questo software non supporta ancora i numeri negativi")
        else:
            corretto=True
    except:
        print("input non valido")
utente=input("hai un o più codice sconto?(si/no)").strip()
if utente.lower() == "si":
    s=True
    tenta=0
    while s:
        
        utente =input("scrivi lo sconto: ")
        if tenta<3:
            try:
                if utente ==utente[:-1].isalpha() and utente==utente[-1].isdigit():
                    print("codice nominale")
                    if utente=="marco3":
                        ps=prezzo*sconto
                        pf=prezzo-ps
                        ps=pf*sm
                        pf=pf-ps
                        prezzo=pf
                        serie_sconti=serie_sconti+1
                        print(f"la tua spesa sara scontato del {sm:.0%} e del {sconto:.0%}")
                        print(f"quindi il prezzo finale è{pf}")
                        utente=input("hai altri sconti? (si/no): ")
                        if utente.lower() == "no":
                            s=False
                    elif utente=="sara4":
                        ps=prezzo*sconto
                        pf=prezzo-ps
                        ps=pf*ss
                        pf=pf-ps
                        prezzo=pf
                        serie_sconti=serie_sconti+1
                        print(f"la tua spesa sara scontato del {ss:.0%} e del {sconto:.0%}")
                        print(f"quindi il prezzo finale è{pf}")
                        utente=input("hai altri sconti? (si/no): ")
                        if utente.lower() == "no":
                            s=False
                    elif utente=="thomas7":
                        ps=prezzo*sconto
                        pf=prezzo-ps
                        ps=pf*st
                        pf=pf-ps
                        prezzo=pf
                        serie_sconti=serie_sconti+1
                        print(f"la tua spesa sara scontato del {st:.0%} e del {sconto:.0%}")
                        print(f"quindi il prezzo finale è{pf}")
                        utente=input("hai altri sconti? (si/no): ")
                        if utente.lower() == "no":
                            s=False
                    else:
                        print("la tua spea sara scontata dal black fryday")
                        ps=prezzo*sconto
                        pf=prezzo-ps
                        serie_sconti=serie_sconti+1
                        print(f"la tua spesa sara scontato del  {sconto:.0%}")
                        print(f"quindi il prezzo finale è{pf}")
                if utente.lower() =="sconto1":
                    ps=prezzo*sconto
                    pf=prezzo-ps
                    ps=pf*sconto1
                    pf=pf-ps
                    prezzo=pf
                    serie_sconti=serie_sconti+1
                    print(f"la tua spesa sara scontato del {sconto1:.0%} e del {sconto:.0%}")
                    print(f"quindi il prezzo finale è{pf}")
                    utente=input("hai altri sconti? (si/no): ")
                    if utente.lower() == "no":
                        s=False
                elif utente.lower() =="sconto2":
                    ps=prezzo*sconto
                    pf=prezzo-ps
                    ps=pf*sconto2
                    pf=pf-ps
                    prezzo=pf
                    serie_sconti=serie_sconti+1
                    print(f"la tua spesa sara scontato del {sconto2:.0%} e del {sconto:.0%}")
                    print(f"quindi il prezzo finale è{pf}")
                    utente=input("hai altri sconti? (si/no): ")
                    if utente.lower() == "no":
                        s=False
                elif utente.lower()== "sconto3":
                    ps=prezzo*sconto
                    pf=prezzo-ps
                    ps=pf*sconto3
                    pf=pf-ps
                    prezzo=pf
                    serie_sconti=serie_sconti+1
                    print(f"la tua spesa sara scontato del {sconto3:.0%} e del {sconto:.0%}")
                    print(f"quindi il prezzo finale è{pf}")
                    utente=input("hai altri sconti? (si/no): ")
                    if utente.lower() == "no":
                        s=False
            except:
                tenta=tenta+1
                print("sei sicuro di avere dei codici sconto...")   
    else:
        print("hai esaurito i tentativi di avere degli sconti")
else:
    print("ok la tua spesa sarà scontato solo dal black fryday")
    ps=prezzo*sconto
    pf=prezzo-ps
    serie_sconti=serie_sconti+1
    print(f"la tua spesa sara scontato del {sconto:.0%}")
    print(f"quindi il prezzo finale è{pf}")
ora=datetime.now()

serie_spesa=serie_spesa +1
serie=input("vuoi continuare la serie(si/no): ").strip()
serie=serie.lower()
if serie=="si":
    corretto=False
else:
    corretto=True
    print(f"il tempo di esecuzione programma {ora-inizio} 🕑")
    print(f"hai utilizzato {serie_sconti} sconto/i")