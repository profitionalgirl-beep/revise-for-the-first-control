"""
var n,sd,:entier
debut 
lire n 
sd=0
pour i de 1 jusqu'a n
        sd=sd+1/i
ecrire("la somme est ",sd)
"""
while True :
    n=input ("saisire un nombre :")
    if n.isdigit():
        n=int(n)
        break 
sd=0
for i in range (1,n+1):
    sd+=1/i
print("la somme est ",sd)