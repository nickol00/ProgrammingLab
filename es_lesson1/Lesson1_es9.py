#Definire una funzione che conta quante vocali sono presenti in una stringa.
def count_vocals(string):
    a={"a","A","e","E","i","I","o","O","u","U"}
    count=int(0)
    for letter in str(string):
        if letter in a:
            count+=1
    return count

print(count_vocals("Alpaca"))
print(count_vocals("tttrtr"))
print(count_vocals("puede"))