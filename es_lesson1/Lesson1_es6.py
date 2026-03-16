# Scrivere un programma che fa la somma di n numeri inseriti dall’utente. Di all'utente di scrivere 0 per
# fermarsi.
sum=float(0)
num=float(1)
while num!=float(0):
    num=float(input("Inserisci numero da sommare (0 per smettere): "))
    sum+=num
print("Sa somma è:",sum)