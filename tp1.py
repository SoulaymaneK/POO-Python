"""
EX1 - programme qui calcule la surface d'un cercle en fonction de la saisie du rayon.
"""
from math import pi
def surface(r):
    surface = r*(pi**2)
    return surface 

r = float(input("entrez le rayon du cercle :"))
print("La surface du cercle est de",surface(r),"unié d'air.")

"""
EX2 - programme qui demande deux nombres Ã  l'utilisateur et l'informe ensuite 
si leur produit est négatif ou positif.
"""
def test_prod(x,y):
    if x*y >0 :
        print("Le produit de",x,"et",y,"est positif")
    else: 
        print("Le produit de",x,"et",y,"est négatif")
        
x = int(input("entrez le premier nombre :"))
y = int(input("entrez le deuxième nombre :"))

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
EX4 - Une année est bissextile si elle est divisible par 4 mais non divisible par 100. 
Les années divisibles par 400 sont également bissextiles.
"""
def bisextile(a):
    if a%4 == 0 and (a%100!=0 or a%400==0):
        print(a,"est une année bisextile")
    else :
        print(a,"n'est pas une année bisextile")

a = int(input("entrez une année :"))
bisextile(a)

"""
EX5 - Ecrire un programme qui demande à l'utilisateur les coordonnées de deux points dans le plan
 et qui calcul et puis affiche la distance entre ces points
selon la formule.
"""
from math import sqrt

def distance():
    print("entrez les coordonnéez du point 1:")
    x1 = int(input("abscisse :"))
    x2 = int(input("ordonnée :"))
    print("entrez les coordonnées du point 2:")
    y1 = int(input("abscisse :"))
    y2 = int(input("ordonnée :"))
    return sqrt(((x2-x1)**2)+((y2-y1)**2))

print("La distance entre les deux points est de :",distance())

"""
EX6 - Déclarer un tableau avec les valeurs [7, 5, 4, 9, 3] , et les trier par ordre croissant.
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