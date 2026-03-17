import os

NOME_FILE_TXT = "compiti/compiti-16_03/archivio_film.txt"
SEPARATORE = ";"

def carica_dati_txt():
    lista_film = []
    if os.path.exists(NOME_FILE_TXT):
        file = open(NOME_FILE_TXT, "r", encoding="utf-8")
        for riga in file:
            # Rimuoviamo gli spazi bianchi e dividiamo la stringa
            dati = riga.strip().split(SEPARATORE)
            if len(dati) == 3:
                film = {
                    "titolo": dati[0],
                    "anno": int(dati[1]),
                    "incasso": float(dati[2])
                }
                lista_film.append(film)
        file.close()
        print("Dati caricati dal file di testo.")
    return lista_film

def salva_dati_txt(lista):
    file = open(NOME_FILE_TXT, "w", encoding="utf-8")
    for film in lista:
        # Costruiamo la riga unendo i campi con il separatore
        riga = str(film["titolo"]) + SEPARATORE + str(film["anno"]) + SEPARATORE + str(film["incasso"])
        file.write(riga + "\n")
    file.close()
    print("Dati salvati con successo (formato TXT).")

def visualizza(lista):
    print("--- ELENCO FILM ---")
    if len(lista) == 0:
        print("Nessun film presente.")
    else:
        for i in range(len(lista)):
            f = lista[i]
            print(i + 1, "-", f["titolo"], "Anno:", f["anno"], "Incasso:", f["incasso"], "€")

def inserisci(lista):
    titolo = input("Inserisci titolo: ").capitalize()
    anno = int(input("Inserisci anno: "))
    incasso = float(input("Inserisci incasso: "))
    lista.append({"titolo": titolo, "anno": anno, "incasso": incasso})
    print("Film aggiunto.")

def main():
    film_visti = carica_dati_txt()
    continua = True
    
    while continua:
        print("")
        print("1-Inserisci | 2-Visualizza | 3-Modifica | 4-Elimina | 0-Esci")
        scelta = input("Scegli: ")
        
        if scelta == "1":
            inserisci(film_visti)
        elif scelta == "2":
            visualizza(film_visti)
        elif scelta == "3":
            visualizza(film_visti)
            pos = int(input("Indice da modificare: ")) - 1
            if 0 <= pos < len(film_visti):
                film_visti[pos]["titolo"] = input("Nuovo titolo: ").capitalize()
                film_visti[pos]["anno"] = int(input("Nuovo anno: "))
                film_visti[pos]["incasso"] = float(input("Nuovo incasso: "))
        elif scelta == "4":
            visualizza(film_visti)
            pos = int(input("Indice da eliminare: ")) - 1
            if 0 <= pos < len(film_visti):
                film_visti.pop(pos)
        elif scelta == "0":
            salva_dati_txt(film_visti)
            continua = False
            print("Chiusura programma.")
        else:
            print("Scelta non valida.")

main()