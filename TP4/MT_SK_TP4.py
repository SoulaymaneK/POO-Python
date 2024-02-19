"""
KEBLI Soulayamne 
TAHIRI Mohamed 
 
TP4 B Mercredi 10h15 - 12h15
"""

"""
VOUS AVEZ JUSTE BESOIN DE LANCER DE LE PROGRAMME
"""
try : 
    import matplotlib.pyplot as plt 
    import numpy as np 
    from scipy.interpolate import make_interp_spline
    from os import path
    from pandas import DataFrame,read_csv
except ModuleNotFoundError:
    raise ModuleNotFoundError("Verifier que vous avez bien installé les modules matplolib\nscipy,numpy et pandas avec la commande pip install NomDuModule")

"""
EXERCICE 1 - Enregistrement 

Exercice dans lequel on crée une classe Enregistrement qui va permettre d'enregistrer 
les différentes caractéristiques d'un candidat, ncin,nom,prenom,age et decision du jury.
On utilise ensuite des fonctions qui permettent de gérer les différents attendus de l'exercice.
"""


class Enregistrement : 
    liste_NCIN = []#liste qui nous servira pour savoir si un ncin entré est déjà attribué
    def __init__(self,ncin,nom,prenom,age,decision):
        self.ncin = ncin
        self.nom = nom 
        self.prenom = prenom
        self.age = age 
        self.decision = decision
        Enregistrement.liste_NCIN.append(self.ncin)
        
    @property 
    def ncin(self):
        return self.__ncin 
    
    @ncin.setter 
    def ncin(self,ncin):
        try : 
            ncin = int(ncin)
        except ValueError :
            raise ValueError("le ncin doit être un entier!")
        self.__ncin = ncin 
    
    @property 
    def nom(self):
        return self.__nom 
    
    @nom.setter 
    def nom(self,nom):
        if not isinstance(nom, str):
            raise TypeError("Le nom doit être de type str !")
        self.__nom = nom
    
    @property 
    def prenom(self):
        return self.__prenom 
    
    @prenom.setter 
    def prenom(self,prenom):
        if not isinstance(prenom, str):
            raise TypeError("Le prenom doit être de type str !")
        self.__prenom = prenom
    
    @property 
    def age(self):
        return self.__age 
    
    @age.setter 
    def age(self,age):
        try :
            age = int(age)
            if age < 0 :
                raise ValueError("L'age doit être strictement positive")
        except ValueError:
            ValueError("L'age doit être un entier")
        self.__age = age
        
    @property 
    def decision(self):
        return self.__decision 
    
    @decision.setter 
    def decision(self,decision): 
        if not isinstance(decision, str):
            raise TypeError("La decision doit être de type str !")
        elif not decision.lower() in ["admis","refuse","ajourne"]:
            raise ValueError("La decision doit etre admis,refuse  ou ajourné !")
        self.__decision = decision 
    
    def print(self):
        return f"{self.ncin};{self.nom.lower()};{self.prenom.lower()};{self.age};{self.decision.lower()};"


def saisir():
    with open("concours.txt","w") as file : 
        bool1 = True 
        while bool1 : 
            candidat  = Enregistrement(ncin = input("entrez le ncin du candidat : "), 
                                       nom = input("entrez son nom : "),
                                       prenom = input("entrez son prenom : "), 
                                       age = input("entrez son age :"), 
                                       decision =input("entrez la decision du jury :") 
                                       )
               
            while candidat.ncin in candidat.liste_NCIN[:len(candidat.liste_NCIN)-1]:
                #si le ncin entré est déjà attribué, on demande a l'utilisateur d'entré un nouveau ncin
                print("\nle ncin du candidat existe deja veuillez rentrez son nouvel ncin!")
                ncin = input("entrez le ncin du candidat : ")
                candidat.ncin = ncin
                                            
            file.write(f"{candidat.print()}\n")
            continuer = input("voulez vous continuer oui ou non: ")
            if continuer.lower() not in ["oui","yes"] :
                bool1 = False
    

def admis():
    try :
        file1 = open("concours.txt","r") 
        file2 = open("admis.txt","w") 
        texte = file1.readlines() 
        for ligne in texte : 
            candidat = ligne.split(";")
            if candidat[4].lower() == "admis":# candidat[4] correspond a la decision du candidat
                file2.write(ligne)
        file1.close()
        file2.close()
    except FileNotFoundError :
        raise FileNotFoundError("Le fichier n'existe pas")
            
            
def attente():
    try : 
        file1 = open("admis.txt","r") 
        file2 = open("attente.txt","w") 
        texte = file1.readlines() 
        for ligne in texte : 
            candidat = ligne.split(";")
            if int(candidat[3]) > 30:#candidat[3] correspond a l'age du candidat
                file2.write(f"{candidat[0]};{candidat[1]};{candidat[2]};\n")
        file1.close()
        file2.close()      
    except FileNotFoundError :
        raise FileNotFoundError("Le fichier n'existe pas")

def supprimer():
    try:
        attente = open("attente.txt", "r")
        readAdmis = open("admis.txt", "r")
    except FileNotFoundError:
        print("Un des fichiers n'existe pas.")

    lignesAtt = attente.readlines()
    lignesAd = readAdmis.readlines()
    readAdmis.close()
    admis = open("admis.txt", "w")
    listNCINAtt = []
    for ligneAtt in lignesAtt:
        #boucle qui sert a repertorier les ncin des candidats du fichier attente
        motsAtt = ligneAtt.split(";")
        listNCINAtt.append(motsAtt[0])
    attente.close()

    for ligneAd in lignesAd:
        """
        boucle qui cherche si un ncin du fichier attente est present dans 
        le fichier admis pour tout réecrire dans le fichier admis excepté le candidat du ncin 
        """
        motsAd = ligneAd.split(";")
        if motsAd[0] not in listNCINAtt:
            admis.write(ligneAd)        
    admis.close()

def statistiques(dec):
    if type(dec) != str:
        raise TypeError("La décision doit être de type str.")
    dec = dec.lower()
    if dec not in ["admis", "refuse", "ajourne"]:
        raise ValueError("Cette décision n'est pas comprise.")

    concours = open("concours.txt", "r")

    lignes = concours.readlines()

    nTotal = 0
    nDec = 0

    for ligne in lignes:
        mots = ligne.split(";")
        if dec == mots[4]:
            nDec += 1
        nTotal += 1
    return (nDec/nTotal)*100

def camenbert() :
    plt.figure(figsize = (8,8))
    x = [statistiques("admis"),statistiques("refuse"),statistiques("ajourne")]
    plt.pie(x, labels = ["Admis","Refusés","Ajournés"],
            autopct = lambda x : str(round(x)) + '%',
            pctdistance = 0.7, labeldistance = 1.2)
    plt.legend() 
    plt.show()

def main_1():
    #saisir()
    #admis()
    #attente()
    #supprimer()
    camenbert()

"""
EXERCIE 2 - Mtplotlib

On cree un fonction cercle qu'on utilise dans différents boucles pour afficher 
le reusltat attendu 
"""
def cercle(x0,y0,r):
    plt.xticks(np.linspace(0,20,5))#afficher les valeurs de x uniquement entre 0 et 20 
    plt.yticks(np.linspace(0,20,9))#pareille pour y 
    plt.axis("equal")#ajuster les dimensions des traits d'unité du plan
    theta = np.linspace(0,2*np.pi)#prend toutes les valeurs entre à et 2pi
    x = r * np.cos(theta) + x0
    y = r * np.sin(theta) + y0     
    plt.plot(x,y)


def qst1():
    for i in range(9):
        cercle(10,10,1 + i) #on augmente juste le rayon de 1 a chque itération
    plt.show() 
    
def qst2():
    for i in range(10):
        for j in range(10-i):
            cercle(i+2*j,2*i,1)# on augment 
    plt.show() 

def main_2() : 
    while True : 
        n = int(input("Quelle question (exo 2) voulez-vous tester (1 ou 2) : ")) 
        exec(f"qst{n}()")
        continuer = input("voulez-vous tester une autre question de l'exercice 2 (oui ou non):")
        if continuer.lower() not in ["oui","yes"] :
            break 

""" 
EXERCICE 3 - COS(x)

A l'aide d'une focntion qui renvoie la liste des x et la liste respective des cos(x)
on cree un fichier csv a l'aide du module pandas qui contiend les valeurs de x et de cos(x).
On utilise ensuite ces valeurs pour afficher un graphique.

"""
def x_cos():
    list_x = [i for i in range(-5,6)]
    list_cos = [np.cos(i) for i in range(-5,6)]
    return list_x, list_cos


def ecrire() :
    a,b = x_cos()
    for i in range(-5,6):
        file = DataFrame({"x": a, "cos(x)":b},index = None,columns = ["x","cos(x)"])
    file.to_csv("math.csv")
    #sinon on peut retirer la colonne a et la mettre en index 

        
def lire():
    if not path.isfile("math.csv") :
         raise FileNotFoundError("Le fichier n'a pas été trouvé!")
    file = read_csv("math.csv")
    a = np.array(file[file.columns[1]])
    b = np.array(file[file.columns[2]])
    courbe = make_interp_spline(a, b)
    
    x = np.linspace(a[0],a[len(a)-1],100)
    y = courbe(x)
    plt.plot(x,y)
   
    plt.xticks(np.linspace(-4,4,5))
    plt.yticks(np.linspace(-1,1,9))
    plt.title("cos(x) sur [-5;5]")
    plt.xlabel("x")
    plt.ylabel("cos(x)")
    
    plt.show() 
 
    
def main_3():
    try : 
        ecrire()
        lire() 
    except ModuleNotFoundError :
        raise ModuleNotFoundError("Verifier que vous avez bien installé les modules matplolib\nscipy,numpy et pandas avec la commande pip install NomDuModule")

def main() :
    print("-----------------------------------")
    while True : 
        n = int(input("Quel exercice voulez-vous tester (1 , 2 ou 3) : ")) 
        exec(f"main_{n}()")
        print("-----------------------------------")
        continuer = input("voulez-vous tester un autre exercice (oui ou non):")
        if continuer.lower() not in ["oui","yes"] :
            print("\n--------FIN DU PROGRAMME---------")
            break 
        #c'est possible que la page d'affichage des différents graphiques ne se ferment pas après chaque exercice
        #mais une fois un autre exercice lancé elle s'ajustera automatiquement 
        

main() 


    




    
    