"""
var n,s,som:entier
debut 
lire n 
N=1
pour i de 1 jusqu'a n
    N=N*i
ecrire("la somme de produit est: ",n,"!=",N)
"""
while True :
    n=input ("saisire un nombre :")
    if n.isdigit():
        n=int(n)
        break 
N=1
for i in range (1,n+1):
    N=N*i
print("la somme de produit est:",n,"!=",N)