#le liste possono contenere al loro interno diversi tipi di dato anche tutti assieme 
# e i vari elementi vengono ordinati in base ad un indice proprio della lista,
#  in modo da semplificarne l'accesso.
import random
l1 = ["Brambilla", "Biffi", "Damian","Carrara", "sara", "Milani", "Lorenzi", "Oubada", "Alborghetti"] #lista messa in una variabile
random.shuffle(l1) #mischia la lista 
ok=random.choice(l1) # sceglie 1 a caso dalla lista 
l3=random.sample(l1,2) #ristampa n° oggetti/nomi/numeri dalla lista e ne crea una nuova di quest'ultima
print("lista potenziale di interrogati:")
print(l1[0]) #stampa solo l'oggetto/nome/numero desiderato scritto nelle []
print(l1[1])
print(l1[2])
print(l1[3])
print(l1[4])
print(l1[-1])
print("Interrogato:")
print(ok)
print(l3)
print(len(l1)) # fa visualizzare il numero totale di oggetti/nomi/numeri nella lista
print("---------------------------------------------")
l1.append("Alborghetti")# aggiunge alla lista uno o più oggetti/nomi/numeri 
print(l1)
print("------------------------")
l1.remove("Biffi") # rimuove dalla lista uno o più oggetti/nomi/numeri (Case sensitive)
print(l1)
l1.reverse() #ribalta la lista partendo dal fondo fino ad arrivare al primo e la stampa a schermo(non bisogna metterla nel print)
print("-----------------------")
print(l1)
l2=l1.count("Alborghetti") # conta il numero di oggetti/nomi/numeri uguali che ci sono in una lista (Case sensitive)
print("-----------------------")
print(l2)
l1[0] = "super Mario" # funziona = al replace per le stringhe ma è per le liste quindi sostituisce quell'oggetto con un altro dato da noi
print(l1)