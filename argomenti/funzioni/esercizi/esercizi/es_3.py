#chiedere all'utente di inserire le età ed i nomi di 10 cani;
#  stampare l'età minima ed il relativo nome, l'età massima ed il relativo nome.
#  Verificare l'età inserita dall'utente ed il nome inserito dall'utente
# (solo lettere dalla a alla z, niente cifre o caratteri speciali;
#  sono però ammessi gli spazi)
for i in range(10):
    corretto=False
    while not corretto:
                eta= int(input(f"inserisci l'età del tuo cane {i+1}: ",))
                nome=input(f"inserisci il nome del tuo cane {i+1}: ",)
                try:
                    if eta < 0 and nome!=nome.isalpha():
                        print("età o nome non valido")
                    else:
                        corretto=True    
                except:
                    print("metti un eta reale o un nome reale")
                if i==0 or eta<minimo:
                    minimo=eta
                    mini=nome
                if i==0 or eta>=massimo:
                    massimo=eta
                    maxi=nome
                   
print(f"l'età massima è {massimo} ed il nome corrispondente è {maxi} .")
print(f"l'età minima è {minimo} ed il nome corrispondente è {mini} .")