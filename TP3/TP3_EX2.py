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
            print(f"{self.getprenom()} et {p.getprenom()} ont le meme nom, à savoir : {self.getnom()}.")
            return True
        else : 
            print(f"{self} et {p} n'ont pas le meme nom.")
            return False
    
    def oldest(self,p):
        if not isinstance(p, Personne):
            raise TypeError ("L'argument entré n'est pas une personne!")
        if self.getage() > p.getage():
            print(f"{self} est plus age que {p}.")
            return self 
        elif self.getage() == p.getage():
            print(f"{self} et {p} ont le meme age.")
            return self 
        else :
            print(f"{p} est plus age que {self}.")
        
    
    #en plus 
    def __str__(self):
        return f"{self.getsexe()} {self.getprenom()} {self.getnom()} ({self.getage()} ans)"

      
p = Personne("Doe", "John", "23", "h")
d = Personne("Doe","Marc",47,"f")

p.sameLastName(d)
p.oldest(d)











