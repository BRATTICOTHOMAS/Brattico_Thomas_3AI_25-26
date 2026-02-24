# Esercizio 4: 10 Parole, visualizza le uniche
parole = []
print("Inserisci 10 parole.")
for i in range(10):
    parola = ""
    while not parola:
        parola = input(f"Inserisci la parola {i+1}/10: ").strip()
        if not parola:
            print("Errore: Non puoi inserire una parola vuota. Riprova.")
    parole.append(parola)
parole_uniche = set(parole) #visualizza parole uniche
if not parole_uniche:
    print("Nessuna parola è stata inserita.")
else:
    for x in parole_uniche:
        print(x)