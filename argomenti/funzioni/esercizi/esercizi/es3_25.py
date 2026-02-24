# Esercizio 3: 10 Numeri, visualizza i pari
numeri = []
print("Inserisci 10 numeri interi.")
for i in range(10):
    n=True
    while n:
        try:
            num_str = input(f"Inserisci il numero {i+1}/10: ")
            num = int(num_str)
            numeri.append(num)
            n=False
        except ValueError:
            print("Errore: Devi inserire un numero intero valido. Riprova.")
print("\n--- Numeri pari inseriti ---")
numeri_pari_trovati = False
for num in numeri:
    if num % 2 == 0:
        print(num)
        numeri_pari_trovati = True
if not numeri_pari_trovati:
    print("Nessun numero pari è stato inserito.")