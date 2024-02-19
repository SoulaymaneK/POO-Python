"""
KEBLI Soulaymane
TAHIRI Mohamed
TP 4B Mercredi 10h15-12h15

Decorateur pour les accents :

Dans ce fichier, il s'agit d'un décorateur utilisé dans les 3 autres exercices pour que nos programmes soient 
complets et fonctionnent même avec des chaines contenant des accents.

"""

def accent(fonction):#décorateur pour gérer les accents 
  def wrapper(password):
    lettreaccent = ["é","è","à","ù","ç"]#création d'une liste avec les principaux accents 
    lettresans = ["e","e","a","u","c"]#création d'une liste avec les lettres correspondantes respectivement sans accents
    newPassword = ""#on instance le nouveau mot de passe 
    for i in password :
      if i in lettreaccent:
        i = lettresans[lettreaccent.index(i)]#on recompose le mot par toutes les lettres en remplaçant celle avec accent par leur équivalent sans accent
      newPassword += i
    return fonction(newPassword) #on applique la fonction avec le nouveau mot sans accent 
  return wrapper 
