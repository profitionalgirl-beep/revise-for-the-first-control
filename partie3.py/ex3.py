"""
var n,s,som:entier
debut 
lire n 
s=0
pour i de 1 jusqu'a n
        s=s+i**2
    som =s
ecrire("la somme est ",som)
"""
while True :
    n=input ("saisire un nombre :")
    if n.isdigit():
        n=int(n)
        break 
s=0
for i in range (1,n+1):
    s+=i**2
som=s
print("la somme est ",som)