#Scrivere un programma che verifica se un numero inserito dall’utente è pari o dispari
x=input("inserire un numero:")
par=int(x)%2
if par:
    print(x," è dispari")
else:
    print(x," è pari")