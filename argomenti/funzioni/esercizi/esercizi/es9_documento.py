f=str(input("inserisci una parola "))
f=f.lower()
n=0
for i,c in enumerate(f):
    if(c=="a" or c=="e" or c=="i" or c=="o" or c=="u" or c=="à" or c=="è" or c=="é" or c=="ì" or c=="ò" or c=="ù" ):
        if c:
            n=n+1
            print(n)