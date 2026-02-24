parola= input("scrivi una parola: ")
lettere= len(parola) 
print(f"la parola è composta da: ", lettere)
num= int(input("scrivi un numero intero compreso tra 0 e e il numero di lettere della parola -1: " ))
num2= int(input("scrivi un numero intero compreso tra 0 e e il numero di lettere della parola -1 e diverso dal numero precedente: " ))


if(num>=lettere and num2>=lettere or num<0 or num2<0):
    print("impossibile svolgere il programma")
else:
    print("la parola che hai scelto è: ", end="")
    print(parola[num:num2+1])