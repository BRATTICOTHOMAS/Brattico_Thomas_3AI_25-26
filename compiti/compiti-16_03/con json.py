import json
import os

NOME_FILE_JSON = "compiti/compiti-16_03/archivio_film.json"

def carica_dati_json():
    lista_film = []
    if os.path.exists(NOME_FILE_JSON):
        file = open(NOME_FILE_JSON, "r", encoding="utf-8")
        # La funzione load ricostruisce automaticamente la lista di dizionari
        lista_film = json.load(file)
        file.close()
        print("Dati caricati dal file JSON.")
    return lista_film

def salva_dati_json(lista):
    file = open(NOME_FILE_JSON, "w", encoding="utf-8")
    # indent=4 serve per rendere il file leggibile anche a occhio nudo
    json.dump(lista, file, indent=4)
    file.close()
    print("Dati salvati con successo (formato JSON).")

def visualizza(lista):
    print("--- ARCHIVIO DIGITALE FILM ---")
    if not lista:
        print("Archivio vuoto.")
    else:
        for i in range(len(lista)):
            f = lista[i]
            print(i + 1, "-", f["titolo"], "| Anno:", f["anno"], "| Botteghino:", f["incasso"])

def main_json():
    film_visti = carica_dati_json()
    attivo = True
    
    while attivo:
        print("")
        print("--- MENU JSON ---")
        print("1-Aggiungi | 2-Mostra | 3-Cambia | 4-Rimuovi | 0-Salva ed Esci")
        azione = input("Operazione: ")
        
        if azione == "1":
            t = input("Titolo: ").capitalize()
            a = int(input("Anno: "))
            i = float(input("Incassi: "))
            film_visti.append({"titolo": t, "anno": a, "incasso": i})
        elif azione == "2":
            visualizza(film_visti)
        elif azione == "3":
            visualizza(film_visti)
            indice = int(input("Quale numero vuoi modificare? ")) - 1
            if 0 <= indice < len(film_visti):
                film_visti[indice]["titolo"] = input("Titolo: ").capitalize()
                film_visti[indice]["anno"] = int(input("Anno: "))
                film_visti[indice]["incasso"] = float(input("Incasso: "))
        elif azione == "4":
            visualizza(film_visti)
            indice = int(input("Quale numero vuoi eliminare? ")) - 1
            if 0 <= indice < len(film_visti):
                film_visti.pop(indice)
        elif azione == "0":
            salva_dati_json(film_visti)
            print("Dati archiviati. Arrivederci.")
            attivo = False
        else:
            print("Comando errato.")

main_json()