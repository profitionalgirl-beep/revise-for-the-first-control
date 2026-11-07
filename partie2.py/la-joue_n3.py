import random
s=0
sp=0
sim=0
for i in range (1,6):
    de=random.randint(1,6)
    s+=1
    print(f"le resultat de lancer N{i} est :{de}")
    if de%2==0:
        sp+=1 
    else:
       sim+=1
print ("le nombre des lancement est :",s)
print ("le nombre des resultat paire",sp )
print ("le nombre des resultat impaire",sim )

