"""
Var d,v:reel
Var t:entier
debut
lire d
lire t
v=d/(t/60)
si v<8 alors
    ecrire "Vitesse faible pour cet objectif "
sinon si v<12 alors
    ecrire"Vitesse modérée "
sinon si v<16 alors
    ecrire"Bonne vitesse moyenne "
sinon alors
    ecrire"Vitesse moyenne élevée "
finsi
fin
"""
while True:
    d =input("saisire la distance en km")
    if d.isdigit():
        d=int(d)
        break
while True:
    t=input("saisire le temps en min")
    if t.isdigit():
        t=int(t)
        break
v=d/(t/60)
if v<8 :
    print("Vitesse faible pour cet objectif ")
elif v<12 :
    print("Vitesse modérée ")
elif v<16 :
    print("Bonne vitesse moyenne ")
else:
    print("Vitesse moyenne élevée ")