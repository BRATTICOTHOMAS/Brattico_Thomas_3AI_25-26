p=float(input("digita il tuo peso espresso in kg (compreso tra 35 e 220)"))
h=float(input("digita la tua altezza espressa in cm (compreso tra 140 e 215)"))
if p < 35 or p>220 and h<140 or h>215:
    print("metti dei numeri validi")
else:
    IMC=(p*10000)/(h*h)
    if IMC < 16:
        print(f"Questo è il tuo IMC {IMC}")
        print("sei in sottopeso ... MANGIA")
    elif IMC>= 16 and IMC<=28:
        print(f"Questo è il tuo IMC {IMC}")
        print("Sei in normapeso ... continua così")
    elif IMC> 28 :
        print(f"Questo è il tuo IMC {IMC}")
        print("sei in sovrappeso... dimagrisci")