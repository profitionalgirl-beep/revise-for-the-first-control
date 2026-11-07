"""
var n,s,som:entier
debut 
lire n 
s=0
pour i de 1 jusqu'a n
    si i%2==0 alors
        s=s+i
ecrire("la somme est ",s)
"""
while True :
    n=input ("saisire un nombre :")
    if n.isdigit():
        n=int(n)
        break 
s=0
for i in range (1,n+1):
    if i%2==0:
        s+=i
print("la somme est ",s)