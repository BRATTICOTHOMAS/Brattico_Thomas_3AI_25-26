#O(log(n)) è la complessita dell'algoritmo quindi all'aumentare 
# degli elementi la ricerca dicotonica è una delle migliori

def ricerca_dicotonica(l, n):
    #restituisce true se l'elemento cercato è nella lista,false se non ce
    i= 0
    f=len(l)-1
    while i!=f or l[m]==n:
    
        m=(i+f)//2
        if l[m]==n:
            return True
        if l[m] > n:
            m=m-1 #è bastato aggiungere m=m-1 e m=m+1 per far si che il numero controllato venisse coinvolto nello step successivo
            f=m
        elif l[m] <= n:
            m=m+1
            i= m
            
    return False
lista=[10,12,44,72,88,96,104,1000]
print(ricerca_dicotonica(lista,96))