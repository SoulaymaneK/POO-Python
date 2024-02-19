from tkinter import *
from math import cos,sin,tan,pi,sqrt,degrees,radians
π = pi
class Calculatrice(Tk) :    
    def __init__(self,l = 600,h = 500):
        Tk.__init__(self)
        x = self.winfo_screenwidth() 
        y = self.winfo_screenheight() 
        pos_x = x//2 - l//2
        pos_y = y//2 - h//2
        geometrie = f"{l}x{h}+{pos_x}+{pos_y}"
        self.geometry(geometrie)
        self.title("TP calculatrice")
        self.config(bg="dimgrey")
      
        self.rowconfigure([i for i in range(10)], weight =1)
        self.columnconfigure([i for i in range(4)], weight=1)
        
        self.creation_chaine()
        self.creation_label()
        self.creation_chiffre()
        self.creation_operateur()
        
      
    def creation_chaine(self):
        self.chaine_calcul = StringVar()
        self.chaine_calcul.set("")
        self.chaine_visible = StringVar()
        self.chaine_visible.set("")
        self.ANS = self.chaine_calcul.get() 
   
         
    def creation_label(self): 
        self.label1 = Label(self, text="Calculatrice", bg="dimgrey", fg="black", relief="groove", borderwidth=3)
        self.label1.grid(row =0, rowspan = 1, column = 1, columnspan = 2)
        self.label2 = Label(self, textvariable = self.chaine_visible, bg="dimgrey", fg="black")
        self.label2.grid(row = 2, column= 2, columnspan = 2)
        self.ans_label = Label(self,text=f"ANS : ", bg="dimgrey", fg="black")
        self.ans_label.grid(row=2,column=0, columnspan = 2)
        
    def modif_chaine_calcul(self, x):
        if x=="**2" :
            self.chaine_visible.set(self.chaine_visible.get()+"²")
            self.chaine_calcul.set(self.chaine_calcul.get()+str(x))
        elif x=="sqrt(":
            self.chaine_visible.set(self.chaine_visible.get()+"√(")
            self.chaine_calcul.set(self.chaine_calcul.get()+str(x))
        elif x=="ANS":
            self.chaine_visible.set(self.chaine_visible.get()+"ANS")
            self.chaine_calcul.set(self.chaine_calcul.get()+self.ANS)
        else : 
            self.chaine_visible.set(self.chaine_visible.get()+str(x))
            self.chaine_calcul.set(self.chaine_calcul.get()+str(x))
            
    def ans(self):
       self.modif_chaine_calcul("ANS")
       self.ANS = ""
          
    def clear_chaine_calcul(self):
        self.chaine_calcul.set("")
        self.chaine_visible.set("")
    
    def del_(self):
        self.chaine_calcul.set(self.chaine_calcul.get()[:len(self.chaine_calcul.get())-1]) 
        self.chaine_visible.set(self.chaine_visible.get()[:len(self.chaine_visible.get())-1])
        
    def calcul(self):
        exec("self.chaine_visible.set(str("+self.chaine_calcul.get()+"))")     
        self.ANS = self.chaine_visible.get()
        self.chaine_calcul.set(self.chaine_visible.get())
        self.ans_label.configure(text=f"ANS : {self.chaine_visible.get()}")
            
            
    def creation_chiffre(self):
        
        un = Button(self, text="1", bg="dimgrey",fg="black", command = lambda : self.modif_chaine_calcul(1))
        un.grid(row = 3, column=0, sticky="nesw")
    
        deux = Button(self, text="2",highlightbackground="dimgrey", fg="black",command = lambda : self.modif_chaine_calcul(2))
        deux.grid(row = 3, column = 1, sticky="nesw")
        
        trois = Button(self, text="3",highlightbackground="dimgrey", fg="black", command = lambda : self.modif_chaine_calcul(3))
        trois.grid(row = 3, column = 2, sticky="nesw")
        
        quatre = Button(self, text="4",highlightbackground="dimgrey", fg="black", command =lambda : self.modif_chaine_calcul(4))
        quatre.grid(row = 4, column = 0, sticky="nesw")
        
        cinque = Button(self, text="5",highlightbackground="dimgrey", fg="black", command =lambda : self.modif_chaine_calcul(5))
        cinque.grid(row = 4, column = 1, sticky="nesw")
        
        six = Button(self, text="6",highlightbackground="dimgrey", fg="black", command =lambda : self.modif_chaine_calcul(6))
        six.grid(row = 4, column = 2, sticky="nesw")
        
        sept = Button(self, text="7",highlightbackground="dimgrey", fg="black", command =lambda : self.modif_chaine_calcul(7))
        sept.grid(row = 5, column = 0, sticky="nesw")
        
        huit = Button(self, text="8", highlightbackground="dimgrey", fg="black",command =lambda : self.modif_chaine_calcul(8))
        huit.grid(row = 5, column = 1, sticky="nesw")
        
        neuf = Button(self, text="9",highlightbackground="dimgrey", fg="black",command =lambda : self.modif_chaine_calcul(9))
        neuf.grid(row = 5, column = 2, sticky="nesw")
        
        zero = Button(self, text="0",highlightbackground="dimgrey", fg="black",command = lambda : self.modif_chaine_calcul(0))
        zero.grid(row = 6, column = 1, sticky="nesw")
        
        point = Button(self, text=".",bg="dimgrey", fg="black", command = lambda : self.modif_chaine_calcul("."))
        point.grid(row = 6, column = 2, sticky="nesw")
        
        paranthèse_droite = Button(self, text=")",bg="dimgrey", fg="black", command = lambda : self.modif_chaine_calcul(")"))
        paranthèse_droite.grid(row = 7, column = 3, sticky="nesw") 
        
        paranthèse_gauche = Button(self, text="(",bg="dimgrey", fg="black", command = lambda : self.modif_chaine_calcul("("))
        paranthèse_gauche.grid(row = 7, column = 2, sticky="nesw")
        
        pi = Button(self, text="π",bg="dimgrey", fg="black", command = lambda : self.modif_chaine_calcul("π"))
        pi.grid(row = 6, column = 0, sticky="nesw")
        
    
    def creation_operateur(self):
        plus = Button(self, text="+",highlightbackground="darkorange", fg="black",command = lambda : self.modif_chaine_calcul("+"))
        plus.grid(row = 3, column = 3, sticky="nesw")
        
        moins = Button(self, text ="-",highlightbackground="darkorange", fg="black", command =lambda :  self.modif_chaine_calcul("-"))
        moins.grid(row = 4, column = 3, sticky="nesw")
        
        fois = Button(self, text="*", highlightbackground="darkorange", fg="black",command = lambda : self.modif_chaine_calcul("*"))
        fois.grid(row = 5, column = 3, sticky="nesw")
        
        div = Button(self, text="/",highlightbackground="darkorange", fg="black", command = lambda : self.modif_chaine_calcul("/"))
        div.grid(row = 6, column = 3, sticky="nesw")
        
        cos = Button(self, text = "cos",highlightbackground="darkorange", fg="black", command = lambda : self.modif_chaine_calcul("cos("))
        cos.grid(row = 8, column = 0, sticky="nesw")
        
        sin = Button(self, text = "sin",highlightbackground="darkorange", fg="black", command = lambda : self.modif_chaine_calcul("sin("))
        sin.grid(row = 8, column = 1, sticky="nesw")
        
        tan = Button(self, text = "tan",highlightbackground="darkorange", fg="black", command = lambda : self.modif_chaine_calcul("tan("))
        tan.grid(row = 8, column = 2, sticky="nesw")
        
        carre = Button(self, text = "x²", highlightbackground="darkorange", fg="black",command = lambda : self.modif_chaine_calcul("**2"))
        carre.grid(row = 7, column = 0, sticky="nesw")
        
        racine = Button(self, text = "√x",highlightbackground="darkorange", fg="black", command = lambda : self.modif_chaine_calcul("sqrt("))
        racine.grid(row = 7, column = 1, sticky="nesw")
        
        ans = Button(self, text="ANS", bg="darkorange", fg="black", command = self.ans)
        ans.grid(row=9, column = 2, sticky = "nesw")
        
        equal  = Button(self, text="=", bg="darkorange", fg="black", command = self.calcul)
        equal.grid(row =8, column = 3, sticky="nesw")
        
        clear = Button(self, text="Clear",  bg="darkorange", fg="black",command = self.clear_chaine_calcul)
        clear.grid(row = 9, column = 0, columnspan = 2, sticky = "nesw")
        
        del_ = Button(self, text="DEL",  bg="darkorange", fg="black",command  = self.del_)
        del_.grid(row = 9, column = 3, sticky = "nesw")
        
        
def main():
    fenetre = Calculatrice()
    fenetre.mainloop()
    
main()
        
     
        