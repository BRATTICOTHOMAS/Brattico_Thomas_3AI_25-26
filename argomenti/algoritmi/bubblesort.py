def bubblesort(listadaordinare):
    n=len(listadaordinare)
    for i in range(n-1):
        for h in range(n-i-1):
            if listadaordinare[h]> listadaordinare[h+1]:
                listadaordinare[h], listadaordinare[h+1]= listadaordinare[h+1], listadaordinare[h]
def bubblesortmag_a_min(listadaordinare):
    n=len(listadaordinare)
    for i in range(n-1):
        for h in range(n-i-1):
            if listadaordinare[h]< listadaordinare[h+1]:
                listadaordinare[h], listadaordinare[h+1]= listadaordinare[h+1], listadaordinare[h]
def bubblesort_con_strutturedati_complesse(listadaordinare):
    n=len(listadaordinare)
    for i in range(n-1):
        for h in range(n-i-1):
            if listadaordinare[h]["cognome"]> listadaordinare[h+1]["cognome"]:
                listadaordinare[h], listadaordinare[h+1]= listadaordinare[h+1], listadaordinare[h]
            elif listadaordinare[h]["cognome"]==listadaordinare[h]["cognome"]:
                if listadaordinare[h]["nome"] > listadaordinare[h+1]["nome"]: 
                    listadaordinare[h], listadaordinare[h+1]= listadaordinare[h+1], listadaordinare[h]
lista=[5,9,12,1,0,25,-25,-6]

print(lista)
bubblesortmag_a_min(lista)
print(lista)
bubblesort(lista)#funziona anche se la lista è vuoto o con numeri uguali
#utilizziamo la bubblesort al posto della sort 
# perche se ci sono delle strutture dati complesse la sort va a bloccarsi e dare errore 
# oppure quando abbiamo delle parole con le parole in maiuscolo  metterà sempre prima quelle in maiusc e non le ordinerà correttamente come vogliamo.
#invece nella bubblesort basta mettere .upper()
print(lista)

lista2=[{"nome": "Alessio", "cognome":"rsso"}, {"nome":"giuseppe", "cognome":"aato"}]
bubblesort_con_strutturedati_complesse(lista2)
print(lista2)
#se devo utilizzare le strutture dati complesse 
#TODO UTILIZZARE SEMPRE BUBBLESORT