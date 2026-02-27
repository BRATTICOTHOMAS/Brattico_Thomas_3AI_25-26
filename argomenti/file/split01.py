f=open("argomenti/file/dati.dat", encoding="utf-8") # il punto (.) è il percorso attuale, i due punti(..) per il percorso precedente all'attuale,se uso slash verso sinistra bisogna raddoppiarlo (\\) invece se uso lo slash a destra (/)
#per il file le maiuscole o minuscole sono uguali, ma la codifica da noi presa come la utf-8 npìon codifichera alcuni caaratteri speciali o strani che non riesce a decodificare
righe = f.read()          #encoding è la codifica per le lettere accentate

p=righe.split(" ")
l=[]
#for s in p:    in caso si divide per una lettera gli spazi ci saranno ancora e si fa questo
#    l.append(s.strip())
print(len(p))
print(p)
#print(l)