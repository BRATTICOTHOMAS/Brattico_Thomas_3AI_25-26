#chiedere all'utente di inserire un numero: stampare tutti i numeri dispari compresi tra 1 ed il numero inserito dall'utente
numero=int(input("scrivi un numero per stampare a schermo tutti i numeri dispari prima del numeor stesso: "))
for i in range(1,numero+1,2):
    print(i)