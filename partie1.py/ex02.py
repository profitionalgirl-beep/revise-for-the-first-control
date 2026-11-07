"""
var p,t:reel
debut
lire p
lire t
imc=p/(t**2)
si imc<18,5 alors
    ecrire"Insuffisance pondérale"
sinon si imc<25 alors
    ecrire "Corpulence dite normale chez l’adulte"
sinon si imc<30 alors
    ecrire "Surpoids chez l’adulte "
sinon alors
    ecrire "Obésité chez l’adulte "
finsi
fin
"""
while True :
    p=input("saisire ton poid: ")
    if p.isdigit():
        p=int(p)
        break
t=float(input("saisire ton taille: "))
imc=p/(t**2)
if imc<18.5 :
    print("Insuffisance pondérale")
elif imc<25 :
    print("Corpulence dite normale chez l’adulte")
elif imc<30 :
    print("Surpoids chez l’adulte ")
else:
    print("Obésité chez l’adulte ")