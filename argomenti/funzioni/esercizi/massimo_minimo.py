def minimo(a,b):
    if a<=b:
        return a
    else:
        return b
#scope = ambito di visibilità della variabile
def incrementa(a): #a è una variabile locale alla funzione
    global b #fa diventare una variabile da locale a globale; però --> produce un effetto collaterale --> cacca pupù
    a+=1
    b=7 #è una variabile locale alla funzione è la vede solo nella funzione

#prima sempre definizioni funzioni e poi scrivere il programma principale


a=10 #questa a invece è una variabile globale vengono viste sia dal programma principale e sia alle funzioni
b=20
m=minimo(a,b)
print(f"il minimo è {m}")
print(f"il valore a prima della funzione {a}")

i=incrementa(a)
print(f"il valore a dopo della funzione {a}")



#python incontra una variabile?
#prima guarda nello scope locale --> se la trova la Usa
#se non la trova, guarda nello scope globale --> se la trova la Usa
#se non la trova, guarda negli elementi built-in --> se la trova la Usa
#se non la trova --> eccezione NameError