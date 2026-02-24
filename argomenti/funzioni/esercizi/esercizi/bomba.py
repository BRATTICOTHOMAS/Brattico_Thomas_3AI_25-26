import random
personaggio=random.randint(0,9)
bomba= random.randint(0,9)
if personaggio != bomba:
    print(f"sei al blocco {personaggio}")
    print("il terreno è lungo 9 partendo da 0")
    print("stai attento alla bomba che è li con te da qualche parte")
else:
    print("sei esploso")