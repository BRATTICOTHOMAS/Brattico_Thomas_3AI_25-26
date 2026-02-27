#REALIZZARE UN PROGRAMMA PYTHON IN GRADO DI RICEVERE 
# DUE PARAMETRI IN INGRESSO 
# IL PRIMO è IL NOME DEL FILE DA ELABORARE 
#IL SECONDO PARAMETRO è IL FILE CONTENENTE 
# L'ELENCO DELLE PAROLE DA CERCARE
#IL PROGRAMMA CONTA LE OCCORENZE DELLE PAROLE PRESENTI
#NELL'ELENCO DA CERCARE E SCRIVE I RISULTATI 
#IN UN FILE CHIAMATO RIS.TXT


#passi file con albero casa topo zaino
#conta delle parole in un file e le scrive su ris.txt
l={}
def elenco_parole():
    corretto=False
    while not corretto:
        scelta=input("hai parole che vuoi cercare (y/n): ").strip()
        if scelta=="y":
            parole=input("inserisci la parola che vuoi cercare").strip()
            l[parole]=0
        else:
            corretto=True

f=open("argomenti/file/biblioteca/biblioteca/Peter Pan.txt", encoding="UTF-8")
r=open("argomenti/file/ris.txt", encoding="UTF-8")
elenco_parole()
righe=f.read()
for key in l:
    p=f.count(l[key])
    
    l[key]+=p
    r.write(f"parola = {key}, trovate ={p}")
r.close()
f.close()

#TODO DA SISTEMARE