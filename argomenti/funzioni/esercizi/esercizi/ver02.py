#dati in ingresso distanza in km e tempo di percorrenza in minuti
#calcolarela velocità media

d= float(input("distanza (km) :"))
t= input("tempo (minuti): ")
if t.isdigit() == True:
    t=int(t)
    if d<5 or d>790 or t<=0:
        print("i dati inseriti non sono nel range adeguato")
    else:
        v = (d*60)/ t 
        print(F"{v} km/h")
        if v<=30:
            print("zona 30")
        elif v>30 and v<=110:
            print("extra-urbana")
        elif v>110:
            print("autostrada")
else:
    print("il tempo deve eseere un numero intero")

   


