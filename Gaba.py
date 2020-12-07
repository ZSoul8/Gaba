import os
import random
import time

#lista per il controllo degli input
lc=[]

#lista personaggio: 0 nome,1 genere,2 razza,3 classe,4 livello,5 esperienza,6 soldi
personaggio = []

#lista statistiche: 0 vita,1 attacco,2 agilità,3 difesa,4 intelligenza,5 mana
statistiche = []

#lista armatura: 0 elmo,1 corpetto,2 gambali,3 stivali
armatura = []

#lista armi: 0 arma primaria,1 arma secondaria
armi = []

#lista anelli: max[10]
anelli = []

#lista equipaggiamento:0 lista armatura,1 lista armi,2 lista anelli
equipaggiamento = [armatura,armi,anelli]

#lista inventario: max[50]
inventario = [] 

#lista giocatore: 0 lista personaggio,1 lista statistiche,2 lista equipaggiamento,3 lista inventario
giocatore = [personaggio,statistiche,equipaggiamento,inventario]

# Inizializzazione procedura main
def main():
    os.system("cls")
    print("Benvenuto in Gaba, un gioco rpg solo in linea di codice, se vuoi la grafica paga! Comunque apparte gli scherzi spero che il viaggio che stai per fare ti piaccia.\nP.S. ricordati di non morire, hai solo una vita.")
    time.sleep(4)
    print("Allora incomincia il tuo viaggio, qual è il tuo nome?")
    #input del nome
    personaggio.append(input().strip())
    os.system("cls")
    print(personaggio[0],"... che bel nome... sei sicuro che i tuoi genitori ti volevano bene?")
    time.sleep(2)
    print("Detto questo, in cosa ti identifichi (maschio,femmina,nonbinary,tostapane,gioco multipiattaforma,shrek,Optimus Prime ecc...)")
    #input del genere
    personaggio.append(input().strip())
    os.system("cls")
    print(personaggio[1],"... interessante...")
    time.sleep(1)
    lc.append(False)
    #while di controllo per la razza
    while not lc[0]:
        print("Che razza sei?\n1 umano\n2 orco\n3 elfo\n4 umanoide\n5 cyborg\n6 non-morto\n7 alieno")
        razza = input().lower().strip()
        if razza == "1" or razza == "umano":
            personaggio.append("umano")
            lc[0] = True
        elif razza == "2" or razza == "orco":
            personaggio.append("orco")
            lc[0] = True
        elif razza == "3" or razza == "elfo":
            personaggio.append("elfo")
            lc[0] = True
        elif razza == "4" or razza == "umanoide":
            personaggio.append("umanoide")
            lc[0] = True
        elif razza == "5" or razza == "cyborg":
            personaggio.append("cyborg")
            lc[0] = True
        elif razza == "6" or razza == "non-morto":
            personaggio.append("non-morto")
            lc[0] = True
        elif razza == "7" or razza == "alieno":
            personaggio.append("alieno")
            lc[0] = True
        else:
            os.system("cls")
            print("Inserisci una razza disponibile")
            time.sleep(1)
    os.system("cls")
    del lc[0]
    lc.append(False)
    #while di controllo per la classe
    while not lc[0]:
        print("""Che cosa vuoi essere?
        1 guerriero                           2 assassino
        statistiche:                          statistiche:
        vita: 100                             vita: 60
        attacco: 10                           attacco: 20
        agilità: 10                           agilità: 30
        difesa: 20                            difesa: 10
        intelligenza: 10                      intelligenza: 30
        mana: 0                               mana: 0
        equipaggiamento:                      equipaggiamento:
        elmo: elmo consumato                  elmo: cappuccio strappato
        corpetto: cotta di maglia             corpetto: mantello strappato
        gambali: pantalone di pelle           gambali: pantalone di pelle
        stivali: stivali di pelle             stivali: scarpe di pelle
        arma: spada arrugginita               arma: pugnale consumato
        arma secondaria: scudo di legno       arma secondaria: pugnale consumato

        3 mago                                4 arciere 
        statistiche:                          statistiche:
        vita: 70                              vita: 70
        attacco: 5                            attacco: 15
        agilità: 10                           agilità: 25
        difesa: 5                             difesa: 10
        intelligenza: 50                      intelligenza: 30
        mana: 100                             mana: 0
        equipaggiamento:                      equipaggiamento:
        elmo: cappuccio strappato             elmo: cappuccio strappato
        corpetto: mantello da apprendista     corpetto: mantello strappato
        gambali: pantaloni di pelle           gambali: pantaloni di pelle
        stivali: scarpe di pelle              stivali: scarpe di pelle
        arma: bastone scrauso                 arma: arco scrauso
        arma secondaria: libro incantato      arma secondaria: faretra scrausa
        """)
        classe = input().lower().strip()
        if classe == "1" or classe == "guerriero":
            personaggio.append("guerriero")
            lc[0] = True
        elif classe == "2" or classe == "assassino":
            personaggio.append("assassino")
            lc[0] = True
        elif classe == "3" or classe == "mago":
            personaggio.append("mago")
            lc[0] = True
        elif classe == "4" or classe == "arciere":
            personaggio.append("arciere")
            lc[0] = True
        else:
            os.system("cls")
            print("Inserisci una classe disponibile")
            time.sleep(1)
    os.system("cls")
               
if __name__ == "__main__":
    main()
