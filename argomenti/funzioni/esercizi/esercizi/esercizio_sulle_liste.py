import random
l1 = []
n=0
try:
    while n!=10:
        interrogati=input("scrivi i possibili interrogati: ").replace(".", ",")
        l1.append(interrogati)
        print("-------------------------------")
        random.shuffle(l1) 
        n+=1
        for i in range(3):
            uno=random.choice(l1)
            due=random.choice(l1)
            tre=random.choice(l1)
except:
    print("errore")
