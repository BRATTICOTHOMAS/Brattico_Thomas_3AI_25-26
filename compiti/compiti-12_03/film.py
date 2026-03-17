import os

# Costante per il nome del file
NOME_FILE = "compiti/compiti-12_03/archivio_film.txt"

def menu():
    print("-----------------------")
    print("    MOVIES TRACKER     ")
    print("-----------------------")
    print("1 - Inserisci film")
    print("2 - Visualizza film")
    print("3 - Modifica film")
    print("4 - Elimina film")
    print("0 - Esci e Salva")
    print("-----------------------")

def carica_dati():
    lista_temp = []
    if os.path.exists(NOME_FILE):
        try:
            with open(NOME_FILE, "r", encoding="utf-8") as file:
                for riga in file:
                    nome = riga.strip()
                    if nome != "":
                        lista_temp.append({"titolo": nome})
            print("Dati caricati dall'archivio.")
        except:
            print("Errore durante il caricamento.")
    return lista_temp

def salva_dati(lista):
    try:
        with open(NOME_FILE, "w", encoding="utf-8") as file:
            for film in lista:
                file.write(film["titolo"] + "\n")
        print("Dati salvati con successo.")
    except:
        print("Errore durante il salvataggio.")

def visualizza_film(lista):
    print("ELENCO FILM VISTI:")
    if len(lista) == 0:
        print("L'archivio è vuoto.")
    else:
        for i in range(len(lista)):
            # Usiamo i+1 per mostrare un elenco numerato naturale (1, 2, 3...)
            print(i + 1, "-", lista[i]["titolo"])

def inserisci_film(lista):
    nuovo_titolo = input("Inserisci il titolo del film: ")
    nuovo_titolo = nuovo_titolo.strip().capitalize()
    if nuovo_titolo != "":
        lista.append({"titolo": nuovo_titolo})
        print("Film aggiunto alla lista.")
    else:
        print("Titolo non valido.")

def modifica_film(lista):
    visualizza_film(lista)
    if len(lista) > 0:
        try:
            posizione = int(input("Inserisci il numero del film da modificare: ")) - 1
            if posizione >= 0 and posizione < len(lista):
                nuovo = input("Inserisci il nuovo titolo: ").strip().capitalize()
                lista[posizione]["titolo"] = nuovo
                print("Titolo aggiornato.")
            else:
                print("Posizione non trovata.")
        except ValueError:
            print("Errore: devi inserire un numero.")

def elimina_film(lista):
    visualizza_film(lista)
    if len(lista) > 0:
        try:
            posizione = int(input("Inserisci il numero del film da eliminare: ")) - 1
            if posizione >= 0 and posizione < len(lista):
                rimosso = lista.pop(posizione)
                print("Film rimosso.")
            else:
                print("Posizione non valida.")
        except ValueError:
            print("Errore: inserisci un numero.")

def main():
    archivio = carica_dati()
    
    # Usiamo una variabile di controllo invece del break
    continua_ciclo = True
    
    while continua_ciclo:
        print("") # Sostituisce il \n per creare spazio vuoto
        menu()
        scelta = input("Scelta: ")
        
        if scelta == "1":
            inserisci_film(archivio)
        elif scelta == "2":
            visualizza_film(archivio)
        elif scelta == "3":
            modifica_film(archivio)
        elif scelta == "4":
            elimina_film(archivio)
        elif scelta == "0":
            salva_dati(archivio)
            print("Arrivederci!")
            continua_ciclo = False # Portiamo la condizione a False per uscire
        else:
            print("Opzione non valida, riprova.")

# Avvio del programma
main()