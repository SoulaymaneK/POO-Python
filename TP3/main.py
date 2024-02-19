from TP3_EX2 import Personne
from TP3_EX3 import Point, TroisPoints

"""
Fonction main() pour l'exo 2
"""

def main2():
    p1 = Personne("Doe","John",30,"m")
    print("Entrez les informations de la deuxième personne.")
    p2 = Personne(input("nom : "), input("prenom : "), int(input("age : ")), input("sexe : "))
    p1.sameLastName(p2) 
   
    

"""
FonctionS main() pour l'exo 3
"""

def main3():
    p1 = Point(-1.,-3.)
    p2 = Point(5.,1.)
    print("La distance entre les deux points est de",p1.calculeDistance(p2))
    print("\nCoordonee du milieu :",p1.calculeMilieu(p2))

def main4():
    p1 = Point(0,0)
    p2 = Point(2,0)
    p3 = Point(1,2)
    p = TroisPoints(p1, p2, p3)
    print(p.sontAligne(p1, p2, p3))
    print(p.estIsocele(p1, p2, p3))

main2() 
main3()
main4()