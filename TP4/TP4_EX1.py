"""
NCIN, NOM, PRENOM, AGE, 
DECISION : (type contenant les valeurs suivantes : admis, refusé, ajourné). 
Chaque élément est séparé par point-virgule (;). Il y a un candidat par ligne.

"""
import matplotlib.pyplot as plt 


class Enregistrement : 
    def __init__(self,ncin,nom,prenom,age,decision):
        self.ncin = ncin
        self.nom = nom 
        self.prenom = prenom
        self.age = age 
        self.decision = decision
    
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
        return f"{self.ncin};{self.nom};{self.prenom};{self.age};{self.decision};"


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
            file.write(f"{candidat.print()}\n")
            continuer = input("voulez vous continuer : ")
            
            if continuer.lower() not in ["oui","yes"] :
                bool1 = False
    

def admis():
    try :
        file1 = open("concours.txt","r") 
        file2 = open("admis.txt","w") 
        texte = file1.readlines() 
        for ligne in texte : 
            candidat = ligne.split(";")
            if candidat[4].lower() == "admis":
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
            if int(candidat[3]) >30:
                file2.write(f"{candidat[0]};{candidat[1]};{candidat[2]};\n")
        file1.close()
        file2.close()
        
    except FileNotFoundError :
        raise FileNotFoundError("Le fichier n'existe pas")
            
def statistique():
    try : 
        with open("concours.txt","r") as file :
            texte = file.readlines()
            admis = 0
            refuse = 0
            ajourne = 0
            for ligne in texte : 
                dec = ligne.split(";")
                if dec[4].lower() == "admis":
                    admis +=1
                elif dec[4].lower() == "refuse":
                    refuse +=1
                elif dec[4].lower() == "ajourne":
                    ajourne +=1 
                    
          
    except FileExistsError :
        raise FileExistsError("Le fichier n'existe pas")

def camenbert():
    plt.figure(figsize = (8,8))
    #x = [admis,refuse,ajourne]
    plt.pie(#x, labels = ["Admis","Refuse","Ajourne"],
            autopct = lambda x : str(round(x)) + '%',
            pctdistance = 0.7, labeldistance = 1.2)
    plt.legend() 
    plt.show()

def supprimer() :
    try :
        file1  = open("admis.txt","r+")
        file2 = open("attente.txt","r+")
        
        lignead = file1.readlines()
        ligneatt = file2.readlines() 
        
        for i in lignead :
            for j in ligneatt:
                if i[:2] == j :
                    lignead.remove(i)
        file1.close()
        file2.close()
        
        with open("admis.txt","w") as file :
            for ligne in lignead :
                file.write(str(ligne.join(";")))
    
    
    except FileNotFoundError:
        raise FileNotFoundError("Le fichier n'a pas été trouvé")
                    
def main() :
    saisir() 
    admis() 
    attente()
    supprimer()
    statistique()

main() 







    
