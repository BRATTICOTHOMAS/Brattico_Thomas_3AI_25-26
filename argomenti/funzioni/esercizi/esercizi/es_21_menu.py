from termcolor import colored, cprint
 
# La lista memorizza liste interne (righe di dati) usando la concatenazione:
# [nome, prezzo_unitario, quantita, spesa_totale]
attrezzature_acquistate = []
 
while True:
    cprint("\n====================================", 'blue')
    cprint("          GESTIONE ACQUISTI", 'blue')
    cprint("====================================", 'blue')
    print(colored("1. Inserisci attrezzature acquistate", 'green'))
    print(colored("2. Visualizza dati di riepilogo", 'yellow'))
    print(colored("3. Esci", 'red'))
    cprint("------------------------------------", 'blue')
    scelta = input(colored("Seleziona un'opzione (1-3): ", 'cyan')).strip()
    if scelta == '1':
        cprint("\n--- Inserisci Attrezzature Acquistate ---", 'yellow')
        dato_valido = False
        while not dato_valido:
            nome = input(colored("Inserisci il nome dell'attrezzatura: ", 'cyan')).strip()
            if nome:
                dato_valido = True
            else:
                cprint("Errore: Il nome dell'attrezzatura non può essere vuoto.", 'red')
        dato_valido = False
        while not dato_valido:
            try:
                prezzo_str = input(colored("Inserisci il prezzo  (in Euro, es. 350.50): ", 'cyan')).strip().replace(',', '.')
                prezzo_unitario = float(prezzo_str)
                if prezzo_unitario > 0:
                    dato_valido = True
                else:
                    cprint("Errore: Il prezzo deve essere maggiore di 0", 'red')
            except ValueError:
                cprint("Errore: Inserisci un numero decimale valido.", 'red')
        dato_valido = False
        while not dato_valido:
            try:
                quantita_str = input(colored("Inserisci il numero di attrezzature acquistate: ", 'cyan')).strip()
                quantita = int(quantita_str)
                if quantita > 0:
                    dato_valido = True
                else:
                    cprint("Errore: La quantità deve essere un intero positivo maggiore di 0.", 'red')
            except ValueError:
                cprint("Errore: Inserisci un numero intero valido.", 'red')
        spesa_totale_articolo = prezzo_unitario * quantita
        nuova_attrezzatura = [nome, prezzo_unitario, quantita, spesa_totale_articolo]
        attrezzature_acquistate = attrezzature_acquistate + [nuova_attrezzatura]
        cprint(f"Attrezzatura '{nome}' inserita con successo.", 'green')
        cprint(f"Spesa per questo articolo: {spesa_totale_articolo:.2f} Euro.", 'green')
    elif scelta == '2':
        cprint("--- Dati di Riepilogo ---", 'yellow')
        if not attrezzature_acquistate:
            cprint("Nessun dato inserito.", 'red')
        else:
            spesa_totale_generale = 0
            min_prezzo = float('inf')
            max_prezzo = float('-inf')
            item_min = None
            item_max = None
            somma_prezzi_unitari = 0
            totale_quantita = 0
            for item in attrezzature_acquistate:
                prezzo = item[1]
                quantita = item[2]
                spesa_totale = item[3]
                spesa_totale_generale += spesa_totale
                somma_prezzi_unitari += prezzo
                totale_quantita += quantita
                if prezzo < min_prezzo:
                    min_prezzo = prezzo
                    item_min = item
                if prezzo > max_prezzo:
                    max_prezzo = prezzo
                    item_max = item
            numero_articoli_distinti = len(attrezzature_acquistate)
            spesa_media_unitaria = 0
            if numero_articoli_distinti > 0:
                 spesa_media_unitaria = somma_prezzi_unitari / numero_articoli_distinti
            spesa_media_pesata = 0
            if totale_quantita > 0:
                spesa_media_pesata = spesa_totale_generale / totale_quantita
            print("-" * 40)
            cprint(f"Spesa Totale: {spesa_totale_generale:.2f} Euro", 'magenta')
            print("-" * 40)
            cprint("Nome e Prezzo Minimo degli Articoli:", 'blue')
            print(f"  Articolo: {colored(item_min[0], 'white')} | Prezzo  Minimo: {colored(f'{item_min[1]:.2f} Euro', 'green')}")
            cprint("Nome e Prezzo Massimo degli Articoli:", 'blue')
            print(f"  Articolo: {colored(item_max[0], 'white')} | Prezzo  Massimo: {colored(f'{item_max[1]:.2f} Euro', 'red')}")
            print("-" * 40)
            cprint("Spesa Media  (Media dei prezzi distinti):", 'blue')
            print(f"  Media: {colored(f'{spesa_media_unitaria:.2f} Euro', 'yellow')}")
            cprint("Spesa Media (Tenendo Conto delle Quantità Acquistate):", 'blue')
            print(f"  Media Pesata: {colored(f'{spesa_media_pesata:.2f} Euro', 'yellow')}")
            print("-" * 40)
    elif scelta == '3':
        cprint("Uscita dal programma. Arrivederci!", 'red')
    else:
        cprint("Scelta non valida. Inserisci 1, 2 o 3.", 'red')