"""
var n:entier
lire n
pour e de 1 jusqua n
    ecrire "*"*e
fin

    """
while True :
    n=input("saisire le nombre des etoile")
    n=int(n)
    break
s="0"
for e in range(1,n+1):
    s=str(e)
    print (s*e)