"""
var d,c,e:entier
lire d
lire c
e=d*c
si e<100 :
    ecrire "Dépense estimée faible "
sinon si e<250 alors
    ecrire "Dépense estimée modérée "
sinon si e<500 alors
    ecrire "Dépense estimée importante"
sinon alors
    ecrire "Dépense estimée élevée"
fin si
fin

"""
d=int(input("saisire la durée en minutes: "))
c=int(input("saisire le  dépense énergétique estimée par minute"))
e=d*c
if e<100 :
    print("Dépense estimée faible ")
elif e<250 :
    print("Dépense estimée modérée ")
elif e<500 :
    print("Dépense estimée importante")
else :
    print("Dépense estimée élevée")