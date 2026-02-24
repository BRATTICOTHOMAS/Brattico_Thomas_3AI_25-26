parola= input("scrivi una parola: ")
lettere= len(parola) 
print(f"la parola è composta da: ", lettere)
num= int(input("scrivi un numero intero compreso tra 0 e e il numero di lettere della parola -1: " ))

if(num>=lettere):
    print("impossibile svolgere il programma")
else:
    print("la lettera che hai scelto è: ", end="")
    print(parola[num])