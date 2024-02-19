"""
KEBLI Soulaymane 
TAHIRI Mohamed 

TP 4B Mercredi 10h15-12h15
"""

from tkinter import *
from math import cos,sin,tan,pi,sqrt
π = pi

"""
On a créé une calculatrice avec tous les boutons de la consigne. On a rajouté quelques fonctionnalitées : 
    - Le bouton Rad/Deg qui permet de modifier l'unité de l'angle en respectant les conversions, 
                L'unité en MAJUSCULE sur le bouton correspond à l'unité actuelle.
                
    - Le bouton ANS qui permet de recuperer le dernier resultat. il est affiché dans un label et peut être utilisé 
                également dans le calcul. Pour le réinitialiser il faut appuyer sur la touche =
                
    - Le bouton Del qui permet de supprimer le dernier élément rentré par l'utilisateur pour d'éventuelles fautes de frappes 
    
    - Le bouton π pour la valeur de pi 
    
    - des éventuelles parenthèses
    
    - On ne peut pas écrire deux opérateurs de suite. Lorsqu'on appuie sur deux opérateurs de suite seul le premier est garder. 
    
    - On est pas obligé d'écrire le "x" pour la multiplication, ex : au lieu de axb on peut ecrire ab directement 
    
    - On a créer des focntions qui vérifient la syntaxe et permettent à la calculatrice de fonctionner en cas d'oublie de paranthèse etc...
    
    - Lorsqu'on étend la fenêtre tous les boutons s'étendent porportionnellement 
    
    - On a créer deux chaines de calculs : une chaine principale (self.chaine_calcul) et une chaine visuelle (self.chaine_visu) pour 
        embellir l'écriture dans le label du calcul comme par exemple : on aura sqrt(a) dans la chaine principale mais on affichera √(a)
        
    - Le bouton Clear réinitialise les chaines de calculs mais le bouton ANS garde quand même le resultat 
    
    - Lorsqu'on appuie sur le bouton = pour avoir le resultat puis qu'on appuie une seconde fois, les chaines de calcule et le Label ANS se 
                remettent à 0
                
    - On ne peut pas entrer un nombre négatif dans la racine (exceptée pour le ANS)
    
    - La division par zéro et la racine d'un nombre négatif affiche un message d'erreur
"""

class Calculatrice(Tk) :
    
    apresOperateurs = ["+",
                  "-",
                  "*",
                  "/",
                  "**2",
                  ".","c"
                  " "]
    
    def __init__(self,l = 400,h = 500):
        Tk.__init__(self)
        x = self.winfo_screenwidth() 
        y = self.winfo_screenheight() 
        pos_x = x//2 - l//2
        pos_y = y//2 - h//2
        geometrie = f"{l}x{h}+{pos_x}+{pos_y}"
        self.geometry(geometrie)
        self.title("TP Calculatrice")
        
        self.rowconfigure([i for i in range(10)], weight =1)
        self.columnconfigure([i for i in range(4)], weight=1)
        
        self.creation_chaine()
        self.creation_label()
        self.creation_chiffre()
        self.creation_operateur()
    
    def creation_chaine(self): 
        self.chaine_calcul = StringVar()
        self.chaine_calcul.set(" ")
        self.chaine_visu = StringVar()
        self.chaine_visu.set(" ")
        self.ANS = self.chaine_calcul.get() 
        self.raddeg = 1
        self.radordeg = StringVar()
        self.radordeg.set("RAD\ndeg")
    
    def creation_label(self):
        self.label1 = Label(self, textvariable = self.chaine_visu, bg='white', relief = 'sunken', fg='black')
        self.label1.grid(row = 2, column = 0, columnspan = 4, sticky="ew", padx = 20)
        
        self.label2 = Label(self, text="Calculatrice", relief='raised')
        self.label2.grid(row =0, column = 1, columnspan = 2, pady=5 )
        
        self.ans_label = Label(self,text=f" ANS : ", bg="white", fg="black", relief = "sunken", anchor = "w")
        self.ans_label.grid(row=1,column=0, columnspan = 2, sticky="ew", padx = 20)
       
    def modif_chaine_calcul(self, x):
        if x == "**2":
            xVisu = "²"
        elif x == "*":
            xVisu = "x"
        elif x == "sqrt(":
            xVisu = "√("
        elif x == ".":
            xVisu = ","
        elif x == "cos(self.raddeg*":
            xVisu = "cos("
        elif x == "sin(self.raddeg*":
            xVisu = "sin("
        elif x == "tan(self.raddeg*":
            xVisu = "tan("
        else:
            xVisu = x
        if x=="ANS": 
            self.chaine_visu.set(self.chaine_visu.get()+"ANS")
            self.chaine_calcul.set(self.chaine_calcul.get()+"("+str(self.ANS)+")")
        if self.checkSyntax(x) and x!="ANS":
            self.chaine_calcul.set(self.chaine_calcul.get()+str(x))
            self.chaine_visu.set(self.chaine_visu.get() + str(xVisu))
        
    def clearAll_chaine_calcul(self):
        self.chaine_calcul.set(" ")
        self.chaine_visu.set(" ")

    def del_chaine_calcul(self):
        if len(self.chaine_calcul.get()) == 1:
            self.clearAll_chaine_calcul()
        else:
            self.chaine_calcul.set(self.chaine_calcul.get()[:len(self.chaine_calcul.get())-1])
            self.chaine_visu.set(self.chaine_visu.get()[:len(self.chaine_visu.get()) - 1])
        
    def calcul(self):
        try : 
            self.checkFinalSyntax()
            if len(self.chaine_calcul.get()) not in (0,1):
                exec("self.chaine_calcul.set(str(round("+self.chaine_calcul.get()+", 5)))")
                self.chaine_visu.set(self.chaine_calcul.get())#.replace('.', ','))
            else:
                self.chaine_calcul.set("0")
                self.chaine_visu.set("0")
            self.ANS = self.chaine_calcul.get()
            self.ans_label.configure(text=f" ANS : {self.chaine_visu.get()}")
        except ZeroDivisionError:
            self.chaine_visu.set("ERROR : division par 0, veuillez clear")
        except ValueError: 
            self.chaine_visu.set("ERROR : nombre négatif dans la racine, veuillez clear")

    def changeraddeg(self):
        if self.raddeg == 1:
            self.raddeg = pi/180
            self.radordeg.set("rad\nDEG")
        else:
            self.raddeg = 1
            self.radordeg.set("RAD\ndeg")

    def checkSyntax(self, x):
        if (self.chaine_calcul.get()[-1] in Calculatrice.apresOperateurs and x in Calculatrice.apresOperateurs)\
            and not (self.chaine_calcul.get()[-1] == ' ' and x == '-'):
            return False
        if self.chaine_calcul.get()[-1] == "(" and x in Calculatrice.apresOperateurs:
            return False
        elif not self.checkTrigo(x):
            return False
        elif not self.checkVirgules(x):
            return False
        elif not self.checkSquares(x):
            return False
        elif not self.checkParentheseG(x):
            return False
        elif not self.checkParentheseD(x):
            return False
        else:
            return True

    def checkVirgules(self, x):
        if x != ".":
            return True
        if self.chaine_calcul.get()[-1] in ("(", ")", " ", "π"):
            return False

        lastTerm = ""
        for i in self.chaine_calcul.get():
            if i in Calculatrice.apresOperateurs and i != ".":
                lastTerm = ""
            else:
                lastTerm += i

        if "." in lastTerm:
            return False
        else:
            return True

    def checkTrigo(self, x):
        if x in [i for i in range(10)] and self.chaine_calcul.get()[-1] == "π":
            return False 
        if x not in ("π","cos(self.raddeg*","sin(self.raddeg*","tan(self.raddeg*"):
            return True
        else:
            if self.chaine_calcul.get()[-1] == ".":
                return False
            else:
                return True

    def checkSquares(self, x):
        if x in [i for i in range(10)] and self.chaine_calcul.get()[-1] == "²":
            return False 
        if x not in ("**2", "sqrt("):
            return True

        else:
            if self.chaine_calcul.get()[-1] == " " and x == "**2":
                return False
            elif self.chaine_calcul.get()[-1] == "." and x == "sqrt(":
                return False
            else:
                return True

    def checkParentheseG(self, x):
        if x != "(":
            return True
        if self.chaine_calcul.get()[-1] == '.':
            return False
        else:
            return True

    def checkParentheseD(self, x):
        if x != ")":
            return True

        nParenthesesG = 0
        nParenthesesD = 0
        for i in self.chaine_calcul.get():
            if i == "(":
                nParenthesesG += 1
            elif i == ")":
                nParenthesesD += 1

        if self.chaine_calcul.get()[-1] == '(' or nParenthesesG <= nParenthesesD:
            return False
        else:
            return True

    def checkFinalSyntax(self):
        chaine = self.chaine_calcul.get()
        if chaine[-1] in ["+","-","*","/",".","(","s","q","r","t","c","o","s","i","n","a"]:
            self.chaine_calcul.set(chaine[:len(chaine)-1])
            return self.checkFinalSyntax()
        nParenthesesG = 0
        nParenthesesD = 0
        for i in chaine:
            if i == "(":
                nParenthesesG += 1
            elif i == ")":
                nParenthesesD += 1

        modifChaine = ""
        nbs = [str(i) for i in range(10)]
        nbs.append("π")
        nbs.append(")")
        for i in range(len(chaine)-1):
            if chaine[i] in nbs and chaine[i+1] in ("(","π","c","s","t","A"):
                modifChaine += f"{chaine[i]}*"
            else:
                modifChaine += f"{chaine[i]}"
            if i == len(chaine)-2:
                modifChaine += chaine[i+1]
        
        self.chaine_calcul.set(modifChaine + (nParenthesesG-nParenthesesD)*")")
        
    def ans(self):
       self.modif_chaine_calcul("ANS")
       self.ANS = ""

    def creation_chiffre(self):
        
        un = Button(self, text="1", highlightbackground='gold4', command = lambda : self.modif_chaine_calcul(1))
        un.grid(row = 3, column=0, sticky="nesw")
    
        deux = Button(self, text="2", highlightbackground='gold4', command = lambda : self.modif_chaine_calcul(2))
        deux.grid(row = 3, column = 1, sticky="nesw")
        
        trois = Button(self, text="3", highlightbackground='gold4', command = lambda : self.modif_chaine_calcul(3))
        trois.grid(row = 3, column = 2, sticky="nesw")
        
        quatre = Button(self, text="4", highlightbackground='gold4', command =lambda : self.modif_chaine_calcul(4))
        quatre.grid(row = 4, column = 0, sticky="nesw")
        
        cinque = Button(self, text="5", highlightbackground='gold4', command =lambda : self.modif_chaine_calcul(5))
        cinque.grid(row = 4, column = 1, sticky="nesw")
        
        six = Button(self, text="6", highlightbackground='gold4', command =lambda : self.modif_chaine_calcul(6))
        six.grid(row = 4, column = 2, sticky="nesw")
        
        sept = Button(self, text="7", highlightbackground='gold4', command =lambda : self.modif_chaine_calcul(7))
        sept.grid(row = 5, column = 0, sticky="nesw")
        
        huit = Button(self, text="8", highlightbackground='gold4', command =lambda : self.modif_chaine_calcul(8))
        huit.grid(row = 5, column = 1, sticky="nesw")
        
        neuf = Button(self, text="9", highlightbackground='gold4', command =lambda : self.modif_chaine_calcul(9))
        neuf.grid(row = 5, column = 2, sticky="nesw")
        
        zero = Button(self, text="0", highlightbackground='gold4', command = lambda : self.modif_chaine_calcul(0))
        zero.grid(row = 6, column = 1, sticky="nesw")
        
        point = Button(self, text=",", highlightbackground='goldenrod', command = lambda : self.modif_chaine_calcul("."))
        point.grid(row = 6, column = 2, sticky="nesw")
        
        parenthese_gauche = Button(self, text="(", highlightbackground='royal blue', command = lambda : self.modif_chaine_calcul("("))
        parenthese_gauche.grid(row = 7, column = 2, sticky="nesw")

        parenthese_droite = Button(self, text=")", highlightbackground='royal blue', command = lambda : self.modif_chaine_calcul(")"))
        parenthese_droite.grid(row = 7, column = 3, sticky="nesw")

        pi = Button(self, text="π", highlightbackground='goldenrod', command = lambda : self.modif_chaine_calcul("π"))
        pi.grid(row = 6, column = 0, sticky="nesw")

    def creation_operateur(self):
        plus = Button(self, text="+", highlightbackground='royal blue', command = lambda : self.modif_chaine_calcul("+"))
        plus.grid(row = 3, column = 3, sticky="nesw")
        
        moins = Button(self, text ="-", highlightbackground='royal blue', command =lambda :  self.modif_chaine_calcul("-"))
        moins.grid(row = 4, column = 3, sticky="nesw")
        
        produit = Button(self, text="x", highlightbackground='royal blue', command = lambda : self.modif_chaine_calcul("*"))
        produit.grid(row = 5, column = 3, sticky="nesw")
        
        div = Button(self, text="/", highlightbackground='royal blue', command = lambda : self.modif_chaine_calcul("/"))
        div.grid(row = 6, column = 3, sticky="nesw")
        
        cos = Button(self, text = "cos", highlightbackground='SpringGreen4', command = lambda : self.modif_chaine_calcul("cos(self.raddeg*"))
        cos.grid(row = 8, column = 0, sticky="nesw")
        
        sin = Button(self, text = "sin", highlightbackground='SpringGreen4', command = lambda : self.modif_chaine_calcul("sin(self.raddeg*"))
        sin.grid(row = 8, column = 1, sticky="nesw")
        
        tan = Button(self, text = "tan", highlightbackground='SpringGreen4', command = lambda : self.modif_chaine_calcul("tan(self.raddeg*"))
        tan.grid(row = 8, column = 2, sticky="nesw")
        
        carre = Button(self, text = "²", highlightbackground='royal blue', command = lambda : self.modif_chaine_calcul("**2"))
        carre.grid(row = 7, column = 0, sticky="nesw")
        
        racine = Button(self, text = "√", highlightbackground='royal blue', command = lambda : self.modif_chaine_calcul("sqrt("))
        racine.grid(row = 7, column = 1, sticky="nesw")
        
        equal = Button(self, text="=", highlightbackground='red3', command = self.calcul)
        equal.grid(row =8, column = 3, sticky="nesw")
        
        clearAll = Button(self, text="CLEAR", highlightbackground='OrangeRed4', command = self.clearAll_chaine_calcul)
        clearAll.grid(row = 9, column = 1, columnspan = 1, sticky = "nesw")

        del_ = Button(self, text="DEL", highlightbackground='OrangeRed4', command=self.del_chaine_calcul)
        del_.grid(row=9, column=0, sticky="nesw")
        
        ans = Button(self, text="ANS", highlightbackground='OrangeRed2', command = self.ans)
        ans.grid(row=9, column = 2, sticky = "nesw")
        
        rad_deg = Button(self, textvariable=self.radordeg, highlightbackground='OrangeRed2', command=self.changeraddeg)
        rad_deg.grid(row=9, column=3, sticky = "nesw")


def main():
    calculatrice = Calculatrice()
    calculatrice.mainloop()
    
main()



