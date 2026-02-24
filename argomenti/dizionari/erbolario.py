erbe={}
erbe["camomilla"] = {
    "nome":"camomilla", "luogo": "Dalmine", "sostanze" : ("limonene", "sost2","sost3"),
    "prezzo": 0.50, "quantita" : 100

}
erbe["mirtilla"] = {
    "nome":"mirtilla", "luogo": "Dalmine", "sostanze" : ("isocianati", "flavonoidi"),
    "prezzo": 0.40, "quantita" : 80

}
#meno dupplicati ho e meglio è
def inserisci(e):
    nome = input('Nome erba: ')
    if nome in e.keys():
        print("erba gia in archivio")
    else:
        luogo= input("luogo raccolta: ")
        prezzo=float(input("prezzo al grammo: "))
        qua= int(input("grammi in magazzino: "))
        sost=[]
        r=""
        while r != "n":
            r= input("ci sono sostanze chimiche da annotare? (s/n)")
            if r =="s":
                s=input("nome varietà chimica: ")
                sost.append(s)

        e[nome]={"nome":nome, "luogo": luogo, "sostanze" : tuple(sost),
            "prezzo": prezzo, "quantita" : qua}
print(erbe)
inserisci(erbe)
n=input("cosa vuoi cercare:")
l=erbe.keys()
for i in l:
    print(l)