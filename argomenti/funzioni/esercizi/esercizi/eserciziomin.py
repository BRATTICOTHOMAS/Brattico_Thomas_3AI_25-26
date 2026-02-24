#scrvi un programma python che chide all'utente di inserire 
#i prezzi di 10 articoli acquistati al supermercato
#alla fine stampa il prezzo dell'articolo pagato di meno

for i in range(10):
    #fase di input
    corretto=False
    while not corretto:
            prezzo= float(input(f"inserisci il prezzo del prodotto numero {i+1}: "))
            try:
                if prezzo < 0:
                    print("prezzo non valido")

                else:
                    corretto=True
            except:
                print("metti un numero reale")
    #fase di calcolo
    if i==0 or prezzo<minimo:
                minimo=prezzo
print(f"il prodotto meno costoso è di {minimo} euro.")
        
