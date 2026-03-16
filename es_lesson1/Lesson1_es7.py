#7. Definire la funzione fattoriale (versione iterativa).
def factorial(num):
    res=1
    for i in range(2,num+1):
        res*=i
    return res

print(factorial(5))
print(factorial(0))
print(factorial(2))

print(factorial(4))