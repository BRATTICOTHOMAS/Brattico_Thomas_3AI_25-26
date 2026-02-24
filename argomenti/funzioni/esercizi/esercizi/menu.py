from datetime import datetime 
import random
scelta= ""
vinte = 0
perse= 0
while scelta !="X":
    print("--------------------------")
    print("1 - lancio dadi")
    print("2 - dataora")
    print("3 - ")
    print("X - exit")
    print("--------------------------")
    print("cosa vuoi fare?", end="")
    scelta = input().strip().upper()
    if scelta =="1":
        pass
        for i in range(200):
            dado1= random.randint(1,6)
            dado2= random.randint(1,6)
        print(f"il lancio ha dato {dado1} e {dado2}", end="")
        

        if dado1 ==6 and dado2 ==6:
            print("hai vinto")
            vinte = vinte + 1
            
        else:
            print("hai perso")
            perse=perse+1
            pvinte=vinte/(vinte+perse)
            pperse=perse/(vinte+perse)
            print(f"le statistiche: tot{vinte+perse} vin {vinte} perc {pvinte:.0%}", end="")
            print(f"pers {perse} {pperse:.0%}")
    elif scelta=="2":
        print(datetime.now())
        pass
    elif scelta =="X":
        print("bye bye")
    else:
        print("scelta inesistente")
