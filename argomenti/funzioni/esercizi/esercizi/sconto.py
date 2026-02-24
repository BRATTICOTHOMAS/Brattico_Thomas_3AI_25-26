import random
pr=float(input('inserisci il prezzo:'))
cs=int(input('quanti sconti hai?(puoi inserire al massimo 3 sconti!):'))
if cs>3 and cs<1:
     print('errore---non puoi inserire più di tre codici sconto!')
else:
    print('----------------------------')
    print('1 - sconto del tipo 11-11')
    print('2 - sconto del tipo nome+n')
    print('3 - sconti fissi')
    print('----------------------------')
    scelta=input('scegli dal menù il tipo di sconto che possiedi:')
    if scelta=='1':
            if cs==1:
                sconto=random.randint(3,5)
                print(f'il tuo sconto è del {sconto} %')
                sf=(pr*sconto)/100
                pf=pr-sf
                print(f'il prezzo finale del tuo prodotto è {pf} euro')
            elif cs==2:
                    sconto=random.randint(3,5)
                    sconto1=random.randint(3,5)
                    print(f'i tuoi sconti sono  del {sconto},{sconto1} %')
                    scontotot=sconto+sconto1
                    sf=(pr*scontotot)/100
                    pf=pr-sf
                    print(f'il prezzo finale del tuo prodotto è {pf} euro')
            elif cs==3:
                sconto=random.randint(3,5)
                sconto1=random.randint(3,5)
                sconto2=random.randint(3,5)
                print(f'i tuoi sconti sono  del {sconto},{sconto1},{sconto2}  %')
                scontotot=sconto+sconto1+sconto2
                sf=(pr*scontotot)/100
                pf=pr-sf
                print(f'il prezzo finale del tuo prodotto è {pf} euro')
    if scelta=='2':
        if cs==1:
            s=input('inserisci per esteso il codice sconto(formato nome+n,sconti validi da una sola cifra!):')
            if s.isalnum()==False:
                print('hai inserito un codice non valido!')
            elif s[-2].isalpha()==False:
                print("non puoi inserire sconti composti da più cifre!")
            else:
                print(f'il tuo sconto è del {s[-1]}%')
        elif cs==2:
            s=input('inserisci per esteso il codice sconto n.1(formato nome+n,sconti validi da una sola cifra!):')
            s1=input('inserisci per esteso il codice sconto n.1(formato nome+n,sconti validi da una sola cifra!):')
            if s.isalnum()==False or s1.isalnum()==False:
                print('hai inserito un codice non valido!')
            if s[-2].isalpha()==False or s1[-2].isalpha()==False:
                print("non puoi inserire sconti composti da più cifre!")
            else:
                print(f'i tuoi sconti sono del {s[-1]}% e del {s1[-1]}%')
        elif cs==3:
            s=input('inserisci per esteso il codice sconto n.1(formato nome+n,sconti validi da una sola cifra!):')
            s1=input('inserisci per esteso il codice sconto n.2(formato nome+n,sconti validi da una sola cifra!):')
            s2=input('inserisci per esteso il codice sconto n.3(formato nome+n,sconti validi da una sola cifra!):')
            if s.isalnum()==False or s1.isalnum()==False or s2.isalnum()==False:
                print('hai inserito un codice non valido!')
            if s[-2].isalpha()==False or s1[-2].isalpha()==False or s2[-2].isalpha()==False:
                print("non puoi inserire sconti composti da più cifre!")
            else:
                print(f' i tuoi sconto sono del {s[-1]}% del {s1[-1]} e del {s2[-1]} %')
    if scelta=='3':
        if cs=='3':
            print('complimenti hai accesso a tutti e tre gli sconti')
            scontotot=0.12
            sf1=(pr*scontotot)/100
            pf1=pr-sf1
            print(f'il prezzo totale è {pf1}')
        elif cs=='2':
            print('complimenti hai accesso hai nostri due codici sconto!')
            scontotot=0.6
            sf2=(pr*scontotot)/100
            pf2=pr-sf2
            print(f'il prezzo totale è {pf2}')
        elif cs=='1':
            print('complimenti hai accesso ad un nostro coidce sconto!')
            sf3=(pr*0.1)/100
            pf3=pr-sf3
            print(f'il prezzo totale è {pf3}')