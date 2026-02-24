#chiedere all'utente di inserire un numero: stampare tutti i numeri dispari compresi tra 1 ed il numero inserito dall'utente; visualizzare i numeri al contrario. Esempio: numero di input = 10 --> 9 7 5 3 1
numero=int(input("scrivi un numero per sapere l'ordine inverso tipo(9 7 5 3 1):"))
for i in range(numero,0,-1):
    if i%2 != 0:#se i %2 è diverso da 0 scrivilo 
        print(i)