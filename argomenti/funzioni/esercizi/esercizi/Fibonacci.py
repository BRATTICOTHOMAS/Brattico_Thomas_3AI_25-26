primo=0 #inizializzazione variabili
secondo= 1
conta=1
while conta <10: #condizione di fine esecuzione
    terzo = primo + secondo
    print(terzo,end=" ")
    primo=secondo
    secondo=terzo
    conta = conta +1 #incremento 
    