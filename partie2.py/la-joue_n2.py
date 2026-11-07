import random
while True:
    print("pierre-papier-ciseaux")
    mx=input("saisire ton choix:")
    ox=random.choice(["pierre","papier","ciseaux"])
    print ("mon choix est:",mx)
    print("choix de l'ordinateure:",ox)
    if mx==ox:
        print("match nul")
    elif (mx=='papier' and ox=='pierre' ) or (mx=='pierre'and ox=='ciseaux') or (mx=='ciseaux' and ox=='papier'):
        print("excellent,tu es ganier ")
    else :
        print("l'ordinateur a gangne !")
        print("tu n'as pas eu de chance cette fois-ci, essaie encore!")
    rep=input("continue ou arreter")
    if rep =='arreter':
        print("merci d'avoir jouer! A bientot")