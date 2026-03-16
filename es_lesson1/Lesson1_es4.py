#Definire una funzione che prende come argomento una parola e una lettera e ritorna quante volte quella lettera è contenuta nella parola.
def conta_lettera(parola,lettera):
    i=int(0)
    for l in parola:
        if l==lettera:
            i+=1
    return i

print(conta_lettera("casa","a"))