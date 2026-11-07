import random
scrtnb = random.randint(1,100)
while True:
    while True:
        n=input("saisire le nombre secret: ")
        n=int(n)
        break
    if n==scrtnb:
        print( "Excellent !")
        break
    elif n>scrtnb:
        print ("Trop grand ")
    else:
        print("Trop petit ")
    
