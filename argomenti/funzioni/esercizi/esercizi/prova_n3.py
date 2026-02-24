prodotto= str(input("metti il nome del prodotto: "))
prodotto.strip
lettere= len(prodotto) 
if lettere>15 or lettere<=3 or not prodotto.isalpha:
    print("il prodotto è invalido")
else:
    codice=input("metti il codice del prodotto (formato C00ccc): ").strip
    cod= len(codice) 
    if cod ==6:
        if codice[0]!=codice[0].upper or codice[1:3]!=codice[1:3] or codice!=codice.lower[4:6]:
            print ("il codice inserito è sbagliato")
        else :
            print("il codice è valido")
            prezzo=float(input("metti il prezzo del prodotto: "))
            if prezzo < 0.05 or prezzo > 12.50:
                print("metti un prezzo valido")
            else:
                print("il prezzo è valido")
                peso=float(input("metti il peso del prodotto in grammi: "))
                if peso<=3000:
                   print("il peso è valido ma non possiamo scontarti nulla")
                elif peso< 250:
                    print("il peso è valido e possiamo scontarti un ulteriore 3%")
                    prezzo_finale=prezzo-((prezzo * 3)/100)
                    print(f"questo è il prezzo finale: {prezzo_finale}")
                else:
                    print("il peso non è valido")
    else:
        print("il codice non è valido")
