#cosa succede se dichiaro 2 set con gli stessi elementi
#ma in posizione differenti if a==b mi darà vero o falso? VERO
#se aggiungo due volte lo stesso elemento ad un set e poi lo stampo,
#quante volte compare quell'elemento? 1 VOLTA
#quando stampo un set vedo gli elementi nello stesso ordine con cui
#li ho inseriti? NO
#posso fare la union di due set? si
#posso fare l'intersezione tra due set? si
#posso fare la differenza tra due set? si
#posso sapere se un elemento c'è o non c'è dentro uno specifico set?  if 2 in set: vero o falso
#posso sapere quanti elementi ha un set? 
#posso creare un set vuoto e poi aggiungere elementi? si

A=set() #serve per creare un nuovo set vuoto
A.add("ciaoo")
A.add("abc")
A.add("abc") #TODO ATTENZIONE UNO ALLA VOLTA 
A.add("ciccio")#serve per aggiungere numeri,stringhe,tuple e booleane.poiche non si puo aggiungere liste,dizionari o altri set che posso variare
print(A)
#PER ELIMINARE UN ELEMENTO ci sono due metodi:
#1 
A.remove("ciccio")#TODO ATTENZIONE SE LA VARIABILE NON C'è RITORNA UN ERRORE quindi TRY and EXCEPT
#2
A.discard("ciasawsa")#è PIù SICURO DEL REMOVE POICHE ANCHE SE NON C'è LA VARIABILE NON LANCIA NESSUN ERRORE
print(A)

B={"ciaoo","abc"}
print(B)
if A==B:
    print("VERO")
else:
    print("FALSO")

lista=list(A)#serve per far diventareun dizionario/set una lista

B.add("dajaifacac")
B.add("afuysaucvus")
#UNIONI CON I SET
UNIONE= A | B #serve per unire due set TODO ATTENZIONE NO LISTE/TUPLE

print(UNIONE)
print(A.union(B))#Un altro metodo per unire i set ma possibile anche unire un set con liste/tuple
print(A.update(B))#TODO ATTENZIONE MODIFICA IL SET ORIGINALE, ma si puo unire con liste e tuple

#INTERSEZIONE CON I SET
INTERSEZIONE= A & B #Serve per trovare gli elementi comuni (intersezione) tra due set 
#TODO ATTENZIONE NON ACCETTA LISTE E TUPLE
print(INTERSEZIONE)
print(A.intersection(B))#é UGUALE AD A & B MA é PIù FLESSIBILE perche accetta liste e tuple
print(A.intersection_update(B))#TODO ATTENZIONE non crea un nuovo set come i precedenti ma aggiorna il set togliendo tutti gli elementi non in comune con il secondo set

#DIFFERENZA TRA SET 
DIFFERENZA= A - B #SERVE PER TOGLIERE GLI ELEMENTI UGUALI CHE CI SONO DAL PRIMO SET AL SECONDO SET E LASCIA GLI ELEMENTI CHE CI SONO DAL PRIMO SET
print(DIFFERENZA)
print(A.difference(B))#é UGUALE AD A - B MA é PIù FLESSIBILE perche accetta liste e tuple
print(A.difference_update(B))