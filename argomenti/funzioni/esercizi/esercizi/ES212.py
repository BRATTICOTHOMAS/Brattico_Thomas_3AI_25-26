#chiedere all'utente di inserire diverse età di cani;
#l'input deve andare avanti fino a che l'utente non inserisce lo 0.
#A quel punto visualizzare età minima ed età massima inserite

corretto=False
i=0
while not corretto:
            eta= int(input(f"inserisci l'età del tuo cane {i+1}: "))
            try:
                if eta < 0 :
                    print("età non valida")
                if eta >25:
                       print("eta non puo essere maggiore di 25")
                else:
                        if eta == 0:
                              corretto=True    
            except:
                print("metti un eta reale")
            
            if (i==0 or eta<minimo) and eta!=0:
                    minimo=eta
            if i==0 or eta>=massimo:
                    massimo=eta
            conta+=1
if conta>1:
    print(f"l'età massima è {massimo} ")
    print(f"l'età minima è {minimo}.")
 