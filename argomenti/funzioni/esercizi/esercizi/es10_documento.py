parola=input("inserisci una parola: ")
n=len(parola)
parola=parola.lower()
n=0
for i,c in enumerate(parola):
    if not (c=="a" or c=="e" or c=="i" or c=="o" or c=="u" or c=="à" or c=="è" or c=="é" or c=="ì" or c=="ò" or c=="ù" ):
            n=n+1
            print(n)