import requests
import json

base_url = "https://fakeapi.net/products"
programma_attivo = True

while programma_attivo:
    
    print("ELENCO CATEGORIE")
    
    try:
        risposta_categoria = requests.get(base_url + "/categories")
        
        if risposta_categoria.status_code != 200:
            print("Errore nel contattare il servizio!")
            programma_attivo = False
        else:
            categorie = json.loads(risposta_categoria.text)
            
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
                    risposta_prodotto = requests.get(base_url + "/category/" + nome_categoria)
                    
                    if risposta_prodotto.status_code == 200:
                        dati_ricevuti = json.loads(risposta_prodotto.text)
                        prodotti = dati_ricevuti.get("data", [])
                        
                        print("PRODOTTI IN: " + nome_categoria.upper())
                        for prodotto in prodotti:
                            print("ID: " + str(prodotto.get("id")) + " | " + str(prodotto.get("title")) + " | Prezzo: " + str(prodotto.get("price")) + "€")
                        
                        scelta_id = input("Inserisci l'ID del prodotto per i dettagli (o INVIO per tornare indietro): ").strip()
                        
                        if scelta_id.isdigit():
                            risposta_nel_dettaglio = requests.get(base_url + "/" + scelta_id)
                            
                            if risposta_nel_dettaglio.status_code == 200:
                                dizionario_ricevuto = json.loads(risposta_nel_dettaglio.text)
                                
                                if "data" in dizionario_ricevuto:
                                    dati_prodotto = dizionario_ricevuto["data"]
                                else:
                                    dati_prodotto = dizionario_ricevuto

                                print("ID: " + str(dati_prodotto.get("id")))
                                print("NOME: " + str(dati_prodotto.get("title")))
                                print("PREZZO: " + str(dati_prodotto.get("price")) + "€")
                                print("DESCRIZIONE: " + str(dati_prodotto.get("description")))
                                print("CATEGORIA: " + str(dati_prodotto.get("category")))
                                print("BRAND: " + str(dati_prodotto.get("brand")))
                                print(" ")
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