"""
TAHIRI Mohamed 
KEBLI Soulaymane 

TP 4B Mercredi 10h15-12h15
"""

import sqlite3
import pandas as pd
from tkinter import *

"""
Dans ce TP on a crée une base de donnée selon la consigne pour la gestion de l'alesc. Pour cela on a utilisé
plusieurs requête SQL. A chaque fois l'unicité des données est verifiée.
On a ensuite crée une classe Formulaire permettant de gerer l'affichage avec Tkinter des logements et des occupants de ces derniers
selon les logeurs.
"""


class Formulaire(Tk):

    def __init__(self, l=430, h=450):
        Tk.__init__(self)
        x = self.winfo_screenwidth()
        y = self.winfo_screenheight()
        pos_x = x // 2 - l // 2
        pos_y = y // 2 - h // 2
        geometrie = f"{l}x{h}+{pos_x}+{pos_y}"
        self.geometry(geometrie)
        self.title("TP 6 - BDD")

        self.widgets = []

        self.initialise()

    def initialise(self):

        self.prenom = StringVar()
        self.nom = StringVar()

        Label(self, text="Nom du logeur : ", relief='raised', bg='yellow', fg='black').grid(sticky='we', row=0, column=0, padx=10, pady=10)
        Label(self, text="Prénom du logeur : ", relief='raised', bg='yellow', fg='black').grid(sticky='we', row=1, column=0, padx=10)

        Entry(self, textvariable=self.nom).grid(column=1, row=0, columnspan=2)
        Entry(self, textvariable=self.prenom).grid(column=1, row=1, columnspan=2)

        Button(self, text='Valider', relief='raised', command=self.searchLogements).grid(row=2, column=0)
        Button(self, text='Réinitialiser', relief='raised', command=self.eraseAll).grid(row=2, column=1)
        Button(self, text='Quitter', relief='raised', command=self.destroy).grid(row=2, column=2)

    def eraseAll(self):
        self.prenom.set("")
        self.nom.set("")
        self.eraseWidgets()

    def eraseWidgets(self):
        for widget in self.widgets:
            widget.destroy()
        self.widgets = []

    def searchLogements(self):

        self.eraseWidgets()

        nom = self.nom.get()
        prenom = self.prenom.get()

        if nom == "" or prenom == "":
            self.widgets.append(Label(self, text=f"Veuillez entrer un nom valable.", bg='white', fg='black', relief='raised'))
            self.widgets[-1].grid(sticky=W, row=4, column=0, columnspan=4, padx=10, pady=10)
            return 0

        cursor.execute(f''' SELECT id_logeur FROM LOGEUR WHERE nom = '{nom}' AND prenom = '{prenom}' ''')
        try:
            id_logeur = cursor.fetchone()[0]
        except TypeError:
            self.widgets.append(Label(self, text=f"Le logeur {prenom[0].upper() + prenom[1:]} {nom[0].upper() + nom[1:]} n'est pas dans notre base de données.", bg='white', fg='black', relief='raised'))
            self.widgets[-1].grid(sticky=W, row=4, column=0, columnspan=4, padx=10, pady=10)
            return 0

        cursor.execute(
            f''' SELECT numero_rue, nom_rue, code_postal, ville, labelisation, type, id_logement FROM LOGEMENT WHERE logeur = '{id_logeur}' ''')
        logements = cursor.fetchall()

        n = 1
        row = 4


        if len(logements) == 0:
            self.widgets.append(Label(self, text=f"Le logeur {prenom[0].upper() + prenom[1:]} {nom[0].upper() + nom[1:]} n'a pas de logement.", bg='white', fg='black', relief='raised'))
            self.widgets[-1].grid(sticky=W, row=row, column=0, columnspan=4, padx=10, pady=10)

        for logement in logements:

            cursor.execute(f''' SELECT type FROM TYPE WHERE id_type = '{logement[5]}' ''')
            type = cursor.fetchone()[0]
            type = type[0].upper() + type[1:]

            self.widgets.append(Label(self, text=f"Logement n°{n} : ", bg='red', fg='black', relief='raised'))
            self.widgets[-1].grid(row=row, column=0, pady=10)
            self.widgets.append(Label(self, text=f"{logement[0]} {logement[1][0].upper() + logement[1][1:]}, {logement[2]} {logement[3][0].upper() + logement[3][1:]}, {type} {logement[4] * '*'}"))
            self.widgets[-1].grid(row=row, column=1, columnspan=4, sticky='w')

            row += 1

            cursor.execute(f''' SELECT nom, prenom FROM ETUDIANT WHERE logement = '{logement[6]}' ''')
            etudiants = cursor.fetchall()

            if len(etudiants) == 0:
                self.widgets.append(Label(self, text="Ce logement est vide.", bg='white', fg='black', relief='raised'))
                self.widgets[-1].grid(sticky=W, row=row, column=1, columnspan=4)
                row += 1

            for etudiant in etudiants:
                self.widgets.append(Label(self, text="Nom de l'étudiant : ", bg='white', fg='black', relief='raised'))
                self.widgets[-1].grid(sticky=W, row=row, column=1)
                self.widgets.append(Label(self, text=f"{etudiant[1][0].upper() + etudiant[1][1:]} {etudiant[0][0].upper() + etudiant[0][1:]}"))
                self.widgets[-1].grid(sticky=W, row=row, column=2, columnspan=4)
                row += 1

            n += 1

def createTables():
    sql1 = """
    CREATE TABLE IF NOT EXISTS TYPE
    (
        id_type integer
            primary key autoincrement,
        type text
    )"""

    sql2 = """
    CREATE TABLE IF NOT EXISTS LOGEUR
    (
        id_logeur integer
            primary key autoincrement,
        nom text,
        prenom text,
        numero_rue int,
        nom_rue text,
        code_postal text,
        ville text
    )"""

    sql3 = """
    CREATE TABlE IF NOT EXISTS LOGEMENT
    (
        id_logement integer
            primary key autoincrement,
        numero_rue int,
        nom_rue text,
        code_postal text,
        ville text,
        labelisation int,
        type int,
        logeur  INTEGER,
        FOREIGN KEY (type) REFERENCES TYPE (id_type),
        FOREIGN KEY (logeur) REFERENCES LOGEUR (id_logeur)
    )
    """

    sql4 = """
    CREATE TABLE IF NOT EXISTS ETUDIANT
    (
        id_etu integer
            primary key autoincrement,
        nom text,
        prenom text,
        semestre text,
        logement INTEGER,
        FOREIGN KEY (logement) REFERENCES LOGEMENT (id_logement)
    )
    """

    cursor.execute(sql1)
    connexion.commit()

    cursor.execute(sql2)
    connexion.commit()

    cursor.execute(sql3)
    connexion.commit()

    cursor.execute(sql4)
    connexion.commit()

    types = ["chambre", "studio", "f1", "f2", "f3", "f4", "f5", "maison"]

    for i in types:
        cursor.execute(f"INSERT INTO TYPE(type) VALUES('{i}')")

def fillLogeurs():
    logeurs = pd.read_excel("logeurs.xlsx")
    df_logeurs = pd.DataFrame(logeurs, columns=logeurs.columns)

    for i, row in df_logeurs.iterrows():
        sql = f'''INSERT INTO LOGEUR(nom, prenom, numero_rue, nom_rue, code_postal, ville) 
    SELECT * FROM (SELECT '{row[0]}' AS nom, '{row[1]}' AS prenom, '{row[2]}' AS numero_rue, '{row[3]}' AS nom_rue, '{row[4]}' AS code_postal, '{row[5]}' as ville) AS new
    WHERE NOT EXISTS (SELECT nom, prenom FROM LOGEUR WHERE nom = '{row[0]}' AND prenom = '{row[1]}')'''
        cursor.execute(sql)
        connexion.commit()

def fillLogements():
    logements = pd.read_excel("logements.xlsx")
    df_logements = pd.DataFrame(logements, columns=logements.columns)

    for i, row in df_logements.iterrows():
        cursor.execute(f"SELECT id_logeur FROM LOGEUR WHERE nom = '{row[5]}' and prenom = '{row[6]}'")
        logeur = cursor.fetchone()[0]

        cursor.execute(f"SELECT id_type FROM TYPE WHERE type = '{row[7]}'")
        type = cursor.fetchone()[0]

        sql = f'''INSERT INTO LOGEMENT(numero_rue, nom_rue, code_postal, ville, labelisation, logeur, type)
    SELECT * FROM (SELECT '{row[0]}' AS numero_rue, '{row[1]}' AS nom_rue, '{row[2]}' AS code_postal, '{row[3]}' AS ville, '{row[4]}' AS labelisation, '{logeur}' AS logeur, '{type}' as type) AS new
    WHERE NOT EXISTS (SELECT numero_rue, nom_rue FROM LOGEMENT WHERE numero_rue = '{row[0]}' AND nom_rue = '{row[1]}')'''
        cursor.execute(sql)
        connexion.commit()

def fillEtudiants():
    etudiants = pd.read_excel("etudiants.xlsx")
    df_etudiants = pd.DataFrame(etudiants, columns=etudiants.columns)

    for i, row in df_etudiants.iterrows():
        cursor.execute(f"SELECT id_logement FROM LOGEMENT WHERE numero_rue = '{row[3]}' and nom_rue = '{row[4]}' and code_postal = '{row[5]}' and ville = '{row[6]}'")
        logement = cursor.fetchone()[0]

        sql = f'''INSERT INTO ETUDIANT(nom, prenom, semestre, logement)
    SELECT * FROM (SELECT '{row[0]}' AS nom, '{row[1]}' AS prenom, '{row[2]}' AS semestre, '{logement}' AS logement) AS new
    WHERE NOT EXISTS (SELECT nom, prenom FROM ETUDIANT WHERE nom = '{row[0]}' AND prenom = '{row[1]}')'''
        cursor.execute(sql)
        connexion.commit()

def showLogementsConsole(nom, prenom):

    cursor.execute(f''' SELECT id_logeur FROM LOGEUR WHERE nom = '{nom}' AND prenom = '{prenom}' ''')
    try:
        id_logeur = cursor.fetchone()[0]
    except TypeError:
        print(f"\nLe logeur {prenom[0].upper() + prenom[1:]} {nom[0].upper() + nom[1:]} n'est pas dans notre base de données.")
        return 0

    print("\nNom du logeur : ", prenom[0].upper() + prenom[1:], nom[0].upper() + nom[1:])

    cursor.execute(f''' SELECT numero_rue, nom_rue, code_postal, ville, labelisation, type, id_logement FROM LOGEMENT WHERE logeur = '{id_logeur}' ''')
    logements = cursor.fetchall()

    n = 1
    for logement in logements:

        cursor.execute(f''' SELECT type FROM TYPE WHERE id_type = '{logement[5]}' ''')
        type = cursor.fetchone()[0]
        type = type[0].upper() + type[1:]

        print(f"\n\tLogement n°{n} : {logement[0]} {logement[1][0].upper()+logement[1][1:]}, {logement[2]} {logement[3][0].upper()+logement[3][1:]}, {type} {logement[4]*'*'}")

        cursor.execute(f''' SELECT nom, prenom FROM ETUDIANT WHERE logement = '{logement[6]}' ''')
        etudiants = cursor.fetchall()

        if len(etudiants) == 0:
            print("\t\tCe logement est vide.")

        for etudiant in etudiants:
            print(f"\t\tNom de l'étudiant  :", etudiant[1][0].upper() + etudiant[1][1:], etudiant[0][0].upper() + etudiant[0][1:])

        n += 1

def showLogementsFenetre():
    formulaire = Formulaire()
    formulaire.mainloop()

if __name__ == '__main__':
    connexion = sqlite3.connect('alesc.sqlite')
    cursor = connexion.cursor()

    createTables()

    fillLogeurs()
    fillLogements()
    fillEtudiants()

    showLogementsConsole(input("Quel est le nom de la personne dont vous voulez connaître les logements ? : ").lower(), input("Et son prenom ? : ").lower())

    showLogementsFenetre()

    cursor.close()
    connexion.close()

