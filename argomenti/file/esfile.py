#scrivi un programma python che dato come parametro
#a linea di comando il nome di un file, conta e stampa a schermo un
#messaggio di errore se il file non esiste (o è una cartella) 
#altrimenti restituisce il conteggio delle vocali.
import os
import sys
l=["a","e","i","o","u","A","E","I","O","U","ù","à","ò","è","é","ì"]
print("Arguments: ", sys.argv)

p=input("aggiungi un parametro: ")
if os.path.isfile(".\\biblioteca\\ris2.txt") ==True:
    print("hai trovato un file")
else: 
    print("Non è un file") 