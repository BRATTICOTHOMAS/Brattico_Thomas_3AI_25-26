def calcolaOlio(quantitaPesto):
    return quantitaPesto * 2
def calcolaPinoli(quantitaPesto):
    return quantitaPesto * 3
def calcolaBasilico(quantitaPesto):
    return quantitaPesto * 5
print("--- CALCOLATORE INGREDIENTI PESTO ---")
try:
    richiesta = input("Quanti grammi di pesto vuoi produrre? ")
    grammi_pesto = float(richiesta)
    if grammi_pesto > 0:
        olio_necessario = calcolaOlio(grammi_pesto)
        pinoli_necessari = calcolaPinoli(grammi_pesto)
        basilico_necessario = calcolaBasilico(grammi_pesto)
        print(f"Per produrre {grammi_pesto}g di pesto ti servono:")
        print(f"- {olio_necessario} grammi di olio")
        print(f"- {pinoli_necessari} pinoli")
        print(f"- {basilico_necessario} foglie di basilico")
    else:
        print("Errore: Inserire una quantità maggiore di zero.")
except ValueError:
    print("Errore: Devi inserire un numero valido!")