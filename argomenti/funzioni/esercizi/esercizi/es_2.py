#chiedere all'utente di inserire diverse età di cani;
#l'input deve andare avanti fino a che l'utente non inserisce lo 0.
#A quel punto visualizzare età minima ed età massima inserite
corretto=False
i=0
while not corretto:
            eta= int(input("inserisci l'età del tuo cane : "))
            try:
                if eta < 0 :
                    print("età non valida")
                else:
                        if eta == 0:
                              corretto=True    
            except:
                print("metti un eta reale")
            if i==0 and eta<minimo:
                minimo=eta
            if i==0 and eta>=massimo:
                massimo=eta
print(f"l'età massima è {massimo} ")
print(f"l'età minima è {minimo}.")