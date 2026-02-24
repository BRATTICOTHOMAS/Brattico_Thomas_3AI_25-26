#Viene visualizzato un menù di scelta nella quale sono mostrati articoli e relativi prezzi.
#  Esempio
# A - caffe 1.30 euro
# B - cappuccino 1.50 euro
#.......
# Z - fine acquisti
 
#L'utente preme l'articolo e questo viene erogato, mostrando la scritta "articolo erogato".
 
#Il programma mostra nuovamente il menù e si va avanti così fino
#  a che l'utente non seleziona la voce "Z - fine aquisti".
# A quel punto il programma mostra:
#1) totale euro degli articoli acquistati
#2) prezzo e nome dell'articolo meno costoso acquistato
#3) prezzo e nome dell'articolo più costoso acquistato

utente=str(input("scegli tra queste opzioni: "))
utente=utente.upper()
utente=utente.strip()
while utente!="Z":
    print("------------------------------")
    print("-------------CAFFE (1.30 euro)------------")
    print("-------------CAPPUCINO (1.50 euro)--------")
    print("-------------KINDER (1.80 euro)--------")
    print("-------------ACQUA (0.50 euro)--------")
    print("-------------Z (exit)----------")
    if utente=="CAFFE":
        print("l'articolo è stato erogato")
    if utente=="CAPPUCINO":
        print("l'articolo è stato erogato")
    if utente=="KINDER":
        print("l'articolo è stato erogato")
    if utente=="ACQUA":
        print("l'articolo è stato erogato")
print("fine acquisti")
    
