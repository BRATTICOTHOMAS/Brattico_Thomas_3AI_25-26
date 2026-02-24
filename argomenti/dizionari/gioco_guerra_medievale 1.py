import random
import time
from termcolor import colored, cprint
facce_dadi = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅"
}
def stampa_barra_cavalieri(nome, n_cavalieri, colore):
    simbolo = "♞" * n_cavalieri
    testo_colorato = colored(f"Cavalieri {nome} ({n_cavalieri}): {simbolo}", colore)
    print(testo_colorato)
def lancia_dado():
    return random.randint(1, 6)
cprint("♞♞♞ GUERRA MEDIEVALE ♞♞♞", 'white', )
print("Benvenuti nell'arena.")
nome_rosso = input(colored("Giocatore 1 (Armata ROSSA) inserisci nome: ", "red"))
nome_blu = input(colored("Giocatore 2 (Armata BLU) inserisci nome: ", "blue"))
cavalieri_rosso = 15
cavalieri_blu = 15
turno = 1
while cavalieri_rosso > 0 and cavalieri_blu > 0:
    print("-" * 40)
    cprint(f"TURNO {turno}", "cyan")
    if turno % 2 != 0:
        attaccante_nome = nome_rosso
        attaccante_colore = "red"
        difensore_nome = nome_blu
        difensore_colore = "blue"
        cprint(f"Attacca {attaccante_nome} (Rosso) -> Si difende {difensore_nome} (Blu)", "yellow")
    else:
        attaccante_nome = nome_blu
        attaccante_colore = "blue"
        difensore_nome = nome_rosso
        difensore_colore = "red"
        cprint(f"Attacca {attaccante_nome} (Blu) -> Si difende {difensore_nome} (Rosso)", "yellow")
    stampa_barra_cavalieri(nome_rosso, cavalieri_rosso, "red")
    stampa_barra_cavalieri(nome_blu, cavalieri_blu, "blue")
    print(f"{attaccante_nome}, tocca a te!")
    input(colored("Premi INVIO per lanciare i dadi...", ))
    valore_att = lancia_dado()
    valore_dif = lancia_dado()
    dado_att = facce_dadi[valore_att]
    dado_dif = facce_dadi[valore_dif]
    print(f"{attaccante_nome} lancia: {dado_att} ({valore_att})")
    print(f"{difensore_nome} lancia: {dado_dif} ({valore_dif})")
    if valore_att > valore_dif:
        danno = valore_att - valore_dif
        cprint(f"COLPO A SEGNO! {difensore_nome} perde {danno} cavalieri.", "green", attrs=['bold'])
        
        if difensore_colore == "red":
            cavalieri_rosso = max(0, cavalieri_rosso - danno)
        else:
            cavalieri_blu = max(0, cavalieri_blu - danno)
    else:
        cprint("DIFESA RIUSCITA! Nessun cavaliere perso.", "magenta")
    turno += 1
print("="*40)
if cavalieri_rosso > 0:
    vincitore = colored(f"VINCE L'ARMATA ROSSA DI {nome_rosso.upper()}!", "red")
    print(vincitore)
    print(f"Cavalieri rimasti: {cavalieri_rosso}")
else:
    vincitore = colored(f"VINCE L'ARMATA BLU DI {nome_blu.upper()}!", "blue")
    print(vincitore)
    print(f"Cavalieri rimasti: {cavalieri_blu}")