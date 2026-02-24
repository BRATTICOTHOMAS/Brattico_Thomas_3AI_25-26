import random
 
blu= 7
verdi= 4
rosse= 2
palline = blu + verdi + rosse
estratta= random. randint(1, palline)
print(f"blu", blu/palline,)
print(f"rosse", rosse/palline,)
print(f"verdi", verdi/palline,)
 
c=(input("dimmi il colore della pallina(blu-verde-rosso): "))
if c != "blu" and c!= "rosso" and c!= "verde":
    print("devi inserire un colore valido, il colore era: ", estratta )
else:
    if(c== "blu" and estratta <= blu):
        print("hai vinto")
    elif(c== "rosso" and estratta<= rosse):
        print("hai vinto")
    elif(c== "verde" and estratta<= verdi):
        print("hai vinto")
    else:
        print("hai perso")