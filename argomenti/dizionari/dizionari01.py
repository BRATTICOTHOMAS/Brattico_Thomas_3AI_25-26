#i dizionari sono una raccolta di informazioni,
#che attraverso una specifica chiave si puo avere di ritorno una o piu informazioni,
print("dizionario")
dati = {"conad" : 123, "esselunga": 200, "unes" : 103,
        "ginesi": 95, "coop":98 }#chiave e valore
print(dati)
print(dati["unes"])
dati["unes"] = dati["unes"] + 10
print(dati["unes"])

clienti = dati["itis"] =503 #per creare una nuova chiave con il suo valore effettivo

print(dati)

dati["itis"] = "buon anno" #quando la chiave cè sostituisce il valore
print(dati["itis"])
dati["esselunga"] =[1300,1800,1250,1125]#si può sostituire un valore qualsiasi anche con liste e dizionari

print(dati)
clienti= dati["esselunga"][2]#per prendere un dato da una lista di un dizionario
print(f"nella terza sede di esselunga ci sono {clienti} clienti")
#dati.clear()   rimuove  sia chiavi che valori dentro il dizionari (tutti)
k=dati.keys()#ti restituisce una lista delle chiavi presenti nel dizionario
dati["pagnoncelli"] =2320 #case sensitive
print(k)
for key in k:
    print(key)
c=sorted(dati.keys())#serve per riordinare le chiavi in ordine alfabeticodentro il dizionario
print(c)

dati.pop("esselunga")#serve per eliminare una chiave con il corrispetivo valore
print(dati)

if "pagnoncelli" in dati.keys() : #serve per verificare se una chiave è presente nel dizionario; case sensitive
    print("supermercato presente in archivio")
else:
    print("questo supermercato non è ancora stato registrato")