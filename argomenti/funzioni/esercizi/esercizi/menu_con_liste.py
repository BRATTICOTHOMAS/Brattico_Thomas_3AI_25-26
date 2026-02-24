# menu con campionamenti, visualizza dati, esci.
# realizzare un programma implementando le seguenti funzonalità:
# memorizzare i mm di neve (float)
# memorizzare quanta neve è caduta
# quanti campionamenti fatti?
# se ci sono almeno tre misure consecutive > 2 stampo a schermo allerta neve.
from termcolor import cprint, colored
l3=[]
scelta=""
campionamenti=0
nevetot=0
n=0
while scelta !="E":
    print(colored("------------------", "white"))
    print(colored("A - inserisci dati sulla neve (in mm)", "cyan"))
    print(colored("B - visualizza dati sulla neve e quanti campionamenti hai fatto", "blue"))
    print(colored("E - EXIT", "red"))
    print(colored("------------------", "white"))
    try:
        l1=["A", "B","B"]
        scelta=input(colored("scegli tra A,B,E: ", "white"))
        scelta=scelta.strip().upper()
        l2=l1.count(scelta)
    except:
        "metti una scelta valida tra A,B,E"
    if l2==1:
        corretto=False
        while not corretto:
            neve=float(input(colored("inserisci la quantità di neve rilevata (in mm): ", "cyan")).replace(",", ".").strip())
            try:
                if neve > 0 and neve <=2 :
                   
                    print(colored("memorizzato il dato", "green"))
                    corretto=True
                    nevetot+=neve
                    n+=1
                    l3.clear()
                elif neve > 2:
                   
                    print(colored("il dato è stato memorizzato correttamente", "green"))
                    corretto=True
                    campionamenti+=1
                    nevetot+=neve
                    n+=1
                    l3.append("neve")
                elif neve < 0 :
                    print(colored("non c'è neve", "light_yellow"))
                    corretto=True
                    n+=1
            except:
                print(colored("inserisci un dato valido", "red"))
    if l2==2:
        l4=l3.count("neve")
       
        if l4>=3:
            print(colored("ALLERTA NEVE", "red"))
            print(colored(f"la neve che ci sarà è {nevetot:.2f} mm", "white"))
            print(colored(f"i campionamenti effettuati sono {n}", "blue"))
        else:
            print(colored(f"la neve che ci sarà è {nevetot:.2f} mm", "white"))
            print(colored(f"i campionamenti effettuati sono {n}", "blue"))