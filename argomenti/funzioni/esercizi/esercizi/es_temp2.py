#temperature ed eccezioni
import time
from datetime import datetime
inizio=datetime.now()
scelta= ""
tempMedia= 0
n_temp= 0
acc_temp=0
max=0
min=0
conta=0
while scelta !="F":
    print("----------------------------")
    print("1 - Inserici temperatura")
    print("2 - Visualizza temperatura media")
    print("3 - Conteggi")
    print("F - Fine programma")
    print("----------------------------")
    scelta= input("Cosa vuoi fare: ")
    if scelta == "1":
        errore =True
        try:
            t =float(input("temperatura misurata in °C 🌡(-20|+45): "))
            errore=False
        except:
            print("il dato inserito non può essere convalidato nel formato della temperatura ✍")
        if errore ==True or t>45 or t<-20:
            if errore==False:
                print("la temperatura è fuori dall' intervallo non sono consentite 🚨 ")
        else:
            acc_temp=acc_temp+t
            if n_temp == 0:
                max=t
                min=t  
            if max<t:
                max=t
            if min>t:
                min=t
            n_temp=n_temp+1
            tempMedia=acc_temp/n_temp
            print("temperatura acquisita")
    elif scelta== "2":
        if n_temp== 0:
            print("non sono ancora state inserite delle temperature percalcolare la temperatura media ✌️")
        else:
            print(f"la temperatura media è {tempMedia:.1f}°C")
            conta=conta+1
    elif scelta== "3":
        if n_temp==0:
            print("non hai inserito nessuna temperatura ❌🌡️")
        print(f"hai inserito (☞ ͡° ͜ʖ ͡°)☞ {n_temp} temperature")
        print(f" 🥶❄️ {min:.1f}°C e 🔥🥵 {max:.1f}°C")
    elif scelta== "user":
        print("\033[34m⌗ ωᥱℓᥴ𐐫꧑ᥱ ! questo programma è stato fatto da -Brattico Thomas- ╾━╤デ╦︻(•_- ).\033[0m")
    elif scelta=="ver":
            ora=datetime.now()
            print(f"{ora} 🕑")
    elif scelta =="22":
        print(f"hai visualizzato la media della temperatura {conta} 😎👌🔥")
    elif scelta=="tempo":
        print(f"tempo di esecuzione programma {ora-inizio} 🕑")
        