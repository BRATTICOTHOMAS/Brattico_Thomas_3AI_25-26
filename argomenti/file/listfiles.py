import os
import sys
print("Arguments: ", sys.argv)

#rilascia una lista con una stringa

d=os.getcwd() #current workin directory ovvero 
print(d)       #il percorso assoluto di lavoro 
fs= os.listdir(d) #stampa le cartelle e i file dentro la directory 
print(fs)
#s= os.listdir(d+"\\biblioteca") #stampa i libri nella biblioteca 
#aggiungendo al percorso attuale

#un file è un contenitore logico di informazioni digitali.


if os.path.isfile(".\\biblioteca\\ris2.txt") ==True:
    print("hai trovato un file")
else: 
    print("Non è un file") 
if os.path.exists("C:\Windows\Cursors")==True:
    print("hai trovato qualcosa su disco")
else: 
    print("percorso inesistente")


















