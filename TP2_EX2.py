"""
KEBLI Soulaymane 
TAHIRI Mohamed 
TP 4B Mercredi 10h15-12h15

EX2 - Cryptage
"""

from string import ascii_letters
from decoaccent import accent #on importe notre décorateur accent () de notre fichier decoaccent 

@accent
def crypter(ch):
    new_mot = ""
    for i in range(len(ch)):
        if ch[i] in ascii_letters :
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