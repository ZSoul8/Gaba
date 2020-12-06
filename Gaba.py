import os
import random
import time

def main():
    print("Benvenuto in Gaba, un gioco rpg solo in linea di codice, se vuoi la grafica paga! Comunque apparte gli scherzi spero che il viaggio che stai per fare ti piaccia.\nP.S. ricordati di non morire, hai solo una vita.")
    time.sleep(4)
    print("Allora incomincia il tuo viaggio, qual è il tuo nome?")
    nome = input()
    os.system("cls")
    print(nome,"... che bel nome... sei sicuro che i tuoi genitori ti volevano bene?")
    time.sleep(2)
    print("Detto questo, in cosa ti identifichi (maschio,femmina,nonbinary,tostapane,gioco multipiattaforma,shrek,Optimus Prime ecc...)")
    genere = input()
    os.system("cls")
    print(genere,"""... interessante, che cosa vuoi essere?
    1 guerriero
    arma:spada arrugginita
    arma secondaria:scudo di legno
    vita:100
    agilità:30
    intelligenza:10""")
    

    
if __name__ == "__main__":
    main()
    