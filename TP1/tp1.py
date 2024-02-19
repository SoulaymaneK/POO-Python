"""
EX1 - programme qui calcule la surface d'un cercle en fonction de la saisie du rayon.
"""
from math import pi
def surface(r):
    surface = r*(pi**2)
    return surface 

r = float(input("entrez le rayon du cercle :"))
print("La surface du cercle est de",surface(r),"uni� d'air.")

"""
EX2 - programme qui demande deux nombres �  l'utilisateur et l'informe ensuite 
si leur produit est n�gatif ou positif.
"""
def test_prod(x,y):
    if x*y >0 :
        print("Le produit de",x,"et",y,"est positif")
    else: 
        print("Le produit de",x,"et",y,"est n�gatif")
        
x = int(input("entrez le premier nombre :"))
y = int(input("entrez le deuxi�me nombre :"))

test_prod(x,y)

"""
EX3 - programme qui calcule son factoriel en fonction d'un entier
"""
def factoriel(n):
    if n==0 : 
        return 1
    else :
        return n*factoriel(n-1)
n = int(input("entrez un nombre :"))
print("Factorielle de",n,":",factoriel(n))

"""
EX4 - Une ann�e est bissextile si elle est divisible par 4 mais non divisible par 100. 
Les ann�es divisibles par 400 sont �galement bissextiles.
"""
def bisextile(a):
    if a%4 == 0 and (a%100!=0 or a%400==0):
        print(a,"est une ann�e bisextile")
    else :
        print(a,"n'est pas une ann�e bisextile")

a = int(input("entrez une ann�e :"))
bisextile(a)

"""
EX5 - Ecrire un programme qui demande � l'utilisateur les coordonn�es de deux points dans le plan
 et qui calcul et puis affiche la distance entre ces points
selon la formule.
"""
from math import sqrt

def distance():
    print("entrez les coordonn�ez du point 1:")
    x1 = int(input("abscisse :"))
    x2 = int(input("ordonn�e :"))
    print("entrez les coordonn�es du point 2:")
    y1 = int(input("abscisse :"))
    y2 = int(input("ordonn�e :"))
    return sqrt(((x2-x1)**2)+((y2-y1)**2))

print("La distance entre les deux points est de :",distance())

"""
EX6 - D�clarer un tableau avec les valeurs [7, 5, 4, 9, 3] , et les trier par ordre croissant.
"""
def tri(tab):
    return tab.sort()

def tri2(tab):
    nb = len(tab)
    for d in range(nb):
        imin=d
        min=tab[d]
        for j in range(d+1, nb):
            if min > tab[j] :
                imin=j
                min=tab[j]
        tab[imin],tab[d] = tab[d], tab[imin]
    return tab

tab = [7,5,4,9,3]
print(tri(tab))