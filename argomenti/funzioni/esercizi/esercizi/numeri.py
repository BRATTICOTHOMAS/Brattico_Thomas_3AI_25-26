A=int(input("metti un numero intero: "))
B=int(input("metti un numero intero: "))
C=int(input("metti un numero intero: "))

if A<B and B<C:
    print(f"il numero minore è: {A}" )
else:
    if B<A and A<C:
        print(f"il numero minore è: {B}" )
    else: 
        print(f"il numero minore è:{C} " )
M= (A + B + C)/3
print(f"La media  è:{M} " )
