#Riscrivere il programma indicato sotto usando non più di 3/4 righe - deve funzionare sia con h positivo che negativo
h = int(input("Inserisci un numero H: "))
passo = 1 if h > 0 else -1
for i in range(0, h + (1 if h>0 else -1), passo): 
    print(i)