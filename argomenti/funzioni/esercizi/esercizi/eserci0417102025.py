#scrivere un programma che chiede all'utente di inserire una stringa; stampare la striga nel formato maiuscola-minuscola alternato. Esempio:   input "Ciao a tutti", output "CiAo a tUtTi"   ;   input: "roSPO", output "RoSpO"
parola=input("inserisci una parola: ")
parola2= ""
for i, c in enumerate(parola):
    parola2 += c.upper() if i%2 ==0 else c.lower()
print(parola2)