def accent(fonction):
  def wrapper(password):
    lettreaccent = ["é","è","à","ù"]
    lettresans = ["e","e","a","u"] 
    newPassword = ""
    for i in password :
      if i in lettreaccent:
        i = lettresans[lettreaccent.index(i)]
      newPassword += i
    return fonction(newPassword)
  return wrapper 
  
    

"""
EX1 - PALINDROME
"""
import string 
@accent
def inverse(mot):
    #si len(mot)==1 il s'agit d'une lettre
    if len(mot) == 1 :
        return mot 
    else : 
    #sinon on concatène la dernière lettre avec l'avant dernière...etc 
        return mot[len(mot)-1]+inverse(mot[:len(mot)-1])
    
#on fait une boulce pour tester plusieurs mot et verifier si l'inverse == mot 
bool1 = True
while bool1 :
    mot = input("entrez un mot :")
    if mot.lower() == inverse(mot).lower() :
        print(mot,"est un palindrome")
    else :
        print(mot,"n'est pas un palindrome.")
    continuer = input("voulez-vous continuez oui ou non : ")
    if continuer in ["oui","Oui","OUI"] :
        bool1 = True 
    elif continuer in ["non","Non","NON",]:
        bool1 = False 
        print("End")
        
        
"""
EX2 - CRYPTAGE
"""

@accent
#on cherche d'abord à savoir si le caractère est une lettre 
def crypter(ch):
    new_mot = ""
    for i in range(len(ch)):
        if ch[i] in string.ascii_letters :
        #on cherche d'abord à savoir si le caractère est une lettre 
            if (ch[i]!="z") and (ch[i]!="Z"):
            #puis on regarde si la lettre n'est pas un z, qu'on va ensuite concaténer à notre nouveau text
                new_mot = new_mot + chr(ord(ch[i])+1)
            else :
            #sinon on remplace un a pour un z ou A pour un Z
                if ch[i] == "z":
                    new_mot += "a"
                elif ch[i] == "Z" :
                    new_mot += "A"
        else :
        #s'il ne s'agit pas d'une lettre on garde le caractère  
            new_mot += ch[i]
    return new_mot

ch = input("Entrez votre texte :")
print(crypter(ch))


"""
EX3 - MOT DE PASSE
"""


"""
1- fonction nb_min(password) qui retourne le nombre de caractères minuscules.
"""
@accent
def nb_min(password):
    nb_min = 0
    for i in range(len(password)):
        if ord("a") <= ord(password[i]) <= ord("z"):
            nb_min += 1
    return nb_min 
#deuxième façon de faire 
@accent
def nb_min2(password):
    nb_min = 0
    for i in range(len(password)):
        if password[i] in string.ascii_lowercase :
            nb_min += 1
    return nb_min 

"""
2- fonction nb_maj(password) qui retourne le nombre de caractères majuscules.
"""
@accent
def nb_maj(password):
    nb_maj = 0
    for i in range(len(password)):
        if ord("A") <= ord(password[i]) <= ord("Z"):
            nb_maj += 1
    return nb_maj
#deuxième façon de faire 
@accent 
def nb_maj2(password):
    nb_maj = 0
    for i in range (len(password)):
        if password[i] in string.ascii_uppercase :
            nb_maj += 1
    return nb_maj 

"""
3 - fonction nb_alpha(password) qui retourne le nombre de caractères non
alphabétiques.
"""
@accent
def nb_alpha(password):
    nb_alpha = 0
    for i in range(len(password)):
        if not (password[i] in string.ascii_letters):
            nb_alpha += 1
    return nb_alpha 

"""
4 - fonction long_min(password) qui retourne la longueur de la plus longue séquence de
lettres minuscules.
"""
@accent 
def long_min(password):
    nb_min = 0
    tab_long_min  = []
    i = 0
    while i < len(password):
        if password[i] in string.ascii_lowercase:
            nb_min += 1
        else:
           tab_long_min.append(nb_min)
           nb_min = 0
        i += 1
    tab_long_min.append(nb_min)
    return max(tab_long_min)


"""
5 - fonction long_maj(password) qui retourne la longueur de la plus longue séquence de
lettres majuscules.
"""
@accent 
def long_maj(password):
    nb_maj = 0
    tab_long_maj  = []
    i = 0
    while i < len(password):
        if password[i] in string.ascii_uppercase:
            nb_maj += 1
        else:
           tab_long_maj.append(nb_maj)
           nb_maj = 0
        i += 1
    tab_long_maj.append(nb_maj)
    return max(tab_long_maj) 

"""
6 - fonction score(password) qui affiche la force du mot de passe
"""

def score(password):
    bonus = len(password)*4+(len(password)-nb_maj2(password))*2+(len(password)-nb_min2(password))*3+nb_alpha(password)*5
    malus = long_min(password)*2+long_maj(password)*3
    return bonus - malus

"""
Écrire le programme qui demande un mot de passe à l’utilisateur et affiche le score de celui-ci
"""
def main():
    password = input("Entrez votre mot de passe :")
    if score(password)<20 :
        print("Votre mot de passe a un score de",score(password),"il est donc trés faible.")
    elif score(password)<40 :
        print("Votre mot de passe a un score de",score(password),"il est donc faible.")
    elif score(password)<80 :
        print("Votre mot de passe a un score de",score(password),"il est donc fort.")
    else :
        print("Votre mot de passe a un score de",score(password),"il est donc trés fort.")

main()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    