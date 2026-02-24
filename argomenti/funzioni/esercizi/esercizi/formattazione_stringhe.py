#formattazione dell'output
numero= 0.03
print(f"percentuale di prova {numero*3:.0%}")

prezzo=59.598
print(f"il prezzo è {prezzo:.2f}$")

print(f"l'universo è di {13000000000:,} anni")
dec = 9

luce=299792458
print(f"la luce viaggia a{luce:e} m/s")
bina= 0b11001100
print(f"il numero 9 in binario è {9:b}")
print(f"il num {bina:b} in decimale è { bina :d}")
num= 16
print(f"il numero in esadecimale è {num: x} hex")
print("basi :  \u2082 \u2088 ")
x= 10
y= 20 
print(f"{x} è maggiore di {y}? {x>y}")
frase= "oggi è una bella giornata in 3Ai"
print(f"{frase}")
t= -5
print(f"{t:=8}")
t=11
print(f"{t:=8}")
t=9
print(f"{t:=8}")

n="Sara"
print(f"studente/essa 3Ai: {n:>10}")
n="Leo"
print(f"studente/essa 3Ai: {n:>10}")
n="Gianfrancesco"
print(f"studente/essa 3Ai: {n:>10}")
n= "Thomas"
print(f"studente/essa 3Ai: {n:_^20}")
a="aquila"
print(f"la mia barca è piena di {a!r}")
patatine=100
print(f"{patatine=}")
