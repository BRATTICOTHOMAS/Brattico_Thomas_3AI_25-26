f=open("file/biblioteca/biblioteca/Moby Dick.txt", encoding="utf-8") # il punto (.) è il percorso attuale, i due punti(..) per il percorso precedente all'attuale,se uso slash verso sinistra bisogna raddoppiarlo (\\) invece se uso lo slash a destra (/)
#per il file le maiuscole o minuscole sono uguali, ma la codifica da noi presa come la utf-8 npìon codifichera alcuni caaratteri speciali o strani che non riesce a decodificare
righe = f.read()          #encoding è la codifica per le lettere accentate


#print(righe)

#scrivo=f.write(s)
conta=righe.count("albero")
print(f"il numeroo di parole albero presenti sono: {conta}")

s=input("quale parola vuoi cercare: ")
if s in righe:
    conta2=righe.count(s)
    print(f"la parola {s} è apparsa {conta2}")
else: 
    print("non è presente")
    
f.close()#apro leggo/scrivo e chiudo per non avere handler aperti
