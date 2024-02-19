"""
KEBLI Soulaymane 
TAHIRI Mohamed 
TP 4B Mercredi 10h15-12h15

EX1 - Palindrome
"""

from decoaccent import accent #on import notre decorateur accent() de notre fichier decoaccent


@accent
def isPalindrome(mot) :
    if len(mot) <= 1:#condition d'arret de la fonction récursive 
        return True
    else:
        if mot[0].lower() == mot[len(mot)-1].lower():#on vérifie si la première et la dernière lettre de l'argument sont égales
            return isPalindrome(mot[1:len(mot)-1])#si elles sont égales, on renvoie la fonction en y enlevant la première et la dernière lettres
        else :
            return False#sinon le mot ne peut pas être un palindrome

#boucle demandant à l'utilisateur d'entrez un mot et applique la fonction à ce mot 
bool1 = True
while bool1 :
    mot = input("Entrez un mot : ")
    if isPalindrome(mot):
        print(mot, "est un palindrome.")
    else:
        print(mot, "n'est pas un palindrome.")
    continuer = input("voulez-vous continuez oui ou non : ")#on demande à l'utilisateur s'il veut continuer à entrer des mots 
    if continuer in ["oui","Oui","OUI"] :
        bool1 = True 
    elif continuer in ["non","Non","NON",]:
        bool1 = False 
        print("D'accord")
        print("Fin du programme")
        