import requests
import json

base_url = "https://fakeapi.net/products"

def ottieni_lista_categorie():
    risposta = requests.get(base_url + "/categories")
    if risposta.status_code == 200:
        return json.loads(risposta.text)
    return None

def ottieni_prodotti_categoria(nome_categoria):
    risposta = requests.get(base_url + "/category/" + nome_categoria)
    if risposta.status_code == 200:
        dati = json.loads(risposta.text)
        return dati.get("data", [])
    return None

def ottieni_dati_prodotto(identificativo):
    risposta = requests.get(base_url + "/" + identificativo)
    if risposta.status_code == 200:
        dizionario = json.loads(risposta.text)
        if "data" in dizionario:
            return dizionario["data"]
        return dizionario
    return None

def stampa_scheda_prodotto(dati_prodotto):
    print("ID: " + str(dati_prodotto.get("id")))
    print("NOME: " + str(dati_prodotto.get("title")))
    print("PREZZO: " + str(dati_prodotto.get("price")) + "€")
    print("DESCRIZIONE: " + str(dati_prodotto.get("description")))
    print("CATEGORIA: " + str(dati_prodotto.get("category")))
    print("BRAND: " + str(dati_prodotto.get("brand")))
    print(" ")

programma_attivo = True

while programma_attivo:
    print("ELENCO CATEGORIE")
    try:
        categorie = ottieni_lista_categorie()
        
        if categorie is None:
            print("Errore nel contattare il servizio!")
            programma_attivo = False
            continue

        i = 1
        for categoria in categorie:
            print(str(i) + " - " + str(categoria))
            i = i + 1

        scelta_categoria = input("Quale categoria vuoi visualizzare? (0 per uscire): ").strip()

        if scelta_categoria == "0":
            programma_attivo = False
        elif scelta_categoria.isdigit():
            indice = int(scelta_categoria) - 1
            
            if 0 <= indice < len(categorie):
                nome_categoria = categorie[indice]
                prodotti = ottieni_prodotti_categoria(nome_categoria)
                
                if prodotti is not None:
                    print("PRODOTTI IN: " + nome_categoria.upper())
                    for prodotto in prodotti:
                        print("ID: " + str(prodotto.get("id")) + " | " + str(prodotto.get("title")) + " | Prezzo: " + str(prodotto.get("price")) + "€")
                    
                    scelta_id = input("Inserisci l'ID del prodotto per i dettagli (o INVIO per tornare indietro): ").strip()
                    
                    if scelta_id.isdigit():
                        dati_prodotto = ottieni_dati_prodotto(scelta_id)
                        if dati_prodotto:
                            stampa_scheda_prodotto(dati_prodotto)
                            input("Premi INVIO per tornare al menu...")
                        else:
                            print("ID non trovato.")
                else:
                    print("Errore nel caricamento prodotti.")
            else:
                print("Numero categoria non presente in elenco.")
        else:
            print("Inserimento non valido.")
            
    except:
        print("ERRORE DI CONNESSIONE O FORMATO")
        programma_attivo = False