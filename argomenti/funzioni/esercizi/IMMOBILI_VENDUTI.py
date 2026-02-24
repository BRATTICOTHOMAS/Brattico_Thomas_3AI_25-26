#2) scrivere un programma, organizzato in funzioni, 
# che consenta di collezionare immobili venduti da una agenzia immobiliare. 
# Per ogni immobile si vuole memorizzare: la tipologia (appartamento, villa),
#  la tipologia in base alle stanze (monolocale, bilocale, trilocale, quadrilocale), il prezzo. 

def stampaMenu():
    print(" ------------- IMMOBILI VENDUTI --------------")
    print("Scegli:")
    print("1 - per inserire un nuovo immobile venduto")
    print("2 - per visualizzare tutti gli immobili venduti")
    print("3 - modificare un immobile")
    print("4 - eliminare un immobile")
    print("0 - terminare il programma")

def scelta():
    corretto = False
    while not corretto:
        try:
            scelta = int(input("Scelta >> "))
            if scelta < 0 or scelta > 4:
                print("Scelta non valida")
                corretto = False
            else:
                corretto = True  
                return scelta          
        except:
            print("Formato scelta non valido")
            corretto = False

def chiediImmobile():
    corretto = False
    while not corretto:
        tipologia = input("Inserisci la tipologia dell'immobile venduto (appartamento, villa): ").strip().lower()
        stanze = input("Inserisci la tipologia in base alle stanze (monolocale, bilocale, trilocale, quadrilocale): ").strip().lower()
        try:
            prezzo = float(input("Inserisci il prezzo dell'immobile venduto: "))
            if tipologia == "" or stanze == "" or prezzo <= 0:
                print("Dati immobile non validi")
                corretto = False
            else:
                corretto = True
        except:
            print("Formato prezzo non valido")
            corretto = False
    return (tipologia, stanze, prezzo)

def inserisciImmobile(immobili):
    immobile = chiediImmobile()
    immobili.append(immobile)

def eliminaImmobile(immobili):
    visualizzaImmobili(immobili)
    posizione = chiediPosizione(immobili)
    immobili.pop(posizione-1)

def chiediPosizione(immobili):
    corretto = False
    while not corretto:
        try:
            scelta = int(input("Indica il numero dell'immobile da modificare/eliminare "))
            if scelta < 1 or scelta > len(immobili):
                print("Numero immobile non valido")
                corretto = False
            else:
                corretto = True  
                return scelta          
        except:
            print("Formato numero immobile non valido")
            corretto = False

def modificaImmobile(immobili):
    visualizzaImmobili(immobili)
    posizione = chiediPosizione(immobili)
    immobile = chiediImmobile()
    immobili[posizione-1] = immobile

def visualizzaImmobili(immobili):
    if len(immobili) == 0:
        print("Nessun immobile venduto")
    else:
        for i, immobile in enumerate(immobili):
            tipologia, stanze, prezzo = immobile
            print(f"{i+1}. Tipologia: {tipologia}, Stanze: {stanze}, Prezzo: {prezzo}")

def scelta():
    corretto = False
    while not corretto:
        try:
            scelta = int(input("Scelta >> "))
            if scelta < 0 or scelta > 4:
                print("Scelta non valida")

                corretto = False
            else:
                corretto = True  
                return scelta
        except:
            print("Formato scelta non valido")
            corretto = False


#programma principale
immobili_venduti = []
fine = False
while not fine:
    stampaMenu()
    s = scelta()
    if s == 1:
        inserisciImmobile(immobili_venduti)
    elif s == 2:
        visualizzaImmobili(immobili_venduti)
    elif s == 3:
        modificaImmobile(immobili_venduti)
    elif s == 4:
        eliminaImmobile(immobili_venduti)
    elif s == 0:
        print("Arrivederci!")
        fine = True

