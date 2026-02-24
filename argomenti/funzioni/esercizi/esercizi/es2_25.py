# Esercizio 2: Giorni della settimana (Con Liste)
giorni_settimana = [
    "Lunedì", "Martedì", "Mercoledì", "Giovedì",
    "Venerdì", "Sabato", "Domenica"]
try:
    numero = int(input("Inserisci un numero da 1 a 7: "))
    if 1 <= numero <= 7:
        print(giorni_settimana[numero - 1])
    else:
        print("Errore: Il numero deve essere compreso tra 1 e 7.")
except ValueError:
    print("Errore: Devi inserire un numero intero.")