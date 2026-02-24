import datetime, os

listafile = os.listdir(".")

for l in listafile:
    if ".txt" in l:
        print(l)

filename = input("file da elaborare:")

if os.path.exists(filename) == False:
    print("File non trovato")
    quit()

f = open(filename, "r", encoding="utf-8")

parola = input("Stringa da cercare:").lower()
conta = 0
vuote = 0
conDati = 0
nParole = 0
contaParola = 0
for r in f:
    r = r.strip()
    if parola in r.lower():
        nParole += 1
        contaParola += r.count(parola)
    if r == "":
        vuote += 1
    else:
        conDati += 1
    conta+=1
f.close()

fris = open("risultati.html", "w", encoding="utf-8")
fris.write("""<!DOCTYPE html><html lang="it"><head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Risultati</title>
    <style>
        .titolo{
            color:red;
            background-color: aquamarine;
            font-family: 'Verdana';
            font-weight: bold;
            font-size: 30px;
            padding:30px;
            text-align: center;
        }
        .risultati{
            background-color: beige;
            font-family: 'Courier New';
            font-size: 20px;
            padding: 20px;
        }
        .footer{
            color: #919191;
            background-color: #dcdcdc;
            text-align: center;
            padding-top: 10px;
            padding-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="titolo">
        Risultati dei conteggi
    </div>
    <div class="risultati">""")
fris.write(f"""File elaborato: <i>{filename}</i><br>""")
fris.write(f"Ho letto <b>{conta}</b> righe di cui <b>{vuote}</b> vuote e <b>{conDati}</b> con dati.<br>\n")
fris.write(f"Ho trovato <b>{nParole}</b> righe che contengono il termine {parola}<br>\n")
fris.write(f"Ho contato <b>{contaParola}</b> volta/e {parola}<br>\n")
d = datetime.datetime.now()
fris.write(f"""</div><div class="footer">&copy; {d.strftime("%d-%m-%Y")} - 3Ai Dalmine
    </div>
</body>
</html>""")

fris.close()

