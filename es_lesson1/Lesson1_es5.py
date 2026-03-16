#Scrivere un programma che verifica se un numero inserito dall’utente è primo
def is_primo(n):
    num=int(n)
    upper=(int(num)//2)+1
    for i in range(2,upper):
        if(num%i==0): return False
    return True

n=input("Inserisci un numero: ")
if(is_primo(n)):
    print(n,"è primo")
else:
    print(n,"non è primo")