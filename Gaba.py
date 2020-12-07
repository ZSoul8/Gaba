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
    print(genere,"... interessante...")
    while True:
        time.sleep(2)
        razza=input("""Di che razza sei?:
1 umano

2 orco

3 elfo

4 umanoide

5 cyborg

6 nano

7 non-morto
""").lower()
        if (razza=="umano"or"orco"or"elfo"or"umanoide"or"cyborg"or"nano"or"non-morto"):
            break
        else:
            print("Razza inserita non valida, immettere una razza valida\n")
    os.system("cls")
    print("Un ",razza,"...")
    while True:
        time.sleep(2)
        classe=input("""Che cosa vuoi essere?:
1 guerriero
equipaggiamento:
elmo:
corpetto:cotta di maglia consumata
arma:spada arrugginita
arma secondaria:scudo di legno
statistiche:
vita:100
agilità:30
intelligenza:10

2 assassino
equipaggiamento:
statistiche:

3 mago
equipaggiamento:
statistiche:

4 arciere
equipaggiamento:
statistiche:
""").lower()
        if (classe=="guerriero"or"assassino"or"mago"or"arciere"):
            break
        else:
            print("Classe inserita non valida, immettere una classe valida\n")
    os.system("cls")
    print("Un ",classe,"...")

if __name__ == "__main__":
    main()
    
