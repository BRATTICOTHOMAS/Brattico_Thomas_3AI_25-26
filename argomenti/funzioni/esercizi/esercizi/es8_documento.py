import random
n=0
d=0
d2=0
d3=0
while(n<7):
    d=random.randint(1,6)
    if n==1 or n==4:
        print(f"il primo dado è: {d}")
    if n==2 or n==5:
        d2=d
        print(f"il secondo dado è {d2}")
    elif n==3 or n==6:
        d3=d
        print(f"il terzo dado è {d3}")
    
        somma=d+d2+d3
        print(f"la somma è: {somma}")
    n=n+1
    
print("i primi tre numeri sono dell'utente e gli ultimi tre del computer")
    