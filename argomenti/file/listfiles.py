import os

d=os.getcwd() #current workin directory ovvero 
print(d)       #il percorso assoluto di lavoro 
fs= os.listdir(d) #stampa le cartelle e i file dentro la directory 
print(fs)
s= os.listdir(d+"/biblioteca") #stampa i libri nella biblioteca 
#aggiungendo al percorso attuale