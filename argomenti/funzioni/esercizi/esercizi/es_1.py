#chiedere all'utente di inserire le età di 10 cani;
#stampare l'età minima e l'età massima.
#Verificare l'età inserita dall'utente
for i in range(10):
    corretto=False
    while not corretto:
            eta= int(input(f"inserisci l'età del tuo cane {i+1}: "))
            try:
                if eta < 0:
                    print("età non valida")
 
                else:
                    corretto=True
            except:
                print("metti un eta reale")
    if i==0 or eta<minimo:
                minimo=eta
    if i==0 or eta>=massimo:
        massimo=eta
print(f"l'età massima è {massimo} ")
print(f"l'età minima è {minimo}.")