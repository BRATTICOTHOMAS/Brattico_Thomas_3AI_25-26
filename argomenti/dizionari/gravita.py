#realizzare una funzione che prende in ingresso il nome di uno dei pianeti del sistema solare e 
# restituisce in uscita la costante di gravità (se il nome del pianeta è corretto, -1 se il nome è errato). 
import math
def ottieni_gravita(nome_pianeta):
    dati_pianeti = {
        "Mercurio": 3.7,
        "Venere": 8.87,
        "Marte": 3.71,
        "Terra": 9.81,
        "Giove": 24.79,
        "Saturno": 10.44,
        "Urano": 8.87,
        "Nettuno": 11.15
    }
    nome_standard = nome_pianeta.capitalize()
    if nome_standard in dati_pianeti:
        return dati_pianeti[nome_standard]
    else:
        return -1
print("--- CALCOLO TEMPO DI CADUTA SU VARI PIANETI ---")
print("Pianeti disponibili: Mercurio, Venere, Marte, Terra, Giove, Saturno, Urano, Nettuno")
pianeta_scelto = input("Inserisci il nome del pianeta: ")
g = ottieni_gravita(pianeta_scelto)
if g != -1:
    try:
        s = float(input("Inserisci l'altezza di caduta (in metri): "))
        if s >= 0:
            t = math.sqrt((2 * s) / g)
            print(f"Su {pianeta_scelto.capitalize()} (g={g}), un oggetto che cade da {s} metri")
            print(f"impiega {t:.2f} secondi per toccare il suolo.")
        else:
            print("L'altezza non può essere negativa.")
    except ValueError:
        print("Errore: Inserisci un numero valido per l'altezza.")
else:
    print("Errore: Pianeta non trovato nel sistema solare.")