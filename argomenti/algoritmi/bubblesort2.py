import random
def bubblesort(listadaordinare):
    n=len(listadaordinare)
    for i in range(n-1):
        for h in range(n-i-1):
            if listadaordinare[h]> listadaordinare[h+1]:
                listadaordinare[h], listadaordinare[h+1]= listadaordinare[h+1], listadaordinare[h]
lista=[]
for i in range(1000000):
    lista.append(random.randint(1,1000000))
#bubblesort(lista)
lista.sort()
print(lista)