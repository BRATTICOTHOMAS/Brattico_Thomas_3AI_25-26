f=open("ris.txt",mode="w", encoding="utf-8") # il punto (.) è il percorso attuale, i due punti(..) per il percorso precedente all'attuale,se uso slash verso sinistra bisogna raddoppiarlo (\\) invece se uso lo slash a destra (/)
#per il file le maiuscole o minuscole sono uguali, ma la codifica da noi presa come la utf-8 npìon codifichera alcuni caaratteri speciali o strani che non riesce a decodificare
f.write("ciao 3Ai")
f.write("\n Seconda frase")
n=125
f.write(f"\n parole trovate: {n}")
f.close()