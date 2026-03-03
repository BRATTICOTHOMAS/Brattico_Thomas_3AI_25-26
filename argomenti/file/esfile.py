#scrivi un programma python che dato come parametro
#a linea di comando il nome di un file, conta e stampa a schermo un
#messaggio di errore se il file non esiste (o è una cartella) 
#altrimenti restituisce il conteggio delle vocali.
import os
import sys
l=["a","e","i","o","u","A","E","I","O","U","ù","à","ò","è","é","ì"]
print("Arguments: ", sys.argv)
conta=0
p=input("aggiungi un parametro: ")
if os.path.isfile("..\\" + p) ==True:
    print("hai trovato un file")
    for i in p:
        if i in l:
            conta+=1 
else: 
    print("Non è un file") 