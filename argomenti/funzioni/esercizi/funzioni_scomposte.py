#collezzionare i manga che leggo di solito (nome fumetto)
#  nomi -->lista stringhe
#questa funzione si occupa di visualizzare il menu principale
def stampamenu():
    print("-----I MIEI FUMETTI--------------")
    print("scegli:")
    print("1 - per inserire il fumetto------")
    print("2 - per eliminare un fumetto-----")
    print("3 - modificare il nome di un fumetto")
    print("4 - visualizza i fumetti")
    print("0 - esci")

#questa funzione si occupa di:
# chiede all'utente la sua scelta
# controlla che la sceltasia valida
def scelta():
    corretto=False
    while not corretto:
        try:
            scelta= int(input("scelta : "))
            if scelta <0 or scelta >4:
                print("scelta non valida")
                corretto=False
            else:
                corretto=True
                return scelta
        except:
            print("Formato scelta non valido")
            corretto=False
def inserisciFumetto():
    corretto=False
    while not corretto:
        nome= input("inserisci il nome del fumetto").strip().capitalize()
        #TODO: da controllare se il fumetto è già presente
        if len(nome) == 0:
            print("nome fumetto non valido")
            corretto=False
        else:
            corretto=True
def eliminaFumetto():
    pass

def modificaFumetto():
    pass

def visualizzaFumetti():
    pass

def esci():
    pass

#TODO no loop infiniti --> cacca pupu
while True:
    stampamenu()
    s=scelta()#serve per raccoliere il valore restituito dalla funzione
    if s ==1:
        inserisciFumetto()
    elif s ==2:
        eliminaFumetto()
    elif s ==3:
        modificaFumetto()
    elif s==4:
        visualizzaFumetti()
    elif s==0:
        esci()
    print(f"hai scelto {s}")