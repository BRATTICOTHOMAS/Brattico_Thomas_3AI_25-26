def giorno_settimana():
    giorni = {
        1: "Lunedì",
        2: "Martedì",
        3: "Mercoledì",
        4: "Giovedì",
        5: "Venerdì",
        6: "Sabato",
        7: "Domenica"
    }
    print("--- GIORNI DELLA SETTIMANA ---")
    try:
        numero = int(input("Inserisci un numero da 1 a 7: "))
        if numero in giorni:
            print(f"Il giorno {numero} corrisponde a: {giorni[numero]}")
        else:
            print("Errore: Il numero deve essere compreso tra 1 e 7.")
    except ValueError:
        print("Errore: Devi inserire un numero intero!")
giorno_settimana()