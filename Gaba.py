import os
import random
import time

lc=[]
giocatore = []
personaggio = []


# Inizializzazione procedura main
def main():
    print("Benvenuto in Gaba, un gioco rpg solo in linea di codice, se vuoi la grafica paga! Comunque apparte gli scherzi spero che il viaggio che stai per fare ti piaccia.\nP.S. ricordati di non morire, hai solo una vita.")
    time.sleep(4)
    print("Allora incomincia il tuo viaggio, qual è il tuo nome?")
    personaggio.append(input())
    os.system("cls")
    print(personaggio[0],"... che bel nome... sei sicuro che i tuoi genitori ti volevano bene?")
    time.sleep(2)
    print("Detto questo, in cosa ti identifichi (maschio,femmina,nonbinary,tostapane,gioco multipiattaforma,shrek,Optimus Prime ecc...)")
    genere = input()
    os.system("cls")
    print(genere,"... interessante...")
    lc.append(False)
    while not lc[0]:
        print("che razza sei?\n1 umano\n2 orco\n3 elfo\n4 umanoide\n5 cyborg\n6 non-morto\n7 alieno")
        

if __name__ == "__main__":
    main()
