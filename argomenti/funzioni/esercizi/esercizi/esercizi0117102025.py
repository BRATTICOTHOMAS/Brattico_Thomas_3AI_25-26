#chiedere all'utente di inserire un numero: stampare tutti i numeri pari compresi tra 1 ed il numero inserito dall'utente
numero = int(input("Inserisci un numero: "))
for i in range(2, numero+1, 2):
    print(i)
