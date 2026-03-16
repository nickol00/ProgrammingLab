# 1. Stampare l’equivalente di 538 minuti nel formato 8h:58min.
minuti=538.0
ore=minuti//60
minuti=minuti-(ore*60)
print(ore.__int__(),"h:",minuti.__int__(),"min", sep="")