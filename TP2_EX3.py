"""
KEBLI Soulaymane 
TAHIRI Mohamed 
TP 4B Mercredi 10h15-12h15

EX3 - MOT DE PASSE 
"""
from string import ascii_letters,ascii_lowercase,ascii_uppercase 
from decoaccent import accent #on importe notre décorateur accent() de notre fichier decoaccent 

@accent
def nb_min(password):
    nb_min = 0#on initialise le nombre de miniscule à 0
    for i in password:
        if i in ascii_lowercase :
            nb_min += 1#pour chaque minuscule rencontrée on incrémente de 1
    return nb_min #on retourne le nombre de minuscule 

@accent
def nb_maj(password):
    nb_maj = 0#on initialise le nombre de majuscule à 0
    for i in password:
        if i in ascii_uppercase :
            nb_maj += 1#pour chaque majuscule rencontrée on incrémente de 1
    return nb_maj #on retourne le nombre de majuscule

@accent
def nb_alpha(password):
    nb_alpha = 0#on initialise le nombre de caractères spéciaux à 0
    for i in password:
        if i not in ascii_letters :#on vérifie si le caractère n'est pas une lettre
            nb_alpha += 1#pour chaque caractère spécial rencontré on incrémente de 1
    return nb_alpha #on retourne le nombre de caractères spéciaux 

@accent
def long_min(password):
    long_min_actuelle = 0
    long_min_max = 0
    for i in password :
        if i in ascii_lowercase:
            long_min_actuelle += 1#pour chaque minuscule rencontrée on incrémente de 1 jusqu'à que le caractère ne soit pas une minuscule
        else:
            if long_min_max <= long_min_actuelle:#on vérifie si le nombre actuelle de minuscule est plus grand que le nombre maximale (de minuscule)
                long_min_max = long_min_actuelle#si oui on affecte au nombre maximale de minuscule le nombre actuelle 
            long_min_actuelle = 0#on réinitialise le nombre actuelle de minuscule à 0
    if long_min_max <= long_min_actuelle:#on verife en sortie de boule si le nombre actuelle de minuscule est plus grand que le nombre max 
        long_min_max = long_min_actuelle#si oui, on affecte au nomdre max le nombre actuelle 
    return long_min_max

@accent
def long_maj(password):
    long_maj_actuelle = 0
    long_maj_max = 0
    for i in password :
        if i in ascii_lowercase:
            long_maj_actuelle += 1#pour chaque majuscule rencontrée on incrémente de 1 jusqu'à que le caractère ne soit pas une majuscule
        else:
            if long_maj_max <= long_maj_actuelle:#on vérifie si le nombre actuelle de majuscule est plus grand que le nombre maximale (de majuscule)
                long_maj_max = long_maj_actuelle##si oui on affecte au nombre maximale de majsucule le nombre actuelle 
            long_maj_actuelle = 0#on réinitialise le nombre actuelle de majuscule à 0
    if long_maj_max <= long_maj_actuelle:#on verife en sortie de boule si le nombre actuelle de majuscule est plus grand que le nombre max 
        long_maj_max = long_maj_actuelle##si oui, on affecte au nomdre max le nombre actuelle 
    return long_maj_max


def score(password):
    #on calcule les bonus et malus separement (pour plus de lisibilité) selon les conditions de l'enonce 
    bonus = len(password)*4 + (len(password)-nb_maj(password))*2 + (len(password)-nb_min(password))*3 + nb_alpha(password)*5
    malus = long_min(password)*2 + long_maj(password)*3
    score  = bonus - malus 
    #on vérifie la force du mot de passe et on l'affiche 
    if score < 20 :
        print("Votre mot de passe a un score de",score,"il est donc très faible.")
    elif score < 40 :
        print("Votre mot de passe a un score de",score,"il est donc faible.")
    elif score < 80 :
        print("Votre mot de passe a un score de",score,"il est donc fort.")
    else :
        print("Votre mot de passe a un score de",score,"il est donc très fort.")
        

password = input("Entrez votre mot de passe :")
score(password)

