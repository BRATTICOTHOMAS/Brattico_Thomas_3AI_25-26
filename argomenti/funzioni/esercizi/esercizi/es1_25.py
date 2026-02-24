# Esercizio 1: Giorni della settimana (Senza Liste)
try:
    numero = int(input("Inserisci un numero da 1 a 7: "))
    if numero == 1:
        print("Lunedì")
    elif numero == 2:
        print("Martedì")
    elif numero == 3:
        print("Mercoledì")
    elif numero == 4:
        print("Giovedì")
    elif numero == 5:
        print("Venerdì")
    elif numero == 6:
        print("Sabato")
    elif numero == 7:
        print("Domenica")
    else:
        print("Errore: Il numero deve essere compreso tra 1 e 7.")
except ValueError:
    print("Errore: Devi inserire un numero intero.")
print("-" * 30 )