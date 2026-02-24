#menu che gestisce: un velodromo,nome e cognome,
#il suo miglior tempo sul giro e posso cambiare solo il tempo,
#usare 2 liste in paralello 1(nome e cognome) 2(tempo migliore)
#stampa nella classifica i primi 5 e gli ultimi 5
nomi=[]
tempi=[]
coppie=[]
scelta="0"
while scelta!="7":
    print("--------MENU PRINCIPALE------")
    print("---1----AGGIUNGI CICLISTA----")
    print("---2----MODIFICA TEMPO-------")
    print("---3----CLASSIFICA-----------")
    print("---4----ELIMINA CICLISTA-----")
    print("---7----ESCI-----------------")
    print("-----------------------------")
    scelta=input("Inserisci la scelta (1,2,3,4,7)")
    if scelta not in ("1","2","3","4","7"):
        print("La scelta da te fatta non è compresa nel menu")
    elif scelta =="1":
        corretto=False
        while not corretto:
            nome=input("inserisci il nome del ciclista").strip()
            cognome=input("inserisci il cognome del cicista").strip()
            if nome.isalpha()==False or cognome.isalpha()==False:
                print("il nome o il cognome sono scritti incorrettamente")
            else:
                nome=nome+" "+cognome
                corretto=True
        corretto=False
        while not corretto:
            try:
                tempo=float(input("inserisci il tempo dell'atleta (in secondi): "))
                if tempo<=8:
                    print("il tempo da te dichiarato è inferiore a 8 secondi ")
                else:
                    nomi.append(nome)
                    tempi.append(tempo)
                    print("il ciclista è stato aggiunto con successo")
                    corretto=True
            except:
                print("hai fatto un errore molto grave nell'aggiunta del tempo")
    elif scelta =="2":
        nome=input("inserisci il nome e cognome del ciclista al quale devi cambiare il tempo: ").strip()
        if nome in nomi:
            nome_indice=nomi.index(nome)
            corretto=False
            while not corretto:
                try:
                    tempo_nuovo=float(input("inserisci il tempo aggiornato dell'atleta (in secondi): "))
                    if tempo_nuovo<=8:
                        print("il tempo da te dichiarato è inferiore a 8 secondi ")
                    else:
                   
                        tempi[nome_indice]=tempo_nuovo
                        print("iltempo è stato aggiornato con successo")
                        corretto=True
                except:
                    print("hai fatto un errore molto grave nell'aggiunta del tempo")
    elif scelta =="3":
        for i in range(len(tempi)):
            print("Questa è la classifica")
            coppie.append((nomi[i],tempi[i]))
            coppie.sort(key=lambda x: x[1])
        for i in range (len(coppie)):
            (f'{i+1} nome e tempo:{coppie[i]}')
    elif scelta =="4":
        nome=input("inserisci il nome e cognome del ciclista da eliminare: ").strip()
        if nome in nomi:
            nome_indice=nomi.index(nome)
            nomi.pop[nome_indice]
            tempi.pop[nome_indice]
            
print("Arrivederci e buona giornata")
