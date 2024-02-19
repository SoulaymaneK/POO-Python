"""
KEBLI Soulaymane 
TAHIRIR Mohamed 

TP 4 B Mercredi 10h15 - 12h15

"""

"""
EX1 - GoogleMaps 

Dans ce programme on cherche à recuperer les coordonnese gps d'une adresse (sa latitude et sa longitude.
Pour cela on utilise la galsse Gmap et sa méthode coordgps() qui renvoie la latitude et la longitude d'un lieu. 
On cree ensuite une classe Lieu et sa méthode detail qui renvoie toutes ses caractéristisques.

""" 
import googlemaps 

class Gmap:
    def coordgps(adresse):
        gmaps = googlemaps.Client(key='AIzaSyBTeRxf61DWGHagCM2SOVupUhdo2POEkxE') 
        geocode_result = gmaps.geocode(adresse)
        try : 
            lat = geocode_result[0]["geometry"]["location"]["lat"]
            lng = geocode_result[0]["geometry"]["location"]["lng"]
        except IndexError: 
            raise IndexError("Cette adresse n'existe pas!")
        return lat,lng 

class Lieu :
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse
        self.__latitude,self.__longitude = Gmap.coordgps(self.adresse)

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self,nom):
        if not isinstance(nom,str):
            raise TypeError ("L'adresse doit être de type str!")
        self.__nom = nom
    
    @property
    def adresse(self):
        return self.__adresse

    @adresse.setter
    def adresse(self,adresse):
        
        if not isinstance(adresse,str):
            raise TypeError ("L'adresse doit être de type str!")
        self.__adresse = adresse

    def detail(self):
        print(f"Nom : {self.nom}\nAdresse : {self.adresse}\nLatitude et Longitude : ({self.__latitude}, {self.__longitude})")

"""
EX2 - Class Personne 

Dans ce programme, on cherche à creer une class de type Personne qui prend en attribut lenom, prenom, age et sexe
d'une personne.
On cree ensuite des méthodes qui permettent de comparer et retourner si deux personnes ont le meme nom de famille, 
et de savoir quel est la personne la plus agee. 
"""
class Personne : 
    def __init__(self, nom, prenom, age, sexe):
        
        if not isinstance(nom, str):
            raise TypeError ("Le nom doit être de type str")
        self.__nom = nom
        
        if not isinstance(prenom, str):
            raise TypeError ("Le prenom doit être de type str")
        self.__prenom = prenom
        
        if not isinstance(age, int) :
            try:
                age = int(age)
            except ValueError:
                raise ValueError ("L'age doit etre de type int")
        if age < 0 :
            raise ValueError ("L'age doit etre un entier positif!")
        self.__age = age
         
        if not isinstance(sexe, str):
            raise TypeError ("Le nom doit être de type str") 
        if sexe.lower() in ["m","monsieur","h","homme","masculin"]:
            self.__sexe = "Monsieur"
        elif sexe.lower() in ["f","madame","femme","feminin"]:
            self.__sexe = "Madame"
        else : 
            raise ValueError ("Le genre n'est pas reconnu")
        
    def getnom(self):
        return self.__nom
    
    def getprenom(self):
        return self.__prenom
    
    def getage(self):
        return self.__age
       
    def getsexe(self):
        return self.__sexe
            
    def sameLastName(self,p):
        if not isinstance(p, Personne):
            raise TypeError ("L'argument entré n'est pas une personne!")
        if self.getnom().lower() == p.getnom().lower():
            return True
        else : 
            return False
    
    def oldest(self,p):
        if not isinstance(p, Personne):
            raise TypeError ("L'argument entré n'est pas une personne!")
        if self.getage() >= p.getage():
            return self       
        else :
            return p 
        
    
    #en plus 
    def __str__(self):
        return f"{self.getsexe()} {self.getprenom()} {self.getnom()} ({self.getage()} ans)"
    
"""
EX3 - Point 

"""
from math import sqrt 


class Point : 
    def __init__(self,abs,ord):
        self.abs = abs 
        self.ord = ord 
        
    @property 
    def abs(self):
        return self.__abs 
    
    @abs.setter 
    def abs(self,abs):
        if not (isinstance(abs, float) or isinstance(abs,int)):
            raise TypeError ("L'abscisse doit être de type float")
        self.__abs = abs 
        
    @property 
    def ord(self):
        return self.__ord
    
    @ord.setter 
    def ord(self,ord):
        if not (isinstance(ord, float) or isinstance(ord,int)):
            raise TypeError ("L'abscisse doit être de type float")
        self.__ord = ord
    
    def calculeDistance(self,p):
        return sqrt((p.abs - self.abs)**2 + (p.ord - self.ord)**2)
    
    def calculeMilieu(self,p):
        return Point( (self.abs + p.abs) / 2 , (self.ord + p.ord) / 2)

    #en plus
    def __str__(self):
        return f"({self.abs} ,{self.ord})"
    
    
class TroisPoints:
    def __init__(self, p1 , p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    @property 
    def p1(self):
        return self.__p1
    
    @p1.setter 
    def p1(self,p1):
        if not isinstance(p1, Point):
            raise TypeError ("Le point p1 doit être de type Point")
        self.__p1 = p1
        
    @property 
    def p2(self):
        return self.__p2
    
    @p2.setter 
    def p2(self,p2):
        if not isinstance(p2, Point):
            raise TypeError ("Le point p1 doit être de type Point")
        self.__p2 = p2
    
    @property 
    def p3(self):
        return self.__p3
    
    @p3.setter 
    def p3(self,p3):
        if not isinstance(p3, Point):
            raise TypeError ("Le point p1 doit être de type Point")
        self.__p3 = p3
    
    def sontAligne(self):
        p1p2 = self.p1.calculeDistance(self.p2)
        p2p3 = self.p2.calculeDistance(self.p3)
        p1p3 = self.p1.calculeDistance(self.p3)
        if (p1p2 == p2p3 + p1p3) or (p2p3 == p1p2 + p1p3) or (p1p3 == p1p2 + p2p3):
            return True 
        else :
            return False 
    
    def estIsocele(self):
        p1p2 = self.p1.calculeDistance(self.p2)
        p2p3 = self.p2.calculeDistance(self.p3)
        p1p3 = self.p1.calculeDistance(self.p3)
        if p1p2 == p2p3 or p1p2 == p1p3 or p2p3 == p1p3 :
            return True
        else :
            return False 
        

"""
Partie pour tester les classes et leurs attributs des 3 exercices

"""

def main_1():
    print("--------------------------------------------")
    print("Programme de l'exercice 1 : \n")
    BF = Lieu("BF", "Rue Roger Couttolenc, 60200 Compiègne, France")
    PG = Lieu("PG","Rue du Docteur Schweitzer, 60203 Compiègne, France ")
    BF.detail()
    print("\n")
    PG.detail()
    
def main_2():
    print("\n--------------------------------------------")
    print("Programmae de l'exercice 2 : ")
    p1 = Personne("Doe","John",30,"m")
    print("\nEntrez les informations de la deuxième personne.")
    p2 = Personne(input("nom : "), input("prenom : "), int(input("age : ")), input("sexe : "))
    if p1.sameLastName(p2): 
         print(f"\n{p1.getprenom()} et {p2.getprenom()} ont le meme nom, à savoir : {p1.getnom()}.")
    else : 
         print(f"\n{p1} et {p2} n'ont pas le meme nom.")
    print(f"\nLa personne la plus agee est {p1.oldest(p2)}.") 

def main_3():
    print("\n--------------------------------------------")
    print("Programme de l'exercice 3 :")
    p1 = Point(-1.,-3.)
    p2 = Point(5.,1.)
    print(f"\nLa distance entre les points {p1} et {p2} est de {p1.calculeDistance(p2)}.")
    print("\nCoordonee du milieu :",p1.calculeMilieu(p2))
    
    p1 = Point(0,0)
    p2 = Point(2,0)
    p3 = Point(1,2)
    p = TroisPoints(p1, p2, p3)
    if p.sontAligne() :
        print(f"\nLes points {p1}, {p2} et {p3} sont alignes.")
    else : 
        print(f"\nLes points {p1}, {p2} et {p3} ne sont pas alignes.")
    if p.estIsocele(): 
        print(f"\nLe triangle forme par les points {p1}, {p2} et {p3} est isocele.")
    else : 
        print(f"\nLe triangle forme par les points {p1}, {p2} et {p3} n'est pas isocele.")
        
        
main_1()
main_2()
main_3()        
    
