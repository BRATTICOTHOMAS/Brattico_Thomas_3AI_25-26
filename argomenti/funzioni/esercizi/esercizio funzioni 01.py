#Funzione=interfaccia formale, riutilizzabile;
#  con una firma. accetta parametri se dichiarati 
# nella definizione.
#print("ciao")
#print() #cosi va a capo
#print("Thomas")
import random
print()
print("ciao", end="X", sep=" - ")
print("3ai")
print(123)

n=random.randint(b=200,a=-20)#parametri posizionali obbligari 
#sempre prima i parametri posizionali, dopo quelli nominali obbligatoriamente
print(n)
#si puo fare una chiamata dentro una chiamata, ma devi avere il parametro di ritorno per restituire il valore
c=random.randint(random.randint(-20,20), random.randint(30,2000))
print(c)




def interrogato(numElenco):
    studenti={1 :"Alborghetti",2:"Bettinelli",3:"Biffi",4:"Brambilla",5:"Brattico",6:"Calliò",7: "Carrara A.",8: "Carrara G.",9: "Colombelli",10: "Crotti",11: "Crotti M." }
    print(numElenco)
    if numElenco in studenti:
        return studenti[numElenco]
    else: 
        raise Exception
try:    
    n=random.randint(1,27)
    print(f"l'interrogato è: {interrogato(n)}")
except:
    print("non è assagnato nessuno studente alla chiave ricevuta")