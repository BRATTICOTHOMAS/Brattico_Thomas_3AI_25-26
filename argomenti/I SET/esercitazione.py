#per costruire un banco mi serve martello, chiodi, colla vinilica, legno
#abbiamo Alborghetti(legno, colla) e Gabriel (chiodi, martello, colla)
#dobbiamo chiedere all'utente cosa vuoi realizzare e anche cosa gli servira
#poi l'utente chiede cosa porta la prima persona e la seconda
#e a questo punto lui dira se si puo fare o no

Alborghetti=set()
Gabriel=set()
necessario=set()
no=False
costruzione=input("COSA VUOI COSTRUIRE? : ").strip()
while not no:
    try:
        necessito=input("aggiungi gli elementi necessario:(uno alla volta) ")
        necessario.add(necessito)
        scelta=int(input("hai altro da aggiungere 1=si o 2=no"))
        if scelta== 2:
            no=True
    except:
        print("FORMATO NON VALIDO")
no=False
while not no:
    try:
        
        pers1=input("aggiungi gli elementi che porta Alborghetti:(uno alla volta) ")
        Alborghetti.add(pers1)
        scelta=int(input("hai altro da aggiungere 1=si o 2=no"))
        if scelta== 2:
            no=True
    except:
        print("FORMATO NON VALIDO")
no=False
while not no:
    try:
        
        pers2=input("aggiungi gli elementi che porta Alborghetti:(uno alla volta) ")
        Gabriel.add(pers2)
        scelta=int(input("hai altro da aggiungere 1=si o 2=no"))
        if scelta== 2:
            no=True
    except:
        print("FORMATO NON VALIDO")

materiali_totali=Alborghetti.union(Gabriel)

if materiali_totali==necessario:
    print(f"puoi fare {costruzione}")
else:
    print("non puoi fare nulla...")