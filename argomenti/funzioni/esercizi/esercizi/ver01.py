#dati tre numeri interi inseriti dall'utente 
#calcolare media e il massimo dei tre
#msg di errore se i dati inseriti non sono interi
#msg di errore se un numero è minore di 10
#msg di avviso se più numeri sono uguali
n1= input("primo numero: ")
n2= input("secondo numero: ")
n3= input("terzo numero: ")
if n1.isdigit() == True and n2.isdigit() == True and n3.isdigit() == True:
    print("ok")
    n1= int(n1)
    n2= int(n2)
    n3= int(n3)
    if n1<10 or n2<10 or n3<10:
        print("è stato inserito almeno un numero minore di 10")
    else:
        if n1 == n2 or n1 == n3 or n2 == n3:
            print("almeno due numeri sono uguali tra di loro")
    
        if n1> n2 and n1>n3:
            print(n1)
        elif n2>n1 and n2>n3:
            print(n2)
        elif n3>n1 and n3>n2:
            print(n3)
else:
    print("i dati in ingresso devono contenere solo cifre.")